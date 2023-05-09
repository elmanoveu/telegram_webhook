
import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import logging

import yaml

with open("config.yaml","r") as f:
    config = yaml.safe_load(f)

bot = Bot(token=config['token'])
dp = Dispatcher(bot)

# Configure logging
logging.basicConfig(level=logging.INFO)
logging.info("Telegram bot is running...")

@dp.message_handler(commands=['start'])
async def echo_message(msg:types.Message):
    await msg.reply(text="[START]")

@dp.message_handler(commands=['help'])
async def echo_message(msg:types.Message):
    await msg.reply(text="[HELP] чем я могу вам помочь")


if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)

