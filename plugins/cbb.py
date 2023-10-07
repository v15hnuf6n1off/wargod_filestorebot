#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>✑ ᴄʀᴇᴀᴛᴏʀ :<a href='tg://user?id={OWNER_ID}'ʏᴏᴜʀ ғʀɪᴇɴᴅ</a>\n✑ ʟᴀɴɢᴜᴀɢᴇ :<a href='https://python.org'>ᴘʏᴛʜᴏɴ</a>\n✑ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ ᴀsʏɴᴄɪᴏ</a>\n✑ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://t.me/v15hnuf6n1x'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n✑ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/A1pher>ᗩ1ᑭᕼᗴᖇ</a>\n✑ ᴅᴇᴠ : <a href='https://t.me/Mr_V_bots'>Mr_V_bots</a></b>",
            disable_web_page_preview = False,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 ᴄʟᴏsᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
