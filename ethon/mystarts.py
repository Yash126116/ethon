#ignore this file

from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.inline("🤖 Update Channel", url="t.me/vj_botz"),
                               Button.url("💢 Support Group", url="t.me/vj_bot_disscussion")],
                              [Button.url("❣️ Developer", url="t.me/Kingvj01")]])
                              
    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR v1.4**", 
                    buttons=[
                        [Button.inline("info.", data="info"),
                         Button.inline("SOURCE", data="source")],
                        [Button.inline("NOTICE.", data="notice"),
                         Button.inline("Main.", data="help")],
                        [Button.url("DEVELOPER", url="t.me/Kingvj01")]])
    
