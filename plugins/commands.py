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
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import psutil
import time
from os import environ, execle, system

START_TIME = time.time()

# Define your required channel IDs (use the chat ID for private channels, used in the format -100...)
FORCE_CHANNELS = [-1001764441595, -1002135593873]  # Replace these with your actual channel IDs

main_buttons = [[
    InlineKeyboardButton('❣️ ᴅᴇᴠᴇʟᴏᴘᴇʀ ❣️', url='https://t.me/kingvj01')
],[
    InlineKeyboardButton('🔍 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/vj_bot_disscussion'),
    InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/vj_botz')
],[
    InlineKeyboardButton('💝 sᴜʙsᴄʀɪʙᴇ ᴍʏ ʏᴏᴜᴛᴜʙᴇ ᴄʜᴀɴɴᴇʟ', url='https://youtube.com/@Tech_VJ')
],[
    InlineKeyboardButton('👨‍💻 ʜᴇʟᴘ', callback_data='help'),
    InlineKeyboardButton('💁 ᴀʙᴏᴜᴛ', callback_data='about')
],[
    InlineKeyboardButton('⚙ sᴇᴛᴛɪɴɢs', callback_data='settings#main')
]]

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    user = message.from_user

    # Check if the user is a member of the specified channels
    for channel in FORCE_CHANNELS:
        try:
            chat_member = await client.get_chat_member(channel, user.id)
            print(f"Checked membership for {user.id} in {channel}: {chat_member.status}")  # Debugging statement
            
            # Check if the user is either a member or an admin
            if chat_member.status not in ["member", "administrator", "creator"]:
                await message.reply_text(
                    text=f"Please join our channel: Channel Link",
                    disable_web_page_preview=True
                )
                return
        except Exception as e:
            # Specific error handling to understand what's going wrong
            print(f"Error checking membership for user {user.id} in {channel}: {e}")  # Debugging statement
            await message.reply_text(
                text=f"Unable to check your membership status in the channel. Please join and try again.\nChannel Link",
                disable_web_page_preview=True
            )
            return
    
    # Add user to database if they do not exist
    if not await db.is_user_exist(user.id):
        await db.add_user(user.id, user.first_name)
    
    reply_markup = InlineKeyboardMarkup(main_buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Script.START_TXT.format(user.first_name)
    )

# Implement other handlers as needed...
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

# Your existing callback query handlers go here...
