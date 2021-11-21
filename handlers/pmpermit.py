from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Salam, Bu musiqi asistant botudur.\n\n ❗️ Qaydalar:\n - Sohbet etmeyin.\n - İstifade etmek üçün qrupa ve yaxud kanala daxil et **/bilgi** yazsan. komandalarımı öyrene bilersen. \n - Fayl'a atmaq olmaz \n\n 🚨 **USERBOT QRUPUNUZA GİRMESE QRUP DEVETI BAĞLANTISI VEYA USER ADI GÖNDER.**\n\n ⚠️ DİQQET: Burada bir mesaj gönderseniz Admin göre biler ve sohbete qatılın\n - Bu botu gizli qruplara elave etmeyin.\n   - Özel melumatları burda paylaşmayın. 📚 Kömek üçün @DBMBOSSdu\n\n")
  return                      
