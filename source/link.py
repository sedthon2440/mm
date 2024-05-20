from pyrogram import Client, filters, idle
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@Client.on_message(filters.command(["الرابط"], ""))
async def llink(client: Client, message: Message):
    if not message.from_user.username in ["R7_OX"]:
      return
    chat_id = message.text.split(None, 1)[1].strip()
    invitelink = (await client.export_chat_invite_link(chat_id))
    await message.reply_text("**رابط المجموعة .**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("الرابط", url=f"{invitelink}")]]))
