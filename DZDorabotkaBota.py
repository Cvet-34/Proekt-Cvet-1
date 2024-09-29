import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

from configd import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Магазин'),
            KeyboardButton(text='О нас')
        ]
    ], resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Хлеб свежий", callback_data="hleb")],
        [InlineKeyboardButton(text="Рыба свежая", callback_data="riba")],
        [InlineKeyboardButton(text="Сыр Российский", callback_data="siir")],
        [InlineKeyboardButton(text="Яблоки свежий урожай", callback_data="yabloki")]
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Купить!', callback_data="kypit")],
        [InlineKeyboardButton(text='В каталог', callback_data="back_to_catalog")]
    ]
)

priseHleb = 45
priseSiir = 300
priseYabloki = 120
priseRiba = 400


@dp.message_handler(commands=['start']) # Приветствие
async def start(message):
    await message.answer(f"Добро пожаловать, уважаемый покупатель! Я, бот помогаю сделать покупки, выберте оперцию:",
                         reply_markup=start_kb)


@dp.message_handler(text='О нас') # информация о магазине с фото.
async def prise(message):
    with open("magonlain.png", "rb") as img:
        await message.answer_photo(img, "Маганиз Свежих Фермерских продуктов. Местных производителей! Приятных покупок. "
                                        "По всем вопросам можете написать нам или позвонить: адрес: г.Ольгин, ул. Ленина,10., "
                                        "email:werwt@fggsg.ru, тел. 8-800-24800",
                                        reply_markup=start_kb)

@dp.message_handler(text='Магазин') # магазин для покупок
async def info(message):
    await message.answer("Bыбирите товар:", reply_markup=catalog_kb)


@dp.callback_query_handler(text="kypit") # сообщает о завершении покупки
async def pokypka(call):
    await call.message.answer(f"Вы успешно совершили покупку")
    await call.answer()

@dp.callback_query_handler(text="hleb") # товар с фото
async def buy_h(call):
    await call.message.answer(text="Свежий хлеб" f"цена за уп. {priseHleb} руб.", reply_markup=buy_kb)
    with open("hleb.png", "rb") as img:
        await call.message.answer_photo(img, "Свежий хлеб" f"цена за уп. {priseHleb} руб.", reply_markup=buy_kb)
        await call.answer()


@dp.callback_query_handler(text="riba")
async def buy_r(call):
    await call.message.answer(text="Свежая рыба" f"цена за уп. {priseRiba} руб.", reply_markup=buy_kb)
    with open("riba.png", "rb") as img:
        await call.message.answer_photo(img, "Свежая рыба" f"цена за уп. {priseRiba} руб.", reply_markup=buy_kb)
        await call.answer()



@dp.callback_query_handler(text="siir")
async def buy_s(call):
    await call.message.answer(text="Свежая рыба" f"цена за уп. {priseSiir} руб.", reply_markup=buy_kb)
    with open("sir.png", "rb") as img:
        await call.message.answer_photo(img, "Сыр Российский" f"цена за уп. {priseSiir} руб.", reply_markup=buy_kb)
        await call.answer()


@dp.callback_query_handler(text="yabloki")
async def buy_y(call):
    await call.message.answer(text="Яблоки свежий урожай" f"цена за уп. {priseRiba} руб.", reply_markup=buy_kb)
    with open("ybloko.png", "rb") as img:
        await call.message.answer_photo(img,"Яблоки свежий урожай" f"цена за уп. {priseRiba} руб.", reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text="back_to_catalog") # возврать в каталог
async def back(call):
    await call.message.answer('Что вас интересует?', reply_markup=catalog_kb)
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
