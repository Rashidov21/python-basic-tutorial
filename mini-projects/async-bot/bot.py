import logging
from aiogram import Bot, Dispatcher,executor,types
from markup import otherMenu, mainMenu, getContactBtn
from config import TOKEN

BOT_TOKEN = TOKEN
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    user = message.from_user.username
    gr = message.chat.type
    # with open("src/nike.jpg",'rb') as ph:
    #     await message.reply_photo(ph,"Nike JPG")
    await message.reply(f"Hello! @{user} - {gr}", reply_markup=getContactBtn)


print(getContactBtn)


@dp.message_handler()
async def all_msg_handler(message: types.Message):

    await message.voice_chat_started
    # with message, we send types.ReplyKeyboardRemove() to hide the keyboard

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)