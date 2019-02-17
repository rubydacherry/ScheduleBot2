import requests
import datetime
import time
from time import sleep

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = 'https://api.telegram.org/bot{}/'.format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = False

        return last_update

def getWeekDay(wd):
    if wd == 'понедельник':
        return 0
    elif wd == 'вторник':
        return 1;
    elif wd == 'среда':
        return 2
    elif wd == 'четверг':
        return 3;
    elif wd == 'пятница':
        return 4
    elif wd == 'суббота':
        return 5
    elif wd == 'воскресенье':
        return 6

token = '693504057:AAF56kZHnpjAmWjvNiwLWTaEh0m0WBkQnbY'
greet_bot = BotHandler(token)
is_week_odd = True
is_new_week = False

'''
Нужно:
- Функция которая собирает рассписание (group, odd, day)
- Функция аутпута (func Shedule output)
'''

def main():
    new_offset = None
    is_week_odd = False

    while True:

        today = datetime.datetime.today()

        if today.weekday() == 5 and is_new_week:
            is_week_odd = not is_week_odd
            is_new_week == False

        if today.weekday() == 6:
            is_new_week == True

        greet_bot.get_updates(new_offset)
        last_update = greet_bot.get_last_update()

        if last_update == False:
            continue       

        last_update_id = last_update['update_id']
        last_chat_id = last_update['message']['chat']['id']

        requested_weekday = last_update['message']['text'][:-1].strip().lower()
        group_number = last_update['message']['text'][-1]

        is_requested_first_group = (group_number == '1')

        todays = ('пары', 'рассписание', 'сегодня')

        if requested_weekday == 'завтра':
            requested_weekday = today.weekday() + 1
        elif requested_weekday in todays:
            requested_weekday = today.weekday()
        else:
            requested_weekday = getWeekDay(requested_weekday)

        # понедельник
        if requested_weekday == 0:
            greet_bot.send_message(
                last_chat_id,
                '''
                    Понедельник\n\n
                    9:00-10:20: {}\n\n
                    10:30-11:50: {}\n\n
                    12:00-13:20: {}\n\n
                    13:30-14:50: {}\n\n
                    15:00-16:20: {}\n\n
                    16:30-17:50: {}\n\n
                    17:50-19:20: {}\n
                '''.format(
                        '',
                        'Пр. Алгебра 473' if is_requested_first_group else '',
                        'Лекц. Алгебра, Попов А.М., 260',
                        'Обед',
                        'Пр. Иностранный язык 475 / Русский язык 402',
                        'Пр. Иностранный язык 475 / Русский язык 402' if is_week_odd else 'ДПО "Модуль переводчика" 475 / Русский язык 402',
                        'ДПО "Модуль переводчика" 475'
                    ).replace('    ', '')
            )

        # вторник
        elif requested_weekday == 1:
            greet_bot.send_message(
                last_chat_id,
                '''
                    Вторник\n\n
                    9:00-10:20: {}\n\n
                    10:30-11:50: {}\n\n
                    12:00-13:20: {}\n\n
                    13:30-14:40: {}\n
                '''.format(
                        'Лекц. Компы, Аносова Н.П. 495а',
                        'Пр. Математический анализ 258' if is_requested_first_group else 'Лаб. Компы, ДК-3',
                        'Обед',
                        'Прикладная физическая культура, Мальченко А.Д., ФОК РУДН'
                    ).replace('    ', '')
            )

        # среда
        elif requested_weekday == 2:
            greet_bot.send_message(
                last_chat_id,
                '''
                    Среда\n\n
                    9:00-10:20: {}\n\n
                    10:30-11:50: {}\n\n
                    12:00-13:20: {}\n\n
                    13:30-14:50: {}\n\n  
                    15:00-16:20: {}\n\n
                    16:30-17:50: {}\n
                '''.format(
                        'Пр. Аналитическая геометрия 264' if is_requested_first_group else 'Пр. Алгебра 104',
                        'Пр. Алгебра 471' if is_requested_first_group else 'Пр. Аналитическая геометрия 273',
                        'Лекц. Аналитическая геометрия, Гольдман М.Л., 260',
                        'Обед',
                        'Лекция Деловой Этикет Варламова И.Ю. 397 / Лекц. Алгебра 263',
                        'Пр. Деловой этикет 262'
                    ).replace('    ', '')
            )

        # четверг
        elif requested_weekday == 3:
            greet_bot.send_message(
                last_chat_id,
                '''
                    Четверг\n\n
                    9:00-10:20: {}\n\n
                    10:30-11:50: {}\n\n
                    12:00-13:20: {}\n\n
                    13:30-14:50: {}\n\n
                    15:00-16:20: {}\n\n
                    16:30-17:50: {}\n
                '''.format(
                        'Лекц./Пр. Проф. этика Лапшин И.Е. 104',
                        'Пр. Матан 261' if is_requested_first_group else 'Пр. История 258',
                        'Лекц. Матан 263',
                        'Пр. История 264' if is_requested_first_group else 'Пр. Матан 261',
                        'Обед',
                        'Лаб. Компы 422'  if is_requested_first_group else ''
                    ).replace('    ', '')
            )

        # пятница
        elif requested_weekday == 4:
            greet_bot.send_message(
                last_chat_id,
                '''
                    Пятница\n\n
                    12:00-13:20: {}\n\n
                    13:30-14:50: {}\n
                '''.format(
                        'Лекц. Математический анализ, Марченко В.В., 261',
                        '' if is_week_odd else 'Пр. Матан 260'
                    ).replace('    ', '')
            )
        
        # суббота
        elif requested_weekday == 5:
            greet_bot.send_message(
                last_chat_id,
                 '''
                    Суббота\n\n
                    9:00-10:20: {}\n\n
                    10:30-11:50: {}\n
                '''.format(
                        'Лекц. Политология 104 / Пр. Психология Зал 1',
                        'Пр. Политология 104 / Лекц. Психология Зал 1'
                    ).replace('    ', '')
                )

        # воскресенье
        elif requested_weekday == 6:
            greet_bot.send_message(last_chat_id, 'Sunday')

        new_offset = last_update_id + 1



if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
