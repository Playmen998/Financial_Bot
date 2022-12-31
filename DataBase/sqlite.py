import sqlite3 as sq
from create_bot import bot
import datetime


now = datetime.datetime.now()
month = now.strftime("%B")



async def db_start():
    "Создание БД"
    global db, cur

    db = sq.connect('finance.db')
    cur = db.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS finance(id INTEGER,user_id TEXT, date TEXT, category TEXT, value INTEGER)')
    db.commit()


async def create_value(state,user_id):
    "Добавляем значения в БД"
    async with state.proxy() as data:
        cur.execute("INSERT INTO finance VALUES(?, ?, ?, ?, ?)",(data['id'], user_id, data['date'], data['category'], data['value']))
        db.commit()


async def get_today(message):
    "Получаем траты за сегоднешний день"
    result = f"<b>Ваши траты за сегодня:</b>\n"
    for ret in cur.execute("""SELECT category, sum(value) from finance 
    where strftime('%d', datetime('now')) = strftime('%d', date) 
    group by category
    order by sum(value)""").fetchall():
        result += '\n'
        result += f'{ret[0]} - {ret[1]} руб.\n'
    total = cur.execute("""SELECT sum(value) from finance 
    where strftime('%d', datetime('now')) = strftime('%d', date)""").fetchall()
    result += '__________________________________\n'
    result += f'<b>Общий итог:</b> {total[0][0]} руб'
    await bot.send_message(message.from_user.id, text= result, parse_mode='html')

async def get_month(message):
    "Получаем траты за месяц"
    result = f"<b>Ваши траты за {month}:</b>\n"
    for ret in cur.execute("""SELECT category, sum(value) from finance
    where strftime('%m', datetime('now')) = strftime('%m', date)
    group by category
    order by sum(value)""").fetchall():
        result += '\n'
        result += f'{ret[0]} - {ret[1]} руб.\n'
    total = cur.execute("""SELECT sum(value) from finance 
    where strftime('%m', datetime('now')) = strftime('%m', date)""").fetchall()
    result += '__________________________________\n'
    result += f'<b>Общий итог:</b> {total[0][0]} руб'
    await bot.send_message(message.from_user.id, text=result, parse_mode='html')

async def get_week(message):
    "Получаем траты за неделю"
    result = f"<b>Ваши траты за неделю:</b>\n"
    for ret in cur.execute("""SELECT category, sum(value) from finance
    where strftime('%W', datetime('now')) = strftime('%W', date)
    group by category
    order by sum(value)""").fetchall():
        result += '\n'
        result += f'{ret[0]} - {ret[1]} руб.\n'
    total = cur.execute("""SELECT sum(value) from finance 
        where strftime('%W', datetime('now')) = strftime('%W', date)""").fetchall()
    result += '__________________________________\n'
    result += f'<b>Общий итог:</b> {total[0][0]} руб'
    await bot.send_message(message.from_user.id, text=result, parse_mode='html')

async def last_values(message):
    "Вывод последних 5 добавленных записей"
    global value, msg_del
    value = []
    result = '<b>Последние 5 записей:</b>\n\n'
    i = 1
    for ret in cur.execute("""select category, value, strftime('%H:%M - %d', date), id from finance
    order by date desc
    limit 5""").fetchall():
        result += f'Время: {ret[2]} \n{ret[0]} - {ret[1]} руб. /del_{i}\n\n'
        value.append(ret[3])
        i += 1
    msg_del = await bot.send_message(message.from_user.id, text=result, parse_mode='html')
    # используем глобальную переменную msg_del, чтобы потом удалять данное сообщение

"""
--------Команды для удаления строк--------
"""

async def del_0(message):
    for ret in cur.execute(f"""select category, value, strftime('%H:%M - %d', date) from finance
    where id = {value[0]}""").fetchall():
        result = f'Время: {ret[2]} \n{ret[0]} - {ret[1]} руб.\n\n'
    cur.execute(f"""DELETE from finance where id = {value[0]}""")
    db.commit()
    await msg_del.delete()
    await bot.send_message(message.from_user.id, text=f'✅ <b>Запись удалена</b>\n\n{result}', parse_mode='html')

async def del_1(message):
    for ret in cur.execute(f"""select category, value, strftime('%H:%M - %d', date) from finance
    where id = {value[1]}""").fetchall():
        result = f'Время: {ret[2]} \n{ret[0]} - {ret[1]} руб.\n\n'
    cur.execute(f"""DELETE from finance where id = {value[1]}""")
    db.commit()
    await msg_del.delete()
    await bot.send_message(message.from_user.id, text=f'✅ <b>Запись удалена</b>\n\n{result}', parse_mode='html')

async def del_2(message):
    for ret in cur.execute(f"""select category, value, strftime('%H:%M - %d', date) from finance
    where id = {value[2]}""").fetchall():
        result = f'Время: {ret[2]} \n{ret[0]} - {ret[1]} руб.\n\n'
    cur.execute(f"""DELETE from finance where id = {value[2]}""")
    db.commit()
    await msg_del.delete()
    await bot.send_message(message.from_user.id, text=f'✅ <b>Запись удалена</b>\n\n{result}', parse_mode='html')

async def del_3(message):
    for ret in cur.execute(f"""select category, value, strftime('%H:%M - %d', date) from finance
    where id = {value[3]}""").fetchall():
        result = f'Время: {ret[2]} \n{ret[0]} - {ret[1]} руб.\n\n'
    cur.execute(f"""DELETE from finance where id = {value[3]}""")
    db.commit()
    await msg_del.delete()
    await bot.send_message(message.from_user.id, text=f'✅ <b>Запись удалена</b>\n\n{result}', parse_mode='html')

async def del_4(message):
    for ret in cur.execute(f"""select category, value, strftime('%H:%M - %d', date) from finance
    where id = {value[4]}""").fetchall():
        result = f'Время: {ret[2]} \n{ret[0]} - {ret[1]} руб.\n\n'
    cur.execute(f"""DELETE from finance where id = {value[4]}""")
    db.commit()
    await msg_del.delete()
    await bot.send_message(message.from_user.id, text=f'✅ <b>Запись удалена</b>\n\n{result}', parse_mode='html')