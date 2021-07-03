# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import json
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


API = 'https://api.sumanjay.cf/watch/'


@Client.on_message(filters.command(["info", "information"]))
async def get_command(bot, update):
    movie = update.text.split(" ", 1)
    movie = movie.replace(" ", "+")
    movie = movie.replace("\n", "+")
    keyboard = [
        InlineKeyboardButton(
            text="Click here",
            url=f"https://telegram.me/{username}?start={movie}"
        )
    ]
    await update.reply_text(
        text=f"Click the button below",
        reply_markup=InlineKeyboardMarkup([keyboard]),
        disable_web_page_preview=True,
        quote=True
    )


@Client.on_message(filters.private & filters.text & ~filters.command(["start"]))
async def get_movie_name(bot, update):
    await get_movie(bot, update, update.text)


async def get_movie(bot, update, movie):
    movie_name = movie.replace(" ", "+")
    movie_name = movie_name.replace("\n", "+")
    movie_api = API + movie_name
    r = requests.get(movie_api)
    movies = r.json()
    keyboard = []
    number = 0
    for movie in movies:
        number += 1
        button_text = movie['title'] if movie['title'] else None
        button_text += " - " + movie['type'] if movie['type'] else None
        button_text += " - " + str(movie['release_year']) if movie['release_year'] else None
        switch_text = movie_link.encode() + "+" + str(number)
        keyboard.append(
            [
                InlineKeyboardButton(
                    text=button_text,
                    switch_inline_query_current_chat=switch_text
                )
            ]
        )
    await update.reply_text(
        text="Select required option",
        reply_markup=InlineKeyboardMarkup(keyboard),
        disable_web_page_preview=True,
        quote=True
    )


def info(movie):
    info = f"Title: {movie['title']}\n"
    info += f"Type: {movie['type']}\n"
    if movie['providers']:
        try:
            providers = movie['providers']
            info += f"Providers:"
            for provider in providers:
                info += f" [{provider}]({providers[provider]})"
            info += "\n"
        except:
            pass
    try:
        info += f"Release Date: {str(movie['release_date'])}\n"
    except:
        pass
    try:
        info += f"Release Year: {movie['release_year']}\n"
    except:
        pass
    try:
        if movie['score']:
            scores = movie['score']
            info += "Score:"
            for score in scores:
                info += f" {score} - {str(scores[score])}"
    except:
        pass
    return info


def thumb(movie):
    thumbnail = movie['movie_thumb']
    return thumbnail
