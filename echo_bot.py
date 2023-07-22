import asyncio
import os

from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot

load_dotenv()

bot = AsyncTeleBot(os.getenv('TELEGRAM_TOKEN'))


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(
        message, "Hello!"
    )


@bot.message_handler(commands=['ping'])
async def send_welcome(message):
    await bot.reply_to(
        message, "Pong!"
    )


@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


asyncio.run(bot.polling())
