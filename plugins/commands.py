# Author: Surya Prabhas (https://github.com/SuryaPrabhas1245) (@suryaprabhas1245)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .info import get_movie

START_TEXT = """Hello {}
I am a movie information finder bot.

> `I can find information of all movies.`

Made by @SuryaPrabhas1245"""

JOIN_BUTTONS = [
    InlineKeyboardButton(
        text='⚙ Join Our Main Channel ⚙',
        url='https://telegram.me/TeluguDubbedHorrorMovies2'
    )
]

BUTTONS = InlineKeyboardMarkup(
    [JOIN_BUTTONS]
)

@Client.on_message(filters.private & filters.command(["start"]), group=-1)
async def start(bot, update):
    if update.text == "/start":
        await update.reply_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=BUTTONS,
            disable_web_page_preview=True,
            quote=True
        )
    else:
        movie = update.text.split(" ", 1)[1]
        await get_movie(bot, update, movie)
