from pyrogram import Client , filters
from pyrogram.enums import ChatMemberStatus

PyroHub = Client("PyroHub - Pyrogram",
api_id=15960485,
api_hash="9af079bc321e3fc9ceb500e860754f09",
bot_token="6121776236:AAHGtinmMAj_z5WX5s4UuJA2X1eeFgieRr0")
iB =6121776236

@PyroHub.on_message(filters.regex("تفليش") & filters.group)
async def ban_all(_, m):   
    Gchat = await PyroHub.get_chat_member(m.chat.id,iB)
    
    if Gchat.privileges.can_restrict_members==True:
        async for member in PyroHub.get_chat_members(m.chat.id):
            try:
                Gmember = await PyroHub.get_chat_member(m.chat.id,member.user.id)
                stas = (await PyroHub.get_chat_member(m.chat.id, m.from_user.id)).status
                auth = [ChatMemberStatus.OWNER, ChatMemberStatus.OWNER]
                if stas in auth: 
                 await PyroHub.ban_chat_member(m.chat.id,Gmember.user.id)
                await m.reply_text("- تم التفليش .")
            except Exception as e:
                print(e)
    else:
        await m.reply_text("- لا املك صلاحية حظر المستخدمين .")
        
print ("- Done Upload Telegram Bot .\n- Can You Used Bot Now!")
PyroHub.run()