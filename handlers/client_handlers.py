from aiogram import types, Dispatcher
from create_bot import bot
from DataBase.sqlite import get_today, get_month, get_week, last_values
from keyboards import client_kb
from aiogram.dispatcher.filters.state import StatesGroup, State



class ValueStateGroup(StatesGroup):
    "Создаем класс машинного состояния FSM"

    id = State()
    category = State()
    date = State()
    value = State()

START = """
<b>Бот учета финансов💲</b>

●Добавить расходы:  /add_spend
●Расходы за сегодня:  /today
●Расходы за неделю:  /week 
●Раходы за месяц:  /month
●Последние записи:  /record
"""


async def start_command(message : types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=START,
                           reply_markup=client_kb.kb, parse_mode='html')

async def spend_today_command(message : types.Message):
    await get_today(message)


async def spend_month_command(message : types.Message):
    await get_month(message)


async def spend_week_command(message : types.Message):
    await get_week(message)


async def last_values_command(message : types.Message):
    await last_values(message)





def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(spend_today_command, commands=['today'])
    dp.register_message_handler(spend_month_command, commands=['month'])
    dp.register_message_handler(spend_week_command, commands=['week'])
    dp.register_message_handler(last_values_command, commands=['record'])

