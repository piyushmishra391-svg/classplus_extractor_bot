import os
from pyrogram import Client, filters
from pyrogram.types import Message

bot = Client(
    'classplus_bot',
    api_id=int(os.getenv('30424326')),
    api_hash=os.getenv('eb823f3b2a0e6b7af29ac42efe701129'),
    bot_token=os.getenv('8762678534:AAEhShFlS5vPenLLYj4MzvgDuZawaKIlT68')
)

@bot.on_message(filters.command('start'))
async def start_cmd(client, message: Message):
    await message.reply_text('👋 Welcome to Classplus Extractor Bot!')

# You would include /drm, /batch, /txt handlers here

bot.run()
