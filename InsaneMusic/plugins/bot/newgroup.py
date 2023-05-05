from pyrogram import Client, filters
from pyrogram.types import Message
from config import LOG_GROUP_ID
from InsaneMusic import app


async def new_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)


@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        title = message.chat.title
        chat_id = message.chat.id
        Insane = f"#ɴᴇᴡ ɢʀᴏᴜᴘ\n\nᴄʜᴀᴛ ɪᴅ : {chat_id}\nᴄʜᴀᴛ ᴛɪᴛʟᴇ : {title}\nᴀᴅᴅᴇᴅ ʙʏ : {added_by}"
        await new_message(LOG_GROUP_ID, Insane)
