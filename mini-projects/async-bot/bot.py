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
    with open("src/nike.jpg",'rb') as ph:
        await message.reply_photo(ph,"Nike JPG")
    await message.reply("Hello")

    # keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)
    # # default row_width is 3, so here we can omit it actually
    # # kept for clearness
    #
    # btns_text = ('Yes!', 'No!')
    # keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
    # # adds buttons as a new row to the existing keyboard
    # # the behaviour doesn't depend on row_width attribute
    #
    # more_btns_text = (
    #     "I don't know",
    #     "Who am i?",
    #     "Where am i?",
    #     "Who is there?",
    # )
    # keyboard_markup.add(*(types.KeyboardButton(text) for text in more_btns_text))
    # # adds buttons. New rows are formed according to row_width parameter
    #
    # await message.reply("Hi!\nDo you like aiogram?", reply_markup=keyboard_markup)


@dp.message_handler()
async def all_msg_handler(message: types.Message):


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