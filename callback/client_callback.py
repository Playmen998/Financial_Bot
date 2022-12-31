from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from handlers import client_handlers
from DataBase import sqlite
from create_bot import bot
from keyboards import client_kb

async def add_spend_command(message : types.Message):
    global INL_TAB, CANCEL
    CANCEL = await bot.send_message(chat_id=message.from_user.id,
                           text='Для отмены нажмите команду /cancel')
    INL_TAB = await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите нужную категорию:',
                           reply_markup = client_kb.ikb)

async def products_callback(callback: types.CallbackQuery, state: FSMContext):
    global COSTS
    async with state.proxy() as data:
        data['id'] = callback.id
        data['category'] = callback.data
        data['date'] = callback['message']['date']
    COSTS = await callback.message.answer(f'Введите сумму расходов для категории {callback.data}:')
    await callback.answer()
    await client_handlers.ValueStateGroup.value.set() # ожидаем ввод числа

async def value_message(message: types.Message, state: FSMContext):
    global NUM
    if message.text.isdigit():
        async with state.proxy() as data:
            data['value'] = message.text
        await INL_TAB.delete()
        await CANCEL.delete()
        result = f"✅ <b>Данные успешно сохранены</b>\n\nВремя: {data['date'].strftime('%H:%M - %d')}\n{data['category']} - {data['value']} руб."
        await message.answer(result, parse_mode='html')
        await sqlite.create_value(state, user_id=message.from_user.id)
        await state.finish()
    else:
        NUM = await message.answer('Введите число')

async def cancel_command(message : types.Message, state: FSMContext):
    if state is None:
        return
    await state.finish()
    await INL_TAB.delete()
    await CANCEL.delete()
    if "COSTS" in globals():
        await COSTS.delete()
    if 'NUM' in globals():
        await NUM.delete()
    await message.answer('✅ <b>Вы отменили команду</b>', parse_mode='html')

def register_callback_client(dp: Dispatcher):
    dp.register_message_handler(cancel_command, commands=['cancel'], state='*')
    dp.register_message_handler(add_spend_command, commands=['add_spend'], state='*')
    dp.register_callback_query_handler(products_callback)
    dp.register_message_handler(value_message, state=client_handlers.ValueStateGroup.value)