import os
import asyncio
from telegram import Bot

BOT_TOKEN = os.getenv("8016462484:AAGSm9Aw73VrvC3BGnVC_XX60evEMuUJ2-U")
CHANNEL = os.getenv("@ai_ds_job_updates")

async def send_message(text):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHANNEL, text=text)

def notify(text):
    asyncio.run(send_message(text))
