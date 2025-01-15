from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = '***'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder='Нажмите нужную кнопочку')
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
kb.row(button, button2)
kb.add(button3)

kb2= InlineKeyboardMarkup()
button4 = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories')
button5 = InlineKeyboardButton(text = 'Формула расчета', callback_data='formulas')
kb2.row(button4, button5)

kb3= InlineKeyboardMarkup()
button6 = InlineKeyboardButton(text = 'Product1', callback_data='product_buying')
button7 = InlineKeyboardButton(text = 'Product2', callback_data='product_buying')
button8 = InlineKeyboardButton(text = 'Product3', callback_data='product_buying')
button9 = InlineKeyboardButton(text = 'Product4', callback_data='product_buying')
kb3.row(button6, button7, button8, button9)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text= 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup = kb2)

@dp.message_handler(text= 'Купить')
async def get_buying_list(message):
    for i in range(1,5):
        with open(f'file/{i}.jpg', 'rb') as img:
            await message.answer(f'Название: Product{i} | Описание: описание{i} | Цена: {i*100}')
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки', reply_markup = kb3)

@dp.callback_query_handler(text= 'formulas')
async def get_formulas(call):
    await call.message.answer('10*вес(кг) + 6,25*рост(см) - 5*возраст(г) - 161')

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью!', reply_markup=kb)


@dp.message_handler(text='Информация')
async def all_message(message):
    await message.answer('Я могу рассчитать норму калорий для нормальной работы организма)')


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.callback_query_handler(text='product_buying')
async def set_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    calories_w = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] - 161
    await message.answer(f'Ваша норма калорий: {calories_w}')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start для начала общения')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)