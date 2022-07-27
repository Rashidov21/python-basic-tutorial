import emoji
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


pzbtn = InlineKeyboardButton(
    f'Topishmoq! {emoji.emojize(":winking_face_with_tongue:")}', callback_data='get')

kb = InlineKeyboardMarkup()  # resize_keyboard=True
kb.add(pzbtn)
