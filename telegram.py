from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

import peewee
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import info
import keyboard as kb
from db import *

bot = Bot(token="5692590643:AAHB8UY6_wN3vx5ovWtQPn-ecIM2Ow-ZJeI")
dp = Dispatcher(bot)

husky = info.Info('HUSKY 45MG ОРИГИНАЛ', "13р",
                  ['Сочная Маракуя', 'Жвачка Манго', 'Кислое яблоко', 'Мятная Жвачка', 'Энергетик, киви, фейхова',
                   'Конфета Личи', '', '', ''])

hotspot = info.Info('HOTSPOT 60MG', '13р',
                    ['🍏🍏Кислое Яблоко', '🥝🥝Кислый Киви', '🍇🍇Кислая Маракуйя', '🍍🍍Кислый Ананас', '', '', '', '', ''])

genetic = info.Info("GENETIC CODE 50MG", '13р',
                    ['🍓🍈Клубника Дыня', '🍍🍒Ананас Клюква', '🥭🍌Манго Банан', '🍐🍊Маракуйя Кумкват', '🍇🥤Виноградная Кола',
                     '🥝🍐Шелковица Киви Гуава', '🍉🍓Арбуз Грейпфрут Малина', ''])

xylinet = info.Info("XYLINET 40MG", '13р', ['🍓🍋Malinovyi Fisting', '🍑🍍Persikovyi Kuni',
                                            '🍋🍸Myatnaya Irrymatsiya', '🍐🍋Tropicheski Skvirt', '🍍🍯Ananasovyi Kamshot',
                                            '', '', '', ''])


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    _ = User.get_or_create(id=message.from_user.id,
                           defaults={'username': message.from_user.username, 'count': 0, 'lastbuy': '-'})
    await bot.send_message(message.from_user.id, '👋🏻 Привет!'
                                                 '\nДобро пожаловать в <b>TurboShop</b>.'
                                                 '\nВыбор жидкости: жми ниже ⬇️<b>АССОРТИМЕНТ</b>⬇️.'
                                                 '\nСамовывоз:<b>ЖД Вокзал-Гродно</b>.'
                                                 '\nУдобное время для встречи указывай в комментарии к заказу.'
                                                 '\nПо всем вопросам - @Turb0Luv', parse_mode="HTML",
                           reply_markup=kb.markup)


@dp.message_handler(Text(equals="⏩АССОРТИМЕНТ⏪"))
async def katalog(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбери линейку", reply_markup=line_markup)


@dp.message_handler(Text(equals="◀️НАЗАД"))
async def back(message: types.Message):
    await bot.send_message(message.from_user.id, "Главное меню", reply_markup=kb.markup)


@dp.message_handler(Text(equals="HUSKY 45MG"))
async def huskyflavor(message: types.Message):
    global rename
    rename = husky
    await bot.send_message(message.from_user.id, rename.info + "\n\nВыбери вкус:", reply_markup=rename.crbutt())


@dp.message_handler(Text(equals="HOTSPOT 60MG"))
async def hotspotflavor(message: types.Message):
    global rename
    rename = hotspot
    await bot.send_message(message.from_user.id, rename.info + "\n\nВыбери вкус:", reply_markup=rename.crbutt())


@dp.message_handler(Text(equals="GENETIC CODE 50MG"))
async def geneticflavor(message: types.Message):
    global rename
    rename = genetic
    await bot.send_message(message.from_user.id, rename.info + "\n\nВыбери вкус:", reply_markup=rename.crbutt())


@dp.message_handler(Text(equals="XYLINET 40MG"))
async def xylinetflavor(message: types.Message):
    global rename
    rename = xylinet
    await bot.send_message(message.from_user.id, rename.info + "\n\nВыбери вкус:", reply_markup=rename.crbutt())


@dp.message_handler(Text(equals="МОЙ ПРОФИЛЬ👤"))
async def profile(message: types.Message):
    user = User.get(User.id == message.from_user.id)
    await bot.send_message(message.from_user.id, "Профиль:" + '\nИмя: ' + user.username + "\nКол-во заказов: " + str(
        user.count) + '\nПоследний заказ: ' + user.lastbuy, reply_markup=kb.btn_esc)


l = ''


@dp.callback_query_handler(text_contains="liq_")
async def botShop(call: types.CallbackQuery):
    user = User.get(User.id == call.from_user.id)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    global l
    l = rename.info + "\n" + call.data.replace('liq_', '')
    if call.from_user.username:
        l += "\nTG: @" + call.from_user.username
    else:
        l += "\n" + call.from_user.url
    await bot.send_message(call.from_user.id, "Укажи предпочтительное время и комментарий(если нужен)")
    # await bot.send_message(438102155, husky.info + "\n" + husky.inline_btn_1.text + "\n@" + call.from_user.username)


# @dp.message_handler(Text(equals="РАССЫЛКА"))
# async def katalog(message: types.Message):
#   await receiver()

@dp.message_handler(content_types=["text"])
async def read(message):
    user = User.get(User.id == message.from_user.id)
    if len(l) != 0:
        global time
        time = message.text
        await bot.send_message(message.from_user.id,
                               'Ваш заказ:' + '\n' + l + "\nКомментарий:" + time + '\nПОДТВЕРЖДАЕМ?',
                               reply_markup=kb.last_buttons)


@dp.callback_query_handler(text_contains="pac_yes")
async def read(message):
    user = User.get(User.id == message.from_user.id)
    user.count += 1
    if len(l) != 0:
        await bot.delete_message(message.from_user.id, message.message.message_id)
        await bot.send_message(message.from_user.id, 'Ваш заказ:' + '\n' + l + "\n" + time)
        await bot.send_message(message.from_user.id, "В ближайшее время с вами свяжутся. Ожидайте!",
                               reply_markup=kb.markup)
        await bot.send_message(438102155, l + "\n" + time)
        gh()


@dp.callback_query_handler(text_contains="pac_no")
async def read(message):
    if len(l) != 0:
        await bot.send_message(message.from_user.id, "Возврат в меню", reply_markup=kb.assort_buttons)
        await bot.delete_message(message.from_user.id, message.message.message_id)
        gh()


class LineMarkup(ReplyKeyboardMarkup):
    def __init__(self):
        buttons = []
        for line in Line.select():
            buttons.append(KeyboardButton(Line.name, callback_data=Line.id))
        ReplyKeyboardMarkup.add(buttons)
        self.one_time_keyboard = False
        self.resize_keyboard = True


async def receiver():
    global users
    for user in users:
        await bot.send_message(user, "XYI")


def gh():
    global l
    l = ''


if __name__ == '__main__':
    line_markup = LineMarkup()
    executor.start_polling(dp, skip_updates=True)
