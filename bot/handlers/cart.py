# bot/handlers/cart.py
from aiogram import types, Dispatcher
from bot.keyboards.inline_buttons import get_cart_buttons

async def show_cart(message: types.Message):
    # Отображение содержимого корзины с инлайн-кнопками.
    await message.reply("Ваши действия с корзиной:", reply_markup=get_cart_buttons())

def register_cart_handler(dp: Dispatcher):
    dp.register_message_handler(show_cart, commands=['cart'])

