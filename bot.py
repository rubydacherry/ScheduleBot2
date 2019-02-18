import requests
import datetime
import math
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
        return 'Monday'
    elif wd == 'вторник':
        return 'Tuesday'
    elif wd == 'среда':
        return 'Wednesday'
    elif wd == 'четверг':
        return 'Thursday'
    elif wd == 'пятница':
        return 'Friday'
    elif wd == 'суббота':
        return 'Saturday'
    elif wd == 'воскресенье':
        return 'Monday'

def output(group_schedule, requested_weekday, last_chat_id, greet_bot):
    amount = len(group_schedule[requested_weekday])
    greet_bot.send_message(
            last_chat_id,
            '''
                {}\n\n
                9:00-10:20: {}\n\n
                10:30-11:50: {}\n\n
                12:00-13:20: {}\n\n
                13:30-14:50: {}\n\n
                15:00-16:20: {}\n\n
                16:30-17:50: {}\n\n
                17:50-19:20: {}\n
            '''.format(
                    requested_weekday,
                    group_schedule[requested_weekday][0] if amount > 0 else '',
                    '''group_schedule[requested_weekday][1] if amount > 1 else''' '',
                    '''group_schedule[requested_weekday][2] if amount > 2 else''' '',
                    '''group_schedule[requested_weekday][3] if amount > 3 else''' '',
                    '''group_schedule[requested_weekday][4] if amount > 4 else''' '',
                    '''group_schedule[requested_weekday][5] if amount > 5 else''' '',
                    '''group_schedule[requested_weekday][6] if amount > 6 else''' '',
                ).replace('    ', '')
    )
        

token = '693504057:AAF56kZHnpjAmWjvNiwLWTaEh0m0WBkQnbY'
greet_bot = BotHandler(token)
is_week_even = True
is_new_week = False

def main():
    new_offset = None
    is_week_even = False

    while True:

        is_week_even = True if (math.ceil(datetime.date.max.toordinal() / 7) % 2) == 1 else False

        greet_bot.get_updates(new_offset)
        last_update = greet_bot.get_last_update()

        if last_update == False:
            continue       

        last_update_id = last_update['update_id']
        last_chat_id = last_update['message']['chat']['id']

        requested_weekday = last_update['message']['text'][:-1].strip().lower()
        group_number = last_update['message']['text'][-1]

        is_requested_first_group = (group_number == '1')

        requested_weekday = getWeekDay(requested_weekday)

    group_one_schedule = {
                            'Monday': [
                                        '', 
                                    'Пр. Алгебра 473' if is_week_even else '',
                                    'Лекц. Алгебра, Попов А.М., 260',
                                    'Обед',
                                    'Пр. Иностранный язык',
                                    'Пр. Иностранный язык' if is_week_even else 'ДПО "Модуль переводчика"',
                                    'ДПО "Модуль переводчика"'
                                    ],
                            
                            'Tuesday': [
                                        'Лекц. Компы, Аносова Н.П. 495а',
                                        'Лаб. Компы, ДК-3',
                                        'Обед',
                                        'Прикладная физическая культура, Мальченко А.Д., ФОК РУДН'
                                    ],

                            'Wednesday': [
                                            'Пр. Алгебра 104',
                                            'Пр. Аналитическая геометрия 473',
                                            'Лекц. Аналитическая геометрия, Гольдман М.Л., 260',
                                            'Обед',
                                            'Лекция Деловой Этикет Варламова И.Ю. 397' if is_week_even else 'Лекц. Алгебра 263',
                                            'Пр. Деловой этикет 262' if is_week_even else ''
                                        ],
                        
                            'Thursday': [
                                            'Лекц./Пр. Проф. этика Лапшин И.Е. 104',
                                            'Пр. История 258',
                                            'Лекц. Матан 263',
                                            'Пр. Матан 261',
                                            'Обед',
                                            ''
                                        ],

                            'Friday': [
                                        'Лекц. Математический анализ, Марченко В.В., 261'
                                    ],

                            'Saturday': [
                                        'Лекц. Политология 104' if is_week_even else 'Пр. Психология Зал 1',
                                        'Лекц. Политология 104' if is_week_even else 'Пр. Психология Зал 1'
                                        ]
                        }

    group_two_schedule = {
                            'Monday': [
                                        '', 
                                    '' if is_week_even else 'Пр. Алгебра 473',
                                    'Лекц. Алгебра, Попов А.М., 260',
                                    'Обед',
                                    'Пр. Иностранный язык',
                                    'Пр. Иностранный язык' if is_week_even else 'ДПО "Модуль переводчика"',
                                    'ДПО "Модуль переводчика"'
                                    ],
                            
                            'Tuesday': [
                                        'Лекц. Компы, Аносова Н.П. 495а',
                                        'Пр. Математический анализ 258',
                                        'Обед',
                                        'Прикладная физическая культура, Мальченко А.Д., ФОК РУДН'
                                    ],

                            'Wednesday': [
                                            'Пр. Аналитическая геометрия 264',
                                            'Пр. Алгебра 471',
                                            'Лекц. Аналитическая геометрия, Гольдман М.Л., 260',
                                            'Обед',
                                            'Лекция Деловой Этикет Варламова И.Ю. 397' if is_week_even else 'Лекц. Алгебра 263',
                                            'Пр. Деловой этикет 262' if is_week_even else ''
                                        ],
                        
                            'Thursday': [
                                            'Лекц./Пр. Проф. этика Лапшин И.Е. 104',
                                            'Пр. История 258',
                                            'Лекц. Матан 263',
                                            'Пр. Матан 261',
                                            'Обед',
                                            ''
                                        ],

                            'Friday': [
                                        'Лекц. Математический анализ, Марченко В.В., 261'
                                    ],

                            'Saturday': [
                                        'Лекц. Политология 104' if is_week_even else 'Пр. Психология Зал 1',
                                        'Лекц. Политология 104' if is_week_even else 'Пр. Психология Зал 1'
                                        ]
    }

    group_schedule = group_one_schedule if is_requested_first_group else group_two_schedule
    #output(group_schedule, requested_weekday, last_chat_id, greet_bot)
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
    new_offset = last_update_id + 1

if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
