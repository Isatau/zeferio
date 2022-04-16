#	▀▀█ █▀▀ █▀▀ █▀▀ █▀▀█ ░▀░ █▀▀█ 
#	▄▀░ █▀▀ █▀▀ █▀▀ █▄▄▀ ▀█▀ █░░█ 
#	▀▀▀ ▀▀▀ ▀░░ ▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀▀
#
#              © Copyright 2022
#
#          https://t.me/zeferio
#
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

from .. import loader
import logging
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from random import choice
import os

logger = logging.getLogger(__name__)
imgs = [
    "https://github.com/Isatau/img/blob/main/giphy.gif?raw=true",
    "https://github.com/Isatau/img/blob/main/tumblr_mfp5x7csiT1rpfx57o1_500.gif?raw=true",
    "https://github.com/Isatau/img/blob/main/giphy%20(1).gif?raw=true",
    "https://github.com/Isatau/img/blob/main/giphy%20(2).gif?raw=true",
    "https://github.com/Isatau/img/blob/main/giphy%20(3).gif?raw=true",
    "https://github.com/Isatau/img/blob/main/original.gif?raw=true",
    "https://github.com/Isatau/img/blob/main/anime-hug-50.gif?raw=true",
]

TEXT = """👾🇬🇧 <b>Hello.</b> You've just installed <b>Zeferio</b> userbot.

📼 <b>Modules sources: </b>
▫️ @hikarimods
▫️ @ftg2bot 
▫️ @hikarimods_database
▫️ <code>.dlmod</code>

"""


TEXT_RU = """👾🇷🇺 <b>Привет.</b> Твой юзербот <b>Zeferio</b> установлен.

📼 <b>Источники модулей: </b>
▫️ @hikarimods
▫️ @ftg2bot 
▫️ @hikarimods_database
▫️ <code>.dlmod</code>

"""

if "OKTETO" in os.environ:
    TEXT += "☁️ <b>Your userbot is installed on Okteto</b>. Don't worry, you will get some notifications from @WebpageBot. Do not block him."
    TEXT_RU += "☁️ <b>Твой юзербот установлен на Okteto</b>. Не пугайся, когда будешь получать уведомления от @WebpageBot и не блокируй его."


@loader.tds
class QuickstartMod(loader.Module):
    """Notifies user about userbot installation"""

    strings = {"name": "Quickstart"}

    async def client_ready(self, client, db) -> None:
        self._me = (await client.get_me()).id

        mark = InlineKeyboardMarkup()
        mark.add(
            InlineKeyboardButton(
                "🥷 Support chat",
                url="https://t.me/zeferiot",
            ),
        )

        mark.add(
            InlineKeyboardButton(
                "🇷🇺 Русский",
                callback_data="zeferio_qs_sw_lng_ru",
            ),
        )

        await self.inline.bot.send_animation(
            self._me,
            animation=choice(imgs),
            caption=TEXT,
            parse_mode="HTML",
            reply_markup=mark,
        )

        db.set("zeferio", "disable_quickstart", True)

    async def quickstart_callback_handler(self, call: CallbackQuery) -> None:
        if not call.data.startswith("zeferio_qs_sw_lng_"):
            return

        lang = call.data.split("_")[-1]
        if lang == "ru":
            mark = InlineKeyboardMarkup()
            mark.add(
                InlineKeyboardButton(
                    "🥷 Чат помощи",
                    url="https://t.me/zeferiot",
                ),
            )
            mark.add(
                InlineKeyboardButton(
                    "🇬🇧 English",
                    callback_data="zeferio_qs_sw_lng_en",
                ),
            )

            await self.inline.bot.edit_message_caption(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                caption=TEXT_RU,
                parse_mode="HTML",
                reply_markup=mark,
            )
        elif lang == "en":
            mark = InlineKeyboardMarkup()
            mark.add(
                InlineKeyboardButton(
                    "🥷 Support chat",
                    url="https://t.me/zeferiot",
                ),
            )
            mark.add(
                InlineKeyboardButton(
                    "🇷🇺 Русский",
                    callback_data="zeferio_qs_sw_lng_ru",
                ),
            )

            await self.inline.bot.edit_message_caption(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                caption=TEXT,
                parse_mode="HTML",
                reply_markup=mark,
            )
