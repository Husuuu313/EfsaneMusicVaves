from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as BN
from helpers.filters import command, other_filters2


@Client.on_message(command(["start", f"start"]))
async def start(_, message: Message):
    await message.reply_photo("https://i.ibb.co/khRz42f/Turkish-Voice.jpg")
    await message.reply_text(
        f"""**Salam, {message.from_user.mention} 🎵
Sesli sohbetlerde musiqi çalabilen botam. Yetki verin , Asistantımı qrupa elave edin.\n\Hazırladı [DBMBOSSdu 🎙️](https://t.me/DBMBOSSdu).
 **""",

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Qrupunuza elave et ➕", url="https://t.me/Efsanestar_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistant", url="https://t.me/DBMmusicasistant" 
                    ),
                    InlineKeyboardButton(
                        "💬 Sohbet", url="https://t.me/DBMsohbet"
                    ),
                    InlineKeyboardButton(
                        "🇦🇿 Sahibim", url="https://t.me/DBMBOSSdu") 
                ],
                [
                    InlineKeyboardButton(
                        "🧩 Github", url="https://github.com/DBMBOSSdu313/EfsaneMusicVaves"
                    )
                ]
            ]
        ), 
     disable_web_page_preview=True
   ) 

@Client.on_message(command(["bilgi"])) 
async def bilgi(_, message: Message):
      await message.reply_text(f"**Salam {message.from_user.mention}!\n Bu botun kömek menyusu 📚\n\n ▶️ /play - mahnı oxumaq üçün youtube url'sine veya mahnı faylına yanıt verme\n ▶️ /play <song name> - istediyiniz mahnını oxudar\n 🔴 /ytplay <Sorgu> - youtube üzerinden oxuyar\n 🎵 /bul <song name> - istediyiniz mahnıları celd bir şekilde axtarın\n 🎵 /vbul istediyiniz videoları tez bir şekilde axtarın\n 🔍 /ara <query> - youtube'da ayrıntılardan behs eden videoları axtarma\n\n Yalnız adminler üçün..\n ⏩ /resume - mahnı oxumağı davam et\n ⏹ /end - musiqini dayandırar\n 🔼 /ver botun sadece admin istifade ede biler , olan komandalarını istifade ede bilmesi üçün user'e yetki ver\n 🔽 /al botun admin komandalarını istifade ede bilen userin yetkisini al\n 🎚 /ses asistant hesabın ses seviyesini kontrol ele\n\n ⚪ /gir - Musiqi asistantı qrupunuza girer\n ⚫ /çıx - Musiqi asistantı qrupunuzu terk eder.**", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "👨‍🔧 Sahibim", url="https://t.me/DBMBOSSdu")
                 ]
             ]
         )
    )
