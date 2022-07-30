import keyboards as kb
import os
from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
ID = os.getenv("ID")
print(API_TOKEN, ID)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Started!")


@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text, reply_markup=kb.greet_kb1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
