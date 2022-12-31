from aiogram import executor, types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from DataBase.sqlite import db_start
from create_bot import dp
from handlers import client_handlers, delete_handlers
from callback import client_callback



async def on_startup(_):
    print('Бот запущен')
    await db_start()


"""
Данный класс позволяет пользоваться ботом только определеным пользователям
"""
# ADMIN = 902582088

# class CustomMiddleware(BaseMiddleware):
#
#     async def on_process_message(self, message: types.Message,data: dict):
#
#         if message.from_user.id != ADMIN:
#             print(message.from_user.id)
#             raise CancelHandler()

client_handlers.register_handlers_client(dp)

client_callback.register_callback_client(dp)

delete_handlers.register_handlers_delete(dp)


if __name__ == '__main__':
    # dp.middleware.setup(CustomMiddleware())
    executor.start_polling(dp, skip_updates=True, on_startup = on_startup)