# bot/keyboards/reply_buttons.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu_buttons():
    # Создаем клавиатуру с основными командами для быстрого доступа
    menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_keyboard.add(
        KeyboardButton(text="/catalog"),
        KeyboardButton(text="/cart"),
        KeyboardButton(text="/faq")
    )
    return menu_keyboard
