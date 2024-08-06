from AnonXMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

@app.on_message(filters.command(["mention", "utag", "all"]) & filters.group)
async def tag_all_users(_,message): 
    replied = message.reply_to_message  
    if len(message.command) < 2 and not replied:
        await message.reply_text("**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ**") 
        return                  
    if replied:
        SPAM_CHATS.append(message.chat.id)      
        usernum= 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id): 
            if message.chat.id not in SPAM_CHATS:
                break       
            usernum += 3
            usertxt += f"\n⚘ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 1:
                await replied.reply_text(usertxt)
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try :
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        text = message.text.split(None, 1)[1]

        SPAM_CHATS.append(message.chat.id)
        usernum= 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):       
            if message.chat.id not in SPAM_CHATS:
                break 
            usernum += 1
            usertxt += f"\n⚘ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 3:
                await app.send_message(message.chat.id,f'{text}\n{usertxt}')
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""                          
        try :
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass        

@app.on_message(filters.command(["mantionoff", "tagstop", "cancel", "stop"]))
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try :
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass   
        return await message.reply_text("**ᴛᴀɢ ᴀʟʟ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")     

    else :
        await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")  
        return       

__MODULE__ = "Tᴀɢ Aʟʟ"
__HELP__ = """
**Tᴀɢ A Usᴇʀs**

Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀᴏᴡs ᴀᴅᴍɪɴs ᴛᴏ ᴛᴀɢ ᴀ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇ.

Cᴏᴍᴍᴀɴᴅs:
- /ᴀ <ᴛᴇxᴛ>: Tᴀɢ ᴀ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇ ᴡɪᴛʜ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴇxᴛ.
- /ᴍᴇɴᴛɪᴏɴ <ᴛᴇxᴛ>: Tᴀɢ ᴀ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇ ᴡɪᴛʜ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴇxᴛ.
- /ᴍᴇɴᴛɪᴏɴᴀ <ᴛᴇxᴛ>: Tᴀɢ ᴀ ᴜsᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴏʀ ᴄʜᴀɴɴᴇ ᴡɪᴛʜ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴇxᴛ.

Tᴏ sᴛᴏᴘ ᴛᴀɢɢɪɴɢ:
- /sᴛᴏᴘᴍᴇɴᴛɪᴏɴ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴏғғᴀ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴄᴀɴᴄᴇ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴀsᴛᴏᴘ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /sᴛᴏᴘᴀ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴄᴀɴᴄᴇᴍᴇɴᴛɪᴏɴ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴏғғᴍᴇɴᴛɪᴏɴ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴍᴇɴᴛɪᴏɴᴏғғ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴀᴏғғ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴄᴀɴᴄᴇᴀ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.
- /ᴀᴄᴀɴᴄᴇ: Sᴛᴏᴘ ᴛʜᴇ ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss.

Nᴏᴛᴇ: Oɴʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs.
"""
