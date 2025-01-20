# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import sys
import asyncio 
from database import Db, db
from config import Config, temp
from script import Script
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaDocument
import psutil
import time as time
from os import environ, execle, system
START_TIME = time.time()
main_buttons = [[
    InlineKeyboardButton('update ᴄʜᴀɴɴᴇʟ', url='t.me/ROCKERSBACKUP')
],[
    InlineKeyboardButton('👨‍💻 ʜᴇʟᴘ', callback_data='help'),
    InlineKeyboardButton('💁 ᴀʙᴏᴜᴛ', callback_data='about')
],[
    InlineKeyboardButton('⚙ sᴇᴛᴛɪɴɢs', callback_data='settings#main')
]]
FORCE_CHANNELS = [-1001764441595, -1002135593873]  # Replace these with your channel IDs
@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    user = message.from_user
    
    # Check if the user is a member of the specified channels
    for channel in FORCE_CHANNELS:
        try:
            chat_member = await client.get_chat_member(channel, user.id)
            if chat_member.status not in ["member", "administrator", "creator"]:
                await message.reply_text(
                    text=f"Please join our channel: Channel Link",
                    disable_web_page_preview=True
                )
                return
        except Exception as e:
            await message.reply_text("I couldn't check your subscription status. Please try again later.")
            return
    
    # Add user to database if they do not exist
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id, user.first_name)
    
    reply_markup = InlineKeyboardMarkup(main_buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Script.START_TXT.format(message.from_user.first_name)
    )
# Other handlers remain unchanged...
@Client.on_message(filters.private & filters.command(['restart']) & filters.user(Config.BOT_OWNER))
async def restart(client, message):
    msg = await message.reply_text(text="<i>Trying to restarting.....</i>")
    await asyncio.sleep(5)
    await msg.edit("<i>Server restarted successfully ✅</i>")
    system("git pull -f && pip3 install --no-cache-dir -r requirements.txt")
    execle(sys.executable, sys.executable, "main.py", environ)
# Rest of your callback query handlers…
async def get_bot_uptime(start_time):
    uptime_seconds = int(time.time() - start_time)
    uptime_minutes = uptime_seconds // 60
    uptime_hours = uptime_minutes // 60
    uptime_days = uptime_hours // 24
    uptime_weeks = uptime_days // 7
    uptime_string = ""
    if uptime_hours != 0:
        uptime_string += f" {uptime_hours % 24}H"
    if uptime_minutes != 0:
        uptime_string += f" {uptime_minutes % 60}M"
    uptime_string += f" {uptime_seconds % 60} Sec"
    return uptime_string
# Add the rest of your existing code...  

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
