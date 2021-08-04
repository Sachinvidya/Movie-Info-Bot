# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from plugins.info import *


BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text='⚙ Join Updates Channel ⚙', url='https://telegram.me/FayasNoushad')
        ]]
    )


@Client.on_message(filters.private & filters.command(["start"]), group=-1)
async def start(bot, update):
    if update.text == "/start":
        await update.reply_text(f"Hi {update.from_user.mention},\nSend me a movie name")
    else:
        movie = update.text.split(" ", 1)
        await get_movie(bot, update, movie)
