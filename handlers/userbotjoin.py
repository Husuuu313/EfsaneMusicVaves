from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["gir", "asistan"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Meni Evvelce Admin etmelisiz</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "Sesmusic Asistan"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"Yene geldim bura :D")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Asistant qrupda var</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Xeta 🛑 \n User {user.first_name} userbot üçün toplu qatılma istekleri sebebiyle qrupunuza qatılmadı! Asistantın qrupta banlı olmadığından emin olun."
            "\n\n Yada @DBMmusicasistant Hesabını Qruba Özün Elave et </b>",
        )
        return
    await message.reply_text(
            "<b>Asistant Qrupdadı</b>",
        )
    
@USER.on_message(filters.group & filters.command(["çıx", "asistanby"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Bot qrupunuzdan çıxmadı!."
            "\n\nYada Özün çıxart</b>",
        )
        return
 
 
 
