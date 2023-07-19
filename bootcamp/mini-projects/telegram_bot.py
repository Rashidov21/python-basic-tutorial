# pip install -U --pre aiogram
import asyncio
import logging
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "6399580721:AAEw0NLho_ttVPnum751Vg6dotYaqJgHKi4"
router = Router()

@router.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Birinchi tugma 🙀"),
            types.KeyboardButton(text="Ikkinchi tugma 😹")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Tugmalardan birini tanlang "
    )
    await message.answer("Tugmalardan birini tanlang", reply_markup=keyboard)

@router.message()
async def with_puree(message: types.Message):
    if message.text == "Birinchi tugma 🙀":
        await message.reply("Siz birinchi tugmani tanladingiz!")
    if message.text == "Ikkinchi tugma 😹":
        await message.reply("Siz ikinchi tugmani tanladingiz!")
    
@router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")




async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(TOKEN, parse_mode="HTML")
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())