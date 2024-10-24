# bot/handlers/catalog.py
from aiogram import types, Dispatcher
from bot.keyboards.inline_buttons import get_catalog_buttons

async def show_catalog(message: types.Message):
    # Отображение каталога товаров с инлайн-кнопками.
    await message.reply("Выберите категорию:", reply_markup=get_catalog_buttons())

def register_catalog_handler(dp: Dispatcher):
    dp.register_message_handler(show_catalog, commands=['catalog'])

