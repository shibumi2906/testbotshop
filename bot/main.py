import asyncio
from loguru import logger
import os
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove
from dotenv import load_dotenv
from bot.handlers.start import register_start_handler

# Загрузка переменных окружения из файла .env
load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

# Проверка, что токен был загружен
if not API_TOKEN:
    logger.error("TELEGRAM_API_TOKEN не найден. Проверьте файл .env.")
    raise ValueError("TELEGRAM_API_TOKEN не найден. Проверьте файл .env.")

# Настройка логирования Loguru
logger.add("bot_log.log", format="{time} {level} {message}", level="INFO")

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Регистрация обработчиков
register_start_handler(dp)

# Основная функция запуска бота
async def main() -> None:
    logger.info("Запуск бота...")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.exception(f"Ошибка при запуске бота: {e}")

# Запуск бота
if __name__ == "__main__":
    logger.info("Инициализация...")
    asyncio.run(main())

