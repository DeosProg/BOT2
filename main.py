import telebot
import os
import traceback
from telebot import types
import datetime
from datetime import *
import time

# мои зависимости
import timetable_processing
import config
import texts
import homework0
import homework1
from homework_processing import processing

# from cal import cal

texxt = '''

██████╗░░█████╗░████████╗  ░██████╗████████╗░█████╗░██████╗░████████╗███████╗██████╗░
██╔══██╗██╔══██╗╚══██╔══╝  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██████╦╝██║░░██║░░░██║░░░  ╚█████╗░░░░██║░░░███████║██████╔╝░░░██║░░░█████╗░░██║░░██║
██╔══██╗██║░░██║░░░██║░░░  ░╚═══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░██╔══╝░░██║░░██║
██████╦╝╚█████╔╝░░░██║░░░  ██████╔╝░░░██║░░░██║░░██║██║░░██║░░░██║░░░███████╗██████╔╝
╚═════╝░░╚════╝░░░░╚═╝░░░  ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░
'''

codeA = config.codeA
codeB = config.codeB

bot = telebot.TeleBot(config.token)

months = ['', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
          'декабря']


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, texts.welcome_text)


@bot.message_handler(commands=['update'])
def update(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text="Главная страница💥")
    keyboard.add(button)
    bot.send_message(message.chat.id, texts.update, reply_markup=keyboard)
    print('\033[2;35;40m ' + str(message.text) + ' ' + message.from_user.first_name)


