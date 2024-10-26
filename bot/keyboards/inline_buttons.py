# bot/keyboards/inline_buttons.py
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_catalog_buttons():
    # Создаем инлайн-клавиатуру для каталога с визуальным эффектом кнопок
    catalog_keyboard = InlineKeyboardMarkup(row_width=2)
    catalog_keyboard.add(
        InlineKeyboardButton(text="🔹 Категория 1 🔹", callback_data="category_1"),
        InlineKeyboardButton(text="🔹 Категория 2 🔹", callback_data="category_2"),
        InlineKeyboardButton(text="🔹 Категория 3 🔹", callback_data="category_3")
    )
    return catalog_keyboard

def get_cart_buttons():
    # Создаем инлайн-клавиатуру для корзины с визуальным эффектом кнопок
    cart_keyboard = InlineKeyboardMarkup(row_width=2)
    cart_keyboard.add(
        InlineKeyboardButton(text="🔹 Просмотреть корзину 🔹", callback_data="view_cart"),
        InlineKeyboardButton(text="🔹 Очистить корзину 🔹", callback_data="clear_cart"),
        InlineKeyboardButton(text="🔹 Оформить заказ 🔹", callback_data="checkout")
    )
    return cart_keyboard
