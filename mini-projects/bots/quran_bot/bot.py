from aiogram import Bot, Dispatcher, types, executor
import keyboards as kb
API_TOKEN = "5001741680:AAE4IAJoxFtr15EpKIEOckvFq5z7xCNy_DI"

ID = 668618297

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    bot = Bot.get_current()
    user = types.User.get_current()
    print(bot, user)

    await message.answer(message.text, reply_markup=kb.greet_kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
