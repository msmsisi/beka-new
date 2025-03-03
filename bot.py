# bot.py
import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router
from aiogram.fsm.storage.memory import MemoryStorage
from db import create_db, add_country_and_cities, create_tariffs_table, add_tariffs  # Импортируем новые функции

async def main():
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)

    # Объект бота
    bot = Bot(token=BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Создаем БД и заполняем ее данными
    create_db()
    add_country_and_cities()
    create_tariffs_table()  # Добавили вызов функции создания таблицы тарифов
    add_tariffs()  # Добавили вызов функции добавления тарифов

    # Подключаем роутеры
    dp.include_router(router)

    # Запуск поллинга
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Ошибка во время работы бота: {e}")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Бот остановлен")
