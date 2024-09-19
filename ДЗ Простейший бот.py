from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api =
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start']) #Хендлер для приема сообщений. работа с сообщениями бота по указанной команде \start.
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.' )


@dp.message_handler()     #Хендлер для приема сообщений. работа с сообщениями бота, перехватывает все что не перехвачены выше специфичными.
async def all_message(message):
    print("start, чтобы начать общение.")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)