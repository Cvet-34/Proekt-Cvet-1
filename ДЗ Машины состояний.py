from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['Привет'])
async def urban_message(message):
    await message.answer("Введите команду: /start чтобы начать общение!")


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('привет я бот помогающий твоему здоровью, напиши слово Calories')


class UserStat(StatesGroup):
    age = State()
    weight = State()
    height = State()
    calories = State()


@dp.message_handler(text=['Calories'])
async def set_age(message):
    await message.answer('Введите свой возраст ')
    await UserStat.age.set()


@dp.message_handler(state=UserStat.age)
async def set_weight(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой вес ')
    await UserStat.weight.set()


@dp.message_handler(state=UserStat.weight)
async def set_height(message, state):
    await state.update_data(weight=message.text)
    await message.answer('Введите свой рост ')
    await UserStat.height.set()


@dp.message_handler(state=UserStat.height)
async def process_weight(message, state):
    await state.update_data(height=message.text)
    user_data = await state.get_data()
    age = int(user_data['age'])
    height = int(user_data['height'])
    weight = int(user_data['weight'])
    normcalor = 10 * weight + 6.25 * height - 5 * age - 161
    await message.answer(
        f" Вам {user_data['age']} год, Ваш рост {user_data['height']} см и весишь ты {user_data['weight']} кг, твоя норма колорий - {normcalor} кк ")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
