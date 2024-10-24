# bot/handlers/faq.py
from aiogram import types, Dispatcher

async def show_faq(message: types.Message):
    # Здесь будет логика отображения часто задаваемых вопросов.
    await message.reply("Часто задаваемые вопросы:\n1. Как сделать заказ?\n2. Как связаться с поддержкой?")

def register_faq_handler(dp: Dispatcher):
    dp.register_message_handler(show_faq, commands=['faq'])
