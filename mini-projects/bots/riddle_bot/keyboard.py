import emoji
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
).add(
    KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
)


# get_phone = ReplyKeyboardButton(
#     f"Telefon {emoji.emojize(':mobile_phone: ')}", callback_data='get_contact',
#     request_contact=True)

# kb = ReplyKeyboardMarkup().add(get_phone)  # resize_keyboard=True
