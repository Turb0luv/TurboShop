from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

import info
import keyboard as kb

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
    await bot.send_message(message.from_user.id, '👋🏻 Привет! Добро пожаловать в TurboShop.'
                                                 '\nДля просмотра ассортимента жидкостей - нажми Ассортимент'
                                                 '\nСамовывоз - ЖД Вокзал Гродно'
                                                 '\nУдобное время для встречи указывайте в коммнтарии к заказу'
                                                 '\nПо всем вопросам - @Turb0Luv', reply_markup=kb.markup)


@dp.message_handler(Text(equals="Ассортимент"))
async def katalog(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбери линейку", reply_markup=kb.assort_buttons)


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


# @dp.message_handler(Text(equals="Мой кабинет👤"))
# async def kabinet(message: types.Message):
#   await bot.send_message(message.from_user.id, "мой кабинет")
l = ''


@dp.callback_query_handler(text_contains="liq_")
async def botShop(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    global l
    l = rename.info + "\n" + call.data + "\n@" + call.from_user.username
    await bot.send_message(call.from_user.id, "Напиши предпочтительное время")
    # await bot.send_message(438102155, husky.info + "\n" + husky.inline_btn_1.text + "\n@" + call.from_user.username)


@dp.message_handler(content_types=["text"])
async def read(message):
    if len(l) != 0:
        await bot.send_message(438102155, l + "\n" + message.text)
        await bot.send_message(message.from_user.id, "В ближайшее время с вами свяжутся. Ожидайте!")
        gh()


def gh():
    global l
    l = ''


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
