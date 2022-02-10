import logging
# import hashlib
from aiogram import Bot, Dispatcher,executor,types
# from aiogram.types import InlineQuery, InputTextMessageContent,InlineQueryResultArticle
from config import TOKEN

BOT_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)
    # default row_width is 3, so here we can omit it actually
    # kept for clearness

    btns_text = ('Yes!', 'No!')
    keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
    # adds buttons as a new row to the existing keyboard
    # the behaviour doesn't depend on row_width attribute

    more_btns_text = (
        "I don't know",
        "Who am i?",
        "Where am i?",
        "Who is there?",
    )
    keyboard_markup.add(*(types.KeyboardButton(text) for text in more_btns_text))
    # adds buttons. New rows are formed according to row_width parameter

    await message.reply("Hi!\nDo you like aiogram?", reply_markup=keyboard_markup)


@dp.message_handler()
async def all_msg_handler(message: types.Message):
    # pressing of a KeyboardButton is the same as sending the regular message with the same text
    # so, to handle the responses from the keyboard, we need to use a message_handler
    # in real bot, it's better to define message_handler(text="...") for each button
    # but here for the simplicity only one handler is defined

    button_text = message.text
    logger.debug('The answer is %r', button_text)  # print the text we've got

    if button_text == 'Yes!':
        reply_text = "That's great"
    elif button_text == 'No!':
        reply_text = "Oh no! Why?"
    else:
        reply_text = "Keep calm...Everything is fine"

    await message.reply(reply_text, reply_markup=types.ReplyKeyboardRemove())
    # with message, we send types.ReplyKeyboardRemove() to hide the keyboard

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)





# @dp.message_handler(commands='start')
# async def start_cmd_handler(message: types.Message):
#     keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
#     # default row_width is 3, so here we can omit it actually
#     # kept for clearness
#
#     text_and_data = (
#         ('Yes', 'yes'),
#         ('No', 'no'),
#     )
#     # in real life for the callback_data the callback data factory should be used
#     # here the raw string is used for the simplicity
#     row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
#
#     keyboard_markup.row(*row_btns)
#     keyboard_markup.add(
#         # url buttons have no callback data
#         types.InlineKeyboardButton('aiogram source', url='https://robocode.uz'),
#     )
#
#     await message.reply("Hi Do you love aiogram?", reply_markup=keyboard_markup)
#
#
# # Use multiple registrators. Handler will execute when one of the filters is OK
# @dp.callback_query_handler(text='no')  # if cb.data == 'no'
# @dp.callback_query_handler(text='yes')  # if cb.data == 'yes'
# async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
#     answer_data = query.data
#     # always answer callback queries, even if you have nothing to say
#     await query.answer(f'You answered with {answer_data!r}')
#
#     if answer_data == 'yes':
#         text = 'Great, me too'
#     elif answer_data == 'no':
#         text = 'Oh no Why so?'
#     else:
#         text = f'Unexpected callback data {answer_data!r}'
#
#     await bot.send_message(query.from_user.id, text)