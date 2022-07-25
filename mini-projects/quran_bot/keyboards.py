from aiogram.types import (ReplyKeyboardRemove,
                           ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


button_hi = KeyboardButton('Привет! 👋')

greet_kb1 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=False).add(button_hi)
