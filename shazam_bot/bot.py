# pip install aiogram 
import asyncio
import json 
import pprint
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from aiogram import html # html matn formati
from aiogram import F # message filter

from config import BOT_TOKEN
from api import search_from_api

bot = Bot(token=BOT_TOKEN) # configdan bot tokeni olindi
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello! This is Shazam Bot !")

@dp.message(F.text)
async def search_music(message: types.Message):
    res = search_from_api(message.text)
    print()
    if not res:
        await message.answer(html.bold("Not found !"), parse_mode="HTML")
    else: 
        for i in range(len(res.get("tracks").get('hits'))):
            hit = res.get("tracks").get('hits')[i].get("track")
            bg = hit.get("images").get("background")
            await message.answer(html.bold(f"Track : {hit.get('title')}\nArtist : {hit.get ('subtitle')}"), parse_mode="HTML")
            await message.content_type
            

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())