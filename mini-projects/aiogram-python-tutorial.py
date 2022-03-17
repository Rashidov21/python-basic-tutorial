# pip install aiogram
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile


api = ""
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=api)
dp = Dispatcher(bot)
print(__name__) # file name
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!")

@dp.message_handler(content_types=["text"])
async def echo(message: types.Message):

    # for i in dir(message):
    #     print(i)
    p = InputFile('../images/python.png')
    # print(message.photo)
    # print(message.from_user)
    # with open("../images/python.png") as photo:
    await message.reply_photo(p, "Python")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)