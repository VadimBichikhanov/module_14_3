from aiogram import Bot, Dispatcher
import logging
import asyncio
from os import getenv
from handlers import register_handlers

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Получение токена бота из переменных окружения
API_TOKEN = getenv('TELEGRAM_TOKEN')
if not API_TOKEN:
    logging.error("TELEGRAM_TOKEN не найден в переменных окружения")
    exit(1)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Регистрация обработчиков
register_handlers(dp)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())