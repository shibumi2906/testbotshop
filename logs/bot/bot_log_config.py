# main.py
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os
from logs.bot.bot_log_config import logger  # Импортируем логгер

# Загрузите токен из переменных окружения или замените на ваш токен.
API_TOKEN = os.getenv("TELEGRAM_API_TOKEN", "YOUR_API_TOKEN")

# Инициализация бота и диспетчера.
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Логируем запуск бота.
logger.info("Bot is starting...")

# Обработчик команды /start.
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    logger.info(f"User {message.from_user.id} used /start command")
    await message.reply("Привет! Я ваш бот. Чем могу помочь?")

# Обработчик текстовых сообщений.
@dp.message_handler()
async def echo(message: types.Message):
    logger.info(f"Received message from {message.from_user.id}: {message.text}")
    await message.reply(message.text)

# Запуск бота.
if __name__ == "__main__":
    try:
        logger.info("Starting bot polling...")
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
