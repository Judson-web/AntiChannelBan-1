from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Client.on_message(filters.command(["start", "dark"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hʟᴏ {message.from_user.first_name} 😉️!</b>
 `Hᴇʏᴀ I'ᴍ Aɴ Aɴᴛɪ Cʜᴀɴɴᴇʟ Tᴇɢʀᴀᴍ Bᴏᴛ Tᴏ Dᴇʟᴇᴛᴇ Aɴᴅ Bᴀɴ Mᴇssᴀɢᴇ Sᴇɴᴅ BY Cʜᴀɴɴᴇʟ`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Hᴇʟᴘ", url="https://t.me/DeeCodeBots"
                    ),
                    InlineKeyboardButton(
                        "Sᴜᴘᴘᴏʀᴛ", url="https://t.me/STMbOTsUPPORTgROUP"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Bᴏᴛ Eᴅɪᴛᴏʀ", url="https://t.me/VAMPIRE_KING_NO_1"
                    )
                ]
            ]
        )
    )
