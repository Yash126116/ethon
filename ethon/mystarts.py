#ignore this file

from telethon import events, Button
from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton

async def start_srb(event, st):
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🤖 Update Channel", url="https://t.me/vj_botz"),
                InlineKeyboardButton("💢 Support Group", url="https://t.me/vj_bot_disscussion")
            ],
            [
                InlineKeyboardButton("❣️ Developer", url="https://t.me/Kingvj01")
            ]
        ]
    )
    
    await event.send_message(st, reply_markup=reply_markup)
    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR v1.4**", 
                    buttons=[
                        [Button.inline("info.", data="info"),
                         Button.inline("SOURCE", data="source")],
                        [Button.inline("NOTICE.", data="notice"),
                         Button.inline("Main.", data="help")],
                        [Button.url("DEVELOPER", url="t.me/Kingvj01")]])
    
