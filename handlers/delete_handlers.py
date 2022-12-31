from aiogram import types, Dispatcher
from DataBase.sqlite import del_0, del_1, del_2, del_3, del_4

async def del_handler_0(message : types.Message):
    await del_0(message)

async def del_handler_1(message : types.Message):
    await del_1(message)

async def del_handler_2(message : types.Message):
    await del_2(message)

async def del_handler_3(message : types.Message):
    await del_3(message)

async def del_handler_5(message : types.Message):
    await del_4(message)

async def handler(message: types.Message):
    await message.reply(text='Для запуска бота нажмите команду /start')

def register_handlers_delete(dp: Dispatcher):
    dp.register_message_handler(del_handler_0, commands=['del_1'])
    dp.register_message_handler(del_handler_1, commands=['del_2'])
    dp.register_message_handler(del_handler_2, commands=['del_3'])
    dp.register_message_handler(del_handler_3, commands=['del_4'])
    dp.register_message_handler(del_handler_5, commands=['del_5'])
    dp.register_message_handler(handler)