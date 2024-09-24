from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text='Формула расчёта', callback_data='formulas')
button2 = InlineKeyboardButton(text='Рассчитать калории', callback_data='calories')
button3 = InlineKeyboardButton(text='Информация', callback_data='info')
kb.add(button1, button2, button3)


class UserStat(StatesGroup):
    age = State()
    weight = State()
    height = State()



@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Я Бот помогающий Вашему здоровою, чтобы продолжить общение напишите Рассчитать.')

@dp.message_handler(text='Рассчитать')
async def start(message):
    await message.answer('Приятно что вы посетили наш Бот, выберите операцию:', reply_markup=kb)

@dp.callback_query_handler(text='info')
async def inform(call):
    await call.message.answer('Соблюдайте норму калорий и ваше здоровье будет в норме! '
                              'Hажмите кнопку [Рассчитать калории], чтоб рассчитать вашу норму калорий!, '
                              'Нажмите кнопку [Формула расчёта] чтоб получить формулу расчета!', reply_markup=kb)
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def formula(call):
    await call.message.answer('normcalor = 10 * weight + 6.25 * height - 5 * age - 161', reply_markup=kb)
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст ')
    await UserStat.age.set()
    await call.answer()


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
        f" Вам {user_data['age']} год, Ваш рост {user_data['height']} см и весишь ты {user_data['weight']} кг, твоя норма калорий - {normcalor} кк ")
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
