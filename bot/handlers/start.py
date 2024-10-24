# bot/handlers/start.py
from aiogram import types, Dispatcher
from bot.keyboards.reply_buttons import get_main_menu_buttons

async def send_welcome(message: types.Message):
    # Приветственное сообщение с кнопками главного меню.
    await message.reply("Привет! Я ваш бот. Чем могу помочь?", reply_markup=get_main_menu_buttons())

def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])

