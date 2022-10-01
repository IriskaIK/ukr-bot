from aiogram import executor, Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import handlers

from aiogram.utils.executor import start_webhook
import logging
import os

BOT_TOKEN = "5704103888:AAGmgdQK_E8UalwkF7N501kCUcuHiN1O7lA"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

WEBHOOK_HOST = f'https://mighty-woodland-33435..herokuapp.com'
WEBHOOK_PATH = f'/webhook/5704103888:AAGmgdQK_E8UalwkF7N501kCUcuHiN1O7lA'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default=8000)
async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await bot.delete_webhook()
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
