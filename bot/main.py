import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove

# Load the token from environment variables or replace with your token.
API_TOKEN = os.getenv("TELEGRAM_API_TOKEN", "YOUR_API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Create a Router for organizing handlers
router = Router()

# Define a handler for the /start command
@router.message(CommandStart())
async def start_command(message: Message) -> None:
    await message.answer("Привет! Я ваш бот. Чем могу помочь?", reply_markup=ReplyKeyboardRemove())

# Define a handler for text messages
@router.message()
async def echo_message(message: Message) -> None:
    await message.answer(message.text)

# Register the router with the dispatcher
dp.include_router(router)

# Run the bot
async def main() -> None:
    logger.info("Starting bot...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