@bot.message_handler(content_types=["text"])
def text_handler(message):
    # ИНИЦИАЛИЗАЦИЯ КНОПОК, КЛАВИАТУР--------------------------------------------
    c_date = date.today()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)  # основная
    keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)  # экран приветствия
    keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True)  # главный экран
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    markup3 = types.InlineKeyboardMarkup(row_width=7)
    markupdynamic = types.InlineKeyboardMarkup(row_width=6)
    button_5 = types.KeyboardButton(text="Главная страница💥")
    button_6 = types.KeyboardButton(text="Полезные ссылки🔗")
    button_7 = types.KeyboardButton(text="Домашнее задание📚")
    button_8 = types.KeyboardButton(text="Расписание📅")

    item = types.InlineKeyboardButton('Текущая', callback_data='0')
    item2 = types.InlineKeyboardButton('Следующая', callback_data='1')

    item3 = types.InlineKeyboardButton('Сегодня', callback_data='today')
    item4 = types.InlineKeyboardButton('Завтра', callback_data='tomorrow')
    item34 = types.InlineKeyboardButton('На неделю', callback_data='default')
    item43 = types.InlineKeyboardButton('На неделю', callback_data='next')

    item5 = types.InlineKeyboardButton('Понедельник', callback_data='01')
    item6 = types.InlineKeyboardButton('Вторник', callback_data='02')
    item7 = types.InlineKeyboardButton('Среда', callback_data='03')
    item8 = types.InlineKeyboardButton('Четверг', callback_data='04')
    item9 = types.InlineKeyboardButton('Пятница', callback_data='05')
    item10 = types.InlineKeyboardButton('Суббота', callback_data='06')
    item11 = types.InlineKeyboardButton('Понедельник', callback_data='11')
    item12 = types.InlineKeyboardButton('Вторник', callback_data='12')
    item13 = types.InlineKeyboardButton('Среда', callback_data='13')
    item14 = types.InlineKeyboardButton('Четверг', callback_data='14')
    item15 = types.InlineKeyboardButton('Пятница', callback_data='15')
    item16 = types.InlineKeyboardButton('Суббота', callback_data='16')

    keyboard.add(button_8)
    keyboard.add(button_5)
    keyboard.add(button_7)

    keyboard2.add(button_5)

    keyboard3.add(button_8)
    keyboard3.add(button_7)
    keyboard3.add(button_5)
    keyboard3.add(button_6)

    markup.add(item, item2)

    markup2.add(item3, item4, item34, item43)

    markup3.add(item5, item6, item7)
    markup3.add(item8, item9, item10)
    a = datetime.now().strftime("%d.%m %H:%M")
    print('\033[2;35;40m ' + str(a) + ' ' + str(message.text) + ' ' + message.from_user.first_name)
    if len(message.text) == 4:
        try:
            path = '/root/BOT2/ID'
            filelist = []
            for root, dirs, files in os.walk(path):
                for file in files:
                    n = (os.path.join(file))
                    filelist.append(n)
            text = message.text
            for i in filelist:
                if i == text:
                    with open('ID/' + i, 'a+', encoding='utf-8') as f:
                        f.write('\n' + str(message.from_user.first_name) + '\n' + str(message.from_user.id))
                        f.close()
                    with open('ID/' + i, 'r', encoding='utf-8') as f:
                        name = f.readlines()[0]
                        name = name.replace('\n', '')
                        name = name.split(' ')
                        name = name[1] + ' ' + name[2]
                        f.close()
                    os.rename('ID/' + i, 'ID/' + i + '_a')
                    img = open('bot.gif', 'rb')
                    bot.send_video(message.chat.id, img)
                    img.close()
                    print('\033[2;32;40m [LOG] Пользователь', message.from_user.first_name, '/', message.from_user.id,
                          'зарегестрирован.')
                    bot.send_message(message.chat.id, texts.welcome_text_access.format(name=name))
                    bot.send_message(message.chat.id, texts.main, reply_markup=keyboard2)
        except Exception as exc:
            print(exc)
            traceback.print_exc()
            bot.send_message(message.chat.id, texts.welcome_text_access2)
            try:
                with open('ID/' + i, 'r', encoding='utf-8') as f:
                    id = f.readlines()[2]
                    print('\033[2;32;40m [LOG] Ошибка с пользователем ', id, 'решена')
                    bot.send_message(message.chat.id, texts.tr)
                    bot.send_message(message.chat.id, texts.main, reply_markup=keyboard2)
            except Exception as exc:
                print(exc)
                traceback.print_exc()
                print('\033[2;32;40m [LOG] Ошибка с пользователем ', id, 'не решена')
                bot.send_message(message.chat.id, texts.fl, )
    if "Домашнее задание" in message.text:
        bot.send_message(message.chat.id, 'На какую неделю хотите узнать домашнее задание?', reply_markup=markup)
    if "Расписание" in message.text:
        bot.send_message(message.chat.id, 'На какой день вы хотите узнать расписание?', reply_markup=markup2)
    if 'Главная страница' in message.text:
        try:
            bot.send_message(message.chat.id, texts.main_text, reply_markup=keyboard3)
        except Exception as exc:
            print(exc)
            traceback.print_exc()

    # ОТПРАВКА СООБЩЕНИЙ-------------------------------------------------------------
    if codeA in message.text:
        try:
            a = datetime.today().strftime("%d.%m %H:%M")
            text = str(message.text)
            text = text.replace(codeA, '')
            print('\033[2;32;40m', str(a), ' [LOG]', message.from_user.id, '/', message.from_user.first_name, ' ',
                  'отправил admin сообщение:', text)
            path = '/root/BOT2/ID'
            filelist = []
            for root, dirs, files in os.walk(path):
                for file in files:
                    n = (os.path.join(file))
                    filelist.append(n)
            for i in filelist:
                if '_a' in i:
                    with open(path + '/' + str(i), 'r+') as f:
                        line = f.readlines()
                        user = line[2]
                        bot.send_message(user, texts.messageA.format(messa=text, dt=str(a)), parse_mode='Markdown')
        except Exception as exc:
            print(i)
            print(exc)
            traceback.print_exc()

    if codeB in message.text:
        try:
            a = datetime.today().strftime("%d.%m %H:%M")
            text = str(message.text)
            text = text.replace(codeB, '')
            print('\033[2;32;40m', str(a), ' [LOG]', message.from_user.id, '/', message.from_user.first_name, ' ',
                  'отправил BOT сообщение:', text)
            path = '/root/BOT2/ID'
            filelist = []
            for root, dirs, files in os.walk(path):
                for file in files:
                    n = (os.path.join(file))
                    filelist.append(n)
            for i in filelist:
                if '_a' in i:
                    with open(path + '/' + str(i), 'r+') as f:
                        line = f.readlines()
                        user = line[2]
                        try:
                            bot.send_message(user, texts.messageB.format(messb=text, dt=str(a)), parse_mode='Markdown')
                            print('send')
                        except Exception as exc:
                            print(exc)
                            traceback.print_exc()
        except Exception as exc:
            print(exc)
            traceback.print_exc()
    if "Полезные ссылки" in message.text:
        bot.send_message(message.chat.id, texts.urls, reply_markup=keyboard2)


