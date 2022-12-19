import telebot
from telebot import types
from datetime import datetime
import schedule
import time
import random
from threading import Thread
import sqlite3

con = sqlite3.connect('database2.db', check_same_thread=False)
cur = con.cursor()


def db_data_val(id: int, workout_ex, date):
    cur.execute('INSERT into workouts (id, workout_ex, date) '
                'VALUES (?, ?, ?)', (id, workout_ex, date))
    con.commit()


TOKEN = '5952076296:AAHfEaaCpbFJy079Wm8IReKcnQQN634IQV8'
bot = telebot.TeleBot(TOKEN)
chat_id = 863108316  # or your chat_id

now = datetime.today()
weekdayname = now.strftime("%A").upper()
current_time = now.strftime("%H:%M")

wrkout1 = ['https://www.youtube.com/watch?v=8Hy4OstJzvc&list=PL1tB2Cr-gJvmH5SJD-Fl2OVm6ZIJpjUbw&index=1',
           'https://www.youtube.com/watch?v=lCJ42q1HGQw&list=PL1tB2Cr-gJvmH5SJD-Fl2OVm6ZIJpjUbw&index=8',
           'https://www.youtube.com/watch?v=lid4GfHO7U0&list=PL1tB2Cr-gJvmH5SJD-Fl2OVm6ZIJpjUbw&index=9',
           'https://www.youtube.com/watch?v=l6i3X0AWBLI&list=PL1tB2Cr-gJvmH5SJD-Fl2OVm6ZIJpjUbw&index=5']

wrkout2 = ['https://www.youtube.com/watch?v=btnAP-_GXtU&list=PL1tB2Cr-gJvmT_QJCtni0D53ayCRR-IYK&index=13',
           'https://www.youtube.com/watch?v=AgrXJRX39qA&list=PL1tB2Cr-gJvmT_QJCtni0D53ayCRR-IYK&index=11']

wrkout3 = ['https://www.youtube.com/watch?v=EPY5pfEhITo&list=LL&index=14',
           'https://www.youtube.com/watch?v=PTg7AizQViA']

btn = types.InlineKeyboardMarkup(row_width=1)
btn1 = types.InlineKeyboardButton(text='Тренировка на ягодицы 🌰', url=random.choice(wrkout1))
btn2 = types.InlineKeyboardButton(text='Тренировка на пресс 👟', url=random.choice(wrkout2))
btn3 = types.InlineKeyboardButton(text='Тренировка на руки 💪🏼', url=random.choice(wrkout3))
btn.add(btn1, btn2, btn3)

btntime = types.InlineKeyboardMarkup(row_width=2)
btn4 = types.InlineKeyboardButton(text='⏰ 15 минут', callback_data='15 min')
btn5 = types.InlineKeyboardButton(text='⏰ 1 час', callback_data='1 hour')
btn6 = types.InlineKeyboardButton(text='⏰ 1 час', callback_data='2 hour')
btn7 = types.InlineKeyboardButton(text='🙈 Завтра', callback_data='tomorrow')
btntime.add(btn4, btn5, btn6, btn7)


def start():
    buttons = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='Сейчас', callback_data='now')
    button2 = types.InlineKeyboardButton(text='Позже', callback_data='later')
    buttons.add(button1, button2)
    bot.send_message(chat_id=chat_id, text='Привет, напоминаю тебе, '
                                           'что сегодня {} и у тебя тренировка по расписанию. '
                                           'Будешь заниматься сейчас или позже?'.format(weekdayname),
                     reply_markup=buttons)


def end_of_day():
    endbuttons = types.ReplyKeyboardMarkup(True, True)
    endbuttons.row('Да', 'Нет')
    msg = bot.send_message(chat_id=chat_id, text="День подходит к концу. Уделила ли ты сегодня время спорту?",
                           reply_markup=endbuttons)
    bot.register_next_step_handler(msg, reg)


@bot.message_handler(content_types=['text'])
def reg(message):
    num_id = (cur.execute('SELECT MAX(id) FROM workouts')).fetchone()[0] + 1
    date_now = datetime.today().strftime("%A: %d %B")

    if message.text == 'Да':
        bot.send_message(message.chat.id, text='Ты молодец! Отдыхай!')
        wrk = "Выполнена"
        db_data_val(id=num_id, workout_ex=wrk, date=date_now)

    if message.text == 'Нет':
        bot.send_message(message.chat.id, text='Наверное, у тебя сегодня было много дел.. Напомню тебе через день')
        wrk = "Не выполнена"
        db_data_val(id=num_id, workout_ex=wrk, date=date_now)


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'now':
        bot.send_message(call.message.chat.id, text='Я подобрал тебе 3 видео с YouTube,'
                                                    ' хорошей тренировки!', reply_markup=btn)

    if call.data == 'later':
        bot.send_message(call.message.chat.id, text='OK, через сколько тебе о ней напомнить?', reply_markup=btntime)

    if call.data == '15 min':
        bot.send_message(call.message.chat.id, text='ОК, напомню через 15 минут!')
        time.sleep(1)
        bot.send_message(call.message.chat.id, text='⏳')
        time.sleep(60 * 15)
        bot.send_message(call.message.chat.id, text='15 минут прошло!', reply_markup=btn)

    if call.data == '1 hour':
        bot.send_message(call.message.chat.id, text='ОК, напомню через час!')
        time.sleep(1)
        bot.send_message(call.message.chat.id, text='⏳')
        time.sleep(60 * 60)
        bot.send_message(call.message.chat.id, text='1 час прошёл!', reply_markup=btn)

    if call.data == '2 hour':
        bot.send_message(call.message.chat.id, text='ОК, напомню через 2 часа!')
        time.sleep(1)
        bot.send_message(call.message.chat.id, text='⏳')
        time.sleep(2 * 60 * 60)
        bot.send_message(call.message.chat.id, text='2 часа прошло!', reply_markup=btn)

    if call.data == 'tomorrow':
        bot.send_message(call.message.chat.id, text='ОК, перенесём тренировку на завтра!')
        time.sleep(1)
        bot.send_message(call.message.chat.id, text='⏳')
        time.sleep(24 * 60 * 60)
        bot.send_message(call.message.chat.id, text='Прошли сутки!', reply_markup=btn)


def do_schedule():
    schedule.every().wednesday.at("10:00").do(start)
    schedule.every().thursday.at("10:00").do(start)
    schedule.every().saturday.at("10:00").do(start)
#    schedule.every().monday.at("00:16").do(start)  # for checking code (change the day and time)

    schedule.every().wednesday.at("23:00").do(end_of_day)
    schedule.every().thursday.at("23:00").do(end_of_day)
    schedule.every().saturday.at("23:00").do(end_of_day)
#    schedule.every().monday.at("15:07").do(end_of_day)     # for checking code (change the day and time)
                                                             #    and work of database

    while True:
        schedule.run_pending()
        time.sleep(1)


def main_loop():
    thread = Thread(target=do_schedule)
    thread.start()
    bot.polling(True)


if __name__ == '__main__':
    main_loop()
