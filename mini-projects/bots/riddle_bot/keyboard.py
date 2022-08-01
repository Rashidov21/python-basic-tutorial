import emoji
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

inline_btn_1 = InlineKeyboardButton(
    'получить все контакты', callback_data='get_contacts')
inline_kb = InlineKeyboardMarkup().add(inline_btn_1)

markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
)


# get_phone = ReplyKeyboardButton(
#     f"Telefon {emoji.emojize(':mobile_phone: ')}", callback_data='get_contact',
#     request_contact=True)

# kb = ReplyKeyboardMarkup().add(get_phone)  # resize_keyboard=True
