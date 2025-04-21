from UTTAM import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    "╭────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼ ──── ⚘\n┆⚘ ʜᴇʏ, ɪ ᴀᴍ : [˹ 🅢ᴀᴛʏᴀ 🅤sᴇʀʙᴏᴛ ˼](https://t.me/aboutchinnalu)\n┆⚘ ᴍᴏʀᴇ ᴀɴɪᴍᴀᴛɪᴏɴ,ғᴜɴ\n┊⚘ ᴘᴏᴡᴇʀғᴜʟ & ᴜsᴇғᴜʟ ᴜsᴇʀʙᴏᴛ\n╰───────────────────────\n────────────────────────\n❍ нσɯ тσ υʂҽ тнιʂ вσᴛ - [ᴛɪᴘs ʜᴇʀᴇ](https://t.me/BABY09_WORLD/178) \n────────────────────────\n❍ ʂҽʂʂισɳʂ ɠҽɳ вσᴛ ⁚ [sᴇssɪᴏɴ-ʙᴏᴛ](https://t.me/STRING_BABYGEN_BOT) \n────────────────────────\n❍ ¢ℓσɳҽ вσт ⁚ /clone [ ʂᴛɾιɳg ʂҽʂʂισɳ ]\n────────────────────────\n❍ ᴘσɯҽɾҽᴅ ʙу ⏤‌‌‌‌  [˹ ʙᴀʙʏ-ᴍᴜsɪᴄ ™˼𓅂](https://t.me/BABY09_WORLD) \n────────────────────────"
)

@app.on_message(filters.command("start"))
async def hello(client: app, message):
    buttons = [
           [
                InlineKeyboardButton("˹ ᴏᴡɴᴇʀ ˼", url="https://t.me/aboutchinnalu"),
                InlineKeyboardButton("˹ ᴜᴘᴅᴀᴛᴇ ˼", url="https://t.me/BABY09_WORLD"),
            ],
            [
                InlineKeyboardButton("˹ sᴜᴘᴘᴏʀᴛ ˼", url="https://t.me/aboutchinnalu"),
                InlineKeyboardButton("˹ ᴍᴜsɪᴄ ˼", url="https://t.me/BABY09_WORLD"),
            ],
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_photo(message.chat.id, ALIVE_PIC, caption=PHONE_NUMBER_TEXT, reply_markup=reply_markup)

@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("ᴜsᴀɢᴇ:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("sᴀᴛʏᴀ ᴘʀᴏᴄᴇssɪɴɢ.....✲")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="UTTAM/plugins"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f" 𝗝𝗔 𝗣𝗘𝗟 𝗗𝗘 𝗦𝗔𝗕𝗞𝗢 𝗔𝗕 Chinna 𝗞𝗢 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗞𝗘 𝗝𝗔𝗡𝗔 🥵 {user.first_name} 💨.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
