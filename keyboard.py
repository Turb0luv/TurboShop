from aiogram.types import ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

button1 = KeyboardButton("⏩АССОРТИМЕНТ⏪")
button2 = KeyboardButton("МОЙ ПРОФИЛЬ👤")

markup = ReplyKeyboardMarkup(resize_keyboard=True).row(button1).add(button2)

btn_1 = KeyboardButton('HUSKY 45MG', callback_data='liq_button1')
btn_2 = KeyboardButton('HOTSPOT 60MG', callback_data='liq_button2')
btn_3 = KeyboardButton('XYLINET 40MG', callback_data='liq_button3')
# btn_4 = KeyboardButton('PODONKI 60MG', callback_data='liq_button4')
# btn_5 = KeyboardButton('HUSKY PREMIUM 50MG', callback_data='liq_button5')
btn_6 = KeyboardButton('GENETIC CODE 50MG', callback_data='liq_button6')
# btn_7 = KeyboardButton('GLITCH SAUCE 50MG', callback_data='liq_button7')
btn_esc = KeyboardButton('◀️НАЗАД')

assort_buttons = ReplyKeyboardMarkup(resize_keyboard=True).row(btn_1, btn_2, btn_3).add(btn_6,
                                                                                        btn_esc)  # .add(btn_4, btn_5, btn_6, btn_7)#.add(btn_esc)

btn_yes = InlineKeyboardButton('✅', callback_data='pac_yes')
btn_no = InlineKeyboardButton('❌', callback_data='pac_no')

last_buttons = InlineKeyboardMarkup(row_width=1).add(btn_yes, btn_no)
