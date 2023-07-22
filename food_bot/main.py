import asyncio
import os

from dotenv import load_dotenv
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

from option_manager import OptionManager, NoOptionsInData

load_dotenv()

bot = AsyncTeleBot(os.getenv('TELEGRAM_TOKEN'))
option_manager = OptionManager()


@bot.message_handler(commands=['add'])
async def add_food(message: Message):
    try:
        food = message.text.split(' ', 1)[1]
    except IndexError:
        await bot.reply_to(message, "Please specify food to add!")
        return

    option_manager.add(message.from_user.id, food)

    await bot.reply_to(message, f"Added {food} to your food list!")


@bot.message_handler(commands=['list'])
async def list_food(message: Message):
    food_list = option_manager.list(message.from_user.id)

    if not food_list:
        await bot.reply_to(message, "Your food list is empty!")
        return

    await bot.reply_to(message, "\n".join([f"{i + 1}. {food}" for i, food in enumerate(food_list)]))


@bot.message_handler(commands=['eat'])
async def eat_food(message: Message):
    try:
        food = option_manager.eat(message.from_user.id)
        await bot.reply_to(message, f"Today you will eat {food}!")
    except NoOptionsInData:
        await bot.reply_to(message, "Your food list is empty!")


@bot.message_handler(commands=['remove'])
async def remove_food(message: Message):
    try:
        index = int(message.text.split(' ', 1)[1]) - 1
    except (IndexError, ValueError):
        await bot.reply_to(message, "Please specify index of food to remove!")
        return

    try:
        option_manager.remove(message.from_user.id, index)
        await bot.reply_to(message, f"Removed food at index {index + 1}!")
    except IndexError:
        await bot.reply_to(message, f"Index {index + 1} is out of range!")


@bot.message_handler(commands=['clear'])
async def clear_food(message: Message):
    option_manager.clear(message.from_user.id)
    await bot.reply_to(message, "Cleared your food list!")


asyncio.run(bot.polling())
