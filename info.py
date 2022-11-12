from aiogram.types import ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


class Info:
    other = []
    buttons = []

    def __init__(self, name, price, other):
        self.info = name + " \nЦЕНА:" + price
        self.other = other

    inbuttons = InlineKeyboardMarkup(row_width=1).add(buttons)

    def crbutt(self):
        return InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(self.other[0], callback_data='liq_'+self.other[0]),
                                                     InlineKeyboardButton(self.other[1], callback_data='liq_'+self.other[1]),
                                                     InlineKeyboardButton(self.other[2], callback_data='liq_'+self.other[2]),
                                                     InlineKeyboardButton(self.other[3], callback_data='liq_'+self.other[3]),
                                                     InlineKeyboardButton(self.other[4], callback_data='liq_'+self.other[4]),
                                                     InlineKeyboardButton(self.other[5], callback_data='liq_'+self.other[5]),
                                                     InlineKeyboardButton(self.other[6], callback_data='liq_'+self.other[6]),
                                                     InlineKeyboardButton(self.other[7], callback_data='liq_'+self.other[7]),
                                                     )