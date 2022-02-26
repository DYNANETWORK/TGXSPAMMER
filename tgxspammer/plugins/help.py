from tgxspammer import Mam, Mam2, Mam3, Mam4, Mam5, Mam6, Mam7, Mam8, Mam9, Mam10, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from tgxspammer import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/2526a514b8ccd7b7cc380.jpg"

Mam_Help = "__Click On Below Buttons for help__"


@Mam.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mam2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mam3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mam4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mam5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mam6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mam7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mam8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mam9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mam10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Mam_Help,
                                  buttons=[
           [
            Button.inline("• Spam •", data="spam"),
            Button.inline("• Raid •", data="raid"),
           ],
           [
            Button.inline("• Extra •", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/MAMBA_NETWORK")
           ],
           ],
           )              

  
  
extra_msg = f"""
**Help Extra Cmds**
**Userbot**: Userbot Cmds
command:
i) {hl}ping 
ii) {hl}alive
iii) {hl}restart
iv) {hl}addsudo <reply to user> : Owner Cmd
**Echo**: To Active Echo On Any User
command:
i) {hl}addecho <reply to user>
ii) {hl}rmechk <reply to user>
**Leave**: To Leave Group/channel
command:
i) {hl}leave <group/chat id>
ii) {hl}leave : Type in the Group bot will auto leave that group
**Packspam**: Sticker Pack Spam
i) {hl}packspam (replying to any sticker)
**© @MAMBA_NETWORK**
"""

                 
raid_msg = f"""
**Help Raid Cmds**
**raid:** Activates raid on any individual user for given range.
command:
i) {hl}raid <count> <username
ii) {hl}raid <count> <reply to user>
**Delayraid**: Activates raid on any individual user for given range.
Command:
i) {hl}delayraid <delay> <count> <Username of User>
ii) {hl}delayraid <delay> <count> <reply to a User>
**replyraid:** Activates Reply Raid on the user!!
command:
i) {hl}replyraid <replying to user>
ii) {hl}dreplyraid <username>
**dreplyraid:** Deactivates reply raid on the user!!
command:
i) {hl}dreplyraid <replying to user>
ii) {hl}dreplyraid <username>
**© @MAMBA_NETWORK**
"""

spam_msg = f"""
**Help Spam Cmds**
**spam**: Spams a message for given counter(<= 100).
command:
i) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}spam <count> <replying any message>
**bigspam**: Spams a message for given counter.
command:
i) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}bigspam <count> <replying any message>
**delayspam**: Delay spam a text for given counter after given time.
command:
i) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}delayspam <delay> <count> <replying any message>
**pornspam**: Pornography Spam.
command:
i) {hl}pornspam <count>
**hang**: Spams hanging message for given counter.
command:
i) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)
** © @MAMBA_NETWORK**
"""                     
           
           
@Mam.on(events.CallbackQuery(pattern=r"help_back"))
@Mam2.on(events.CallbackQuery(pattern=r"help_back"))
@Mam3.on(events.CallbackQuery(pattern=r"help_back"))
@Mam4.on(events.CallbackQuery(pattern=r"help_back"))
@Mam5.on(events.CallbackQuery(pattern=r"help_back"))
@Mam6.on(events.CallbackQuery(pattern=r"help_back"))
@Mam7.on(events.CallbackQuery(pattern=r"help_back"))
@Mam8.on(events.CallbackQuery(pattern=r"help_back"))
@Mam9.on(events.CallbackQuery(pattern=r"help_back"))
@Mam10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            Riz_Help,
            buttons=[
                [
            Button.inline("Spam", data="spam"),
            Button.inline("Raid", data="raid"),
           ],
           [
            Button.inline("Extra cmds", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/MAMBA_NETWORK")
           ],
           ],
        )           
   else:
        Alert = (
                "Noob !! Make Your Own TGX Spam Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@Mam.on(events.CallbackQuery(pattern=r"spam"))
@Mam2.on(events.CallbackQuery(pattern=r"spam"))
@Mam3.on(events.CallbackQuery(pattern=r"spam"))
@Mam4.on(events.CallbackQuery(pattern=r"spam"))
@Mam5.on(events.CallbackQuery(pattern=r"spam"))
@Mam6.on(events.CallbackQuery(pattern=r"spam"))
@Mam7.on(events.CallbackQuery(pattern=r"spam"))
@Mam8.on(events.CallbackQuery(pattern=r"spam"))
@Mam9.on(events.CallbackQuery(pattern=r"spam"))
@Mam10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "Noob !! Make Your Own TGX Spam Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@Mam.on(events.CallbackQuery(pattern=r"raid"))
@Mam2.on(events.CallbackQuery(pattern=r"raid"))
@Mam3.on(events.CallbackQuery(pattern=r"raid"))
@Mam4.on(events.CallbackQuery(pattern=r"raid"))
@Mam5.on(events.CallbackQuery(pattern=r"raid"))
@Mam6.on(events.CallbackQuery(pattern=r"raid"))
@Mam7.on(events.CallbackQuery(pattern=r"raid"))
@Mam8.on(events.CallbackQuery(pattern=r"raid"))
@Mam9.on(events.CallbackQuery(pattern=r"raid"))
@Mam10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "Noob !! Make Your Own TGX Spam Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@Mam.on(events.CallbackQuery(pattern=r"extra"))
@Mam2.on(events.CallbackQuery(pattern=r"extra"))
@Mam3.on(events.CallbackQuery(pattern=r"extra"))
@Mam4.on(events.CallbackQuery(pattern=r"extra"))
@Mam5.on(events.CallbackQuery(pattern=r"extra"))
@Mam6.on(events.CallbackQuery(pattern=r"extra"))
@Mam7.on(events.CallbackQuery(pattern=r"extra"))
@Mam8.on(events.CallbackQuery(pattern=r"extra"))
@Mam9.on(events.CallbackQuery(pattern=r"extra"))
@Mam10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "Noob !! Make Your Own TGX Spam Bots !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
