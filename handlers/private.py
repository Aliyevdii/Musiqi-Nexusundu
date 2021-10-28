from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USARNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2


@Client.on_message(command(["start", f"start@{BOT_USARNAME}"]))
async def start(_, message: Message):
    await message.reply_photo("https://i.ibb.co/MpdcXYM/IMG-20211023-135851-221.jpg")
    await message.reply_text(
        f"""**Merhaba, {message.from_user.mention} 🎵
Ben {bot}! Sesli sohbetlerde müzik çalabilen botum. Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.**""",

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏷️ Destek Grubu", url="https://t.me/SohbetOdagi"
                    ),
                    InlineKeyboardButton(
                        "🔧 Geliştirici", url = "https://t.me/Bir_Beyfendi"
                    )
                  ],[
                    InlineKeyboardButton(
                        "🛠 Kurucu" , url = "https://t.me/Mahoaga"
                    ),
                    InlineKeyboardButton(
                        "🔊 Asistan" , url = "https://t.me/HerTeldenAsistan"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🌀 Komutlar" , url = "https://telegra.ph/Komutlar-10-22"
                    ),
                    InlineKeyboardButton(
                        "🎮 Oyun Botu", url="https://t.me/BasitOyunBot"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command(["reload", f"reload@{BOT_USARNAME}"]) & ~filters.private & ~filters.channel)
async def reload(_, message: Message):
      await message.reply_text("""**Yeniden başlatıldı. Bot çalışıyor ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙ Geliştirici", url="https://t.me/Bir_Beyfendi")
                ]
            ]
        )
   )

@Client.on_message(filters.command(["help", f"help@{BOT_USARNAME}"]) & ~filters.private & ~filters.channel)
async def help(_, message: Message):
      await message.reply_text("""**Selam {message.from_user.mention}!\n Bu botun yardım menüsü 🤩\n\n ▶️ /oynat - şarkı çalmak için youtube url'sine veya şarkı dosyasına yanıt verme\n ▶️ /oynat <song name> - istediğiniz şarkıyı çal\n 🔴 /ytp <Sorgu> - youtube üzerinden çalma\n 🎵 /sarki <song name> - istediğiniz şarkıları hızlı bir şekilde indirin\n 🔍 /ara <query> - youtube'da ayrıntıları içeren videoları arama\n\n Yalnızca yöneticiler için..\n ▶️ /devam - şarkı çalmaya devam et\n ⏹ /bitir - müzik çalmayı durdurma\n\n ⚪ /katil - Müzik asistanı grubunuza katılır\n ⚫ /ayril - Müzik asistanı grubunuzu terk eder.**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙ Geliştirici", url="https://t.me/Bir_Beyfendi")
                ]
            ]
        )
   )
