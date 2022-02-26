import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Mam, Mam2, Mam3, Mam4, Mam5, Mam6, Mam7, Mam8, Mam9, Mam10, ALIVE_PIC, OWNER_ID
from tgxspammer.plugins.help import *


MAM_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/2526a514b8ccd7b7cc380.jpg"

Mam_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/MAMBA_NETWORK")
        ],
        [
        Button.inline("• ᴄᴍᴅs •", data="help_back")
        ]
        ]
               
MamX_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/MAMBA_NETWORK"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/MAMBA_X_SUPPORT")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/SUKHPAL443/TGXSPAMMER")
        ]
        ]
        
        
#USERS 


@Mam.on(events.NewMessage(pattern="/start"))
@Mam2.on(events.NewMessage(pattern="/start"))
@Mam3.on(events.NewMessage(pattern="/start"))
@Mam4.on(events.NewMessage(pattern="/start"))
@Mam5.on(events.NewMessage(pattern="/start"))
@Mam6.on(events.NewMessage(pattern="/start"))
@Mam7.on(events.NewMessage(pattern="/start"))
@Mam7.on(events.NewMessage(pattern="/start"))
@Mam8.on(events.NewMessage(pattern="/start"))
@Mam9.on(events.NewMessage(pattern="/start"))
@Mam10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       MamBot = await event.client.get_me()
       bot_id = MamBot.first_name
       bot_username = MamBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheMamba = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its me {bot_id}, Your Spam Bot !! \n\n Click Below Buttons For help**"
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [𝐓𝐆𝐗 𝐒𝐏𝐀𝐌𝐌𝐄𝐑](https://t.me/MAMBA_NETWORK)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheMamba,
                  MAM_IMG,
                  caption=ownermsg, 
                  buttons=Mam_Button)
       else:
            await event.client.send_file(TheMamba,
                  MAM_IMG,
                  caption=usermsg, 
                  buttons=MamX_Button)
