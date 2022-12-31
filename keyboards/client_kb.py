from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


ikb = InlineKeyboardMarkup(row_width=3)
ib1 = InlineKeyboardButton(text = '🛒Продукты',
                           callback_data= '🛒Продукты')
ib2 = InlineKeyboardButton(text = '🍔Фастфуд',
                           callback_data='🍔Фастфуд')
ib3 = InlineKeyboardButton(text='🙋Личное',
                            callback_data='🙋Личное')
ib4 = InlineKeyboardButton(text='💊Здоровье',
                           callback_data='💊Здоровье')
ib5 = InlineKeyboardButton(text='🚇Транспорт',
                           callback_data='🚇Транспорт')
ib6 = InlineKeyboardButton(text='👚Одежда, товары',
                           callback_data='👚Одежда, товары')
ib7 = InlineKeyboardButton(text='🚰Коммунальные',
                           callback_data='🚰Коммунальные')
ib8 = InlineKeyboardButton(text='🌐Интернет, связь',
                           callback_data='🌐Интернет, связь')
ib9 = InlineKeyboardButton(text='📚Образование',
                           callback_data='📚Образование')
ib10 = InlineKeyboardButton(text='📺Подписки',
                           callback_data='📺Подписки')
ib11 = InlineKeyboardButton(text='🎢Развлечение',
                           callback_data='🎢Развлечение')
ib12 = InlineKeyboardButton(text='🚧Непредвиденное',
                           callback_data='🚧Непредвиденное')

ikb.add(ib1,ib2,ib3).add(ib4,ib5,ib6).add(ib7,ib8,ib9).add(ib10,ib11,ib12)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb1 = KeyboardButton('/add_spend')
kb2 = KeyboardButton('/today')
kb3 = KeyboardButton('/week')
kb4 = KeyboardButton('/month')
kb5 = KeyboardButton('/record')

kb.add(kb1, kb5).add(kb2,kb3,kb4)


