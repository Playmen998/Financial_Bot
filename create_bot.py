from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
#from config import TOKEN
import os

TOKEN = os.getenv("TOKEN")

storage = MemoryStorage()
bot = Bot(TOKEN)
dp = Dispatcher(bot, storage = storage)
