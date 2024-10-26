# bot/handlers/start.py
from aiogram import types, Dispatcher, Bot
from aiogram.filters import CommandStart
from aiogram.exceptions import TelegramBadRequest
from loguru import logger
from aiogram.utils.keyboard import InlineKeyboardBuilder  # Импорт InlineKeyboardBuilder
from bot.keyboards.reply_buttons import get_main_menu_buttons

# Функция для проверки подписки пользователя на канал
async def is_user_subscribed(user_id: int, bot: Bot, channel_id: str) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
        logger.info(f"Проверка подписки пользователя {user_id} на {channel_id}")
        logger.info(f"Статус пользователя {user_id} в {channel_id}: {member.status}")  # Логируем статус
        return member.status in ["member", "administrator", "creator"]
    except TelegramBadRequest as e:
        logger.warning(f"Ошибка при проверке подписки пользователя {user_id} на {channel_id}: {e}")
        return False


# Функция-обработчик команды /start
async def send_welcome(message: types.Message, bot: Bot):
    channel_id = '@aistudio4u'  # Канал
    group_id = '@AI_and_code'  # Группа

    logger.info(f"Получена команда /start от пользователя {message.from_user.id}")

    # Проверка подписки на канал и группу
    is_subscribed_channel = await is_user_subscribed(message.from_user.id, bot, channel_id)
    is_subscribed_group = await is_user_subscribed(message.from_user.id, bot, group_id)

    if not is_subscribed_channel or not is_subscribed_group:
        logger.info(f"Пользователь {message.from_user.id} не подписан на {channel_id} или {group_id}")

        # Использование InlineKeyboardBuilder для создания кнопок
        builder = InlineKeyboardBuilder()
        builder.add(
            types.InlineKeyboardButton(text="Подписаться на канал", url="https://t.me/aistudio4u")
        )
        builder.add(
            types.InlineKeyboardButton(text="Подписаться на группу", url="https://t.me/AI_and_code")
        )
        reply_markup = builder.as_markup()

        await message.answer(
            "Чтобы получать полные возможности бота, подпишитесь на канал и группу: "
            f"{channel_id} и {group_id}.",
            reply_markup=reply_markup
        )

    # Приветственное сообщение и меню, независимо от подписки
    logger.info(f"Пользователь {message.from_user.id} получил доступ к меню.")
    await message.answer(
        "Привет! Я ваш бот. Чем могу помочь?",
        reply_markup=get_main_menu_buttons()
    )

# Функция для регистрации обработчика команды /start
def register_start_handler(dp: Dispatcher):
    dp.message.register(send_welcome, CommandStart())
    logger.info("Обработчик команды /start зарегистрирован")
