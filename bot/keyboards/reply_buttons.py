# bot/keyboards/reply_buttons.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu_buttons():
    # Создаем клавиатуру с основными командами для быстрого доступа с визуальным эффектом кнопок
    menu_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔵 /catalog 🔵")],
            [KeyboardButton(text="🔵 /cart 🔵")],
            [KeyboardButton(text="🔵 /faq 🔵")]
        ],
        resize_keyboard=True
    )
    return menu_keyboard