# ОБРАБОТКА INLINE КНОПОК--------------------------------------------------------
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    markup3 = types.InlineKeyboardMarkup(row_width=7)
    markup31 = types.InlineKeyboardMarkup(row_width=7)
    markupdynamic = types.InlineKeyboardMarkup(row_width=6)

    item = types.InlineKeyboardButton('Текущая', callback_data='0')
    item2 = types.InlineKeyboardButton('Следующая', callback_data='1')

    item3 = types.InlineKeyboardButton('Сегодня', callback_data='today')
    item4 = types.InlineKeyboardButton('Завтра', callback_data='tomorrow')
    item34 = types.InlineKeyboardButton('На неделю', callback_data='default')
    item43 = types.InlineKeyboardButton('На неделю', callback_data='next')

    item5 = types.InlineKeyboardButton('Понедельник', callback_data='01')
    item6 = types.InlineKeyboardButton('Вторник', callback_data='02')
    item7 = types.InlineKeyboardButton('Среда', callback_data='03')
    item8 = types.InlineKeyboardButton('Четверг', callback_data='04')
    item9 = types.InlineKeyboardButton('Пятница', callback_data='05')
    item10 = types.InlineKeyboardButton('Суббота', callback_data='06')
    item11 = types.InlineKeyboardButton('Понедельник', callback_data='11')
    item12 = types.InlineKeyboardButton('Вторник', callback_data='12')
    item13 = types.InlineKeyboardButton('Среда', callback_data='13')
    item14 = types.InlineKeyboardButton('Четверг', callback_data='14')
    item15 = types.InlineKeyboardButton('Пятница', callback_data='15')
    item16 = types.InlineKeyboardButton('Суббота', callback_data='16')

    markup.add(item, item2)
    markup2.add(item3, item4, item34,item43)
    markup3.add(item5, item6, item7)
    markup3.add(item8, item9, item10)
    markup31.add(item11, item12, item13)
    markup31.add(item14, item15, item16)

    if call.message:

        # ДОМАШНЕЕ ЗАДАНИЕ-------------------------------------------------------
        if call.data == '0':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='На какой день вы хотите узнать домашнее задание?', reply_markup=markup3)
        elif call.data == '1':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='На какой день вы хотите узнать домашнее задание?', reply_markup=markup31)
        elif call.data == '01':
            try:
                lst = homework0.Mo
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(r'/root/BOT2/' + urls[0], 'rb'))
                print(lst)
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '02':
            try:
                lst = homework0.Tu
                print(lst)
                print(homework0.Tu)
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(r'/root/BOT2/' + urls[0], 'rb'))
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '03':
            try:
                lst = homework0.We
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(r'/root/BOT2/' + urls[0], 'rb'))
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '04':
            try:
                lst = homework0.Th
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(r'/root/BOT2/' + urls[0], 'rb'))
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '05':
            try:
                lst = homework0.Fr
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(r'/root/BOT2/' + urls[0], 'rb'))
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '06':
            try:
                lst = homework0.Sa
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(r'/root/BOT2/' + urls[0], 'rb'))
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '11':
            try:
                lst = homework1.Mo
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(r'/root/BOT2/' + urls[0], 'rb'))
                print(lst)
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '12':
            try:
                lst = homework1.Tu
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(r'/root/BOT2/' + urls[0], 'rb'))
                print(lst)
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '13':
            try:
                lst = homework1.We
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(r'/root/BOT2/' + urls[0], 'rb'))
                print(lst)
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '14':
            try:
                lst = homework1.Th
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(r'/root/BOT2/' + urls[0], 'rb'))
                print(lst)
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '15':
            try:
                lst = homework1.Fr
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(r'/root/BOT2/' + urls[0], 'rb'))
                print(lst)
            except Exception as exc:
                traceback.print_exc()
        elif call.data == '16':
            try:
                lst = homework1.Sa
                hw, urls = processing(lst)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.homework.format(a=hw[0], b=hw[1], c=hw[2], d=hw[3], e=hw[4]),
                                      reply_markup=markupdynamic)
                bot.send_document(call.message.chat.id, open(r'/root/BOT2/' + urls[0], 'rb'))
                print(lst)
            except Exception as exc:
                traceback.print_exc()

        # РАСПИСАНИЕ-------------------------------------------------------------
        elif call.data == 'today':
            try:
                today = datetime.today()
                nn = int(today.strftime("%U")) - 35
                c_date = date.today()
                day = str(c_date.day) + ' '
                month = months[int(c_date.month)]
                pairs = timetable_processing.get_timetable_today()
                try:
                    if pairs[5] == 'Авиамоторная':
                        place = 'на Авиамоторной'
                    elif pairs[5] == 'D':
                        place = 'онлайн 💻'
                    else:
                        place = 'на Октябрьском поле'
                except:
                    place = 'нигде'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.timetables_text.format(day=day + month, place=place, pair1=pairs[0],
                                                                        pair2=pairs[1], pair3=pairs[2], pair4=pairs[3],
                                                                        pair5=pairs[4],
                                                                        nn="\nТекущая неделя - " + str(nn + 1),
                                                                        parse_mode="Markdown"))
            except Exception as exc:
                print(exc)
                traceback.print_exc()

        elif call.data == 'tomorrow':
            try:
                c_date = date.today()
                day = str(int(c_date.day) + 1) + ' '
                month = months[int(c_date.month)]
                pairs = timetable_processing.get_timetable_tomorrow()
                try:
                    if pairs[5] == 'Авиамоторная':
                        place = 'на Авиамоторной'
                    elif pairs[5] == 'D':
                        place = 'онлайн 💻'
                    else:
                        place = 'на Октябрьском поле'
                except:
                    place = 'нигде'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                      text=texts.timetables_text.format(
                                          day=day + month,
                                          place=place,
                                          pair1=pairs[0],
                                          pair2=pairs[1],
                                          pair3=pairs[2],
                                          pair4=pairs[3],
                                          pair5=pairs[4],
                                          nn=" ",
                                          parse_mode="Markdown"))
            except Exception as exc:
                print(exc)
                traceback.print_exc()

        elif call.data == 'default':
            try:
                week_number = timetable_processing.get_week_num
                if week_number == 2:
                    bot.send_photo(chat_id=call.message.chat.id, photo=open('0.png', 'rb'))
                    bot.send_message(call.message.chat.id,"Цветовые обозначения:")
                    bot.send_message(call.message.chat.id, "Лекции - 🟢")
                    bot.send_message(call.message.chat.id, "Практика - 🟠")
                    bot.send_message(call.message.chat.id, "Лабораторные - 🟣")
                                     
                    
                else:
                    bot.send_photo(chat_id=call.message.chat.id, photo=open('1.png', 'rb'))
                    bot.send_message(call.message.chat.id,"Цветовые обозначения:")
                    bot.send_message(call.message.chat.id, "Лекции - 🟢")
                    bot.send_message(call.message.chat.id, "Практика - 🟠")
                    bot.send_message(call.message.chat.id, "Лабораторные - 🟣")

            except Exception as exc:
                print(exc)
                traceback.print_exc()
           
       elif call.data == 'default':
            try:
                week_number = timetable_processing.get_week_num
                if week_number == 1:
                    bot.send_photo(chat_id=call.message.chat.id, photo=open('0.png', 'rb'))
                    bot.send_message(call.message.chat.id,"Цветовые обозначения:")
                    bot.send_message(call.message.chat.id, "Лекции - 🟢")
                    bot.send_message(call.message.chat.id, "Практика - 🟠")
                    bot.send_message(call.message.chat.id, "Лабораторные - 🟣")
                                     
                    
                else:
                    bot.send_photo(chat_id=call.message.chat.id, photo=open('1.png', 'rb'))
                    bot.send_message(call.message.chat.id,"Цветовые обозначения:")
                    bot.send_message(call.message.chat.id, "Лекции - 🟢")
                    bot.send_message(call.message.chat.id, "Практика - 🟠")
                    bot.send_message(call.message.chat.id, "Лабораторные - 🟣")

            except Exception as exc:
                print(exc)
                traceback.print_exc()


if __name__ == '__main__':
    print(texxt)
    bot.infinity_polling()
    '''
    while(True):
        try:
            bot.infinity_polling()
        except Exception as e:
            time.sleep(1)
            print(e)
    '''
