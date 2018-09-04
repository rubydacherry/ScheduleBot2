import requests
import datetime
import time
from time import sleep

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

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

token = '693504057:AAF56kZHnpjAmWjvNiwLWTaEh0m0WBkQnbY'
greet_bot = BotHandler(token)  
greetings = ('здравствуй', 'привет', 'ку', 'здорово')
pairs1 = ('пары1', 'рассписание1', 'пары 1', 'рассписание 1')
pairs2 = ('пары2', 'рассписание2', 'пары 2', 'рассписание 2')
pairs1Tommorow = ('завтра1', 'завтра 1')
pairs2Tommorow = ('завтра2', 'завтра 2')

now = datetime.datetime.now()

def main():  
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        greet_bot.get_updates(new_offset)
        last_update = greet_bot.get_last_update()

        if last_update == False:
            continue
        '''
        if not 'message' in last_update.keys():
            new_offset = last_update_id + 1
            continue
        if not 'text' in last_update['message'].keys():
            new_offset = last_update_id + 1
            continue
        if not 'chat' in last_update['message'].keys():
            new_offset = last_update_id + 1
            continue
        if not 'id' in last_update['message'].keys():        
            new_offset = last_update_id + 1
            continue
        if not 'update_id' in last_update.keys():    
            new_offset = last_update_id + 1
            continue
        '''
        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']

        '''
        last_chat_name = last_update['message']['chat']['first_name']
        last_chat_name = 'кто-то'
        '''

        if (last_chat_text.lower() in pairs1 and datetime.datetime.today().weekday() == 0) or (last_chat_text.lower() in pairs1Tommorow and datetime.datetime.today().weekday() == 6) or last_chat_text.lower() == 'понедельник1':
            greet_bot.send_message(last_chat_id, '''
                                                    Понедельник (1):
                                                    \n
                                                    09:00-10:20: Пр. Математический анализ, 480
                                                    \n
                                                    10:30-11:50: Лекц. Математический анализ, Марченко В.В., 398
                                                    \n
                                                    12:00-13:20: Лекц. Алгебра, Попов А.М., 399
                                                    \n
                                                    13:30-14:50: Обед
                                                    \n
                                                    15:00-16:20: Пр. Иностранный язык 475 / Русский язык 402
                                                    \n
                                                    16:30-17:50: Пр. Иностранный язык 475 / Русский язык 402 / ДПО "Модуль переводчика 475"
                                                    \n
                                                    17:50-19:20: ДПО "Модуль переводчика" 475
                                                    \n
                                                    19:30-20:50: '''.replace('    ', ''))

        elif (last_chat_text.lower() in pairs1 and datetime.datetime.today().weekday() == 1) or (last_chat_text.lower() in pairs1Tommorow and datetime.datetime.today().weekday() == 0)  or last_chat_text.lower() == 'вторник1':
            greet_bot.send_message(last_chat_id, '''Вторник (1)
                                                    \n
                                                    09:00-10:20: 
                                                    \n
                                                    10:30-11:50: 
                                                    \n
                                                    12:00-13:20: Обед
                                                    \n
                                                    13:30-14:50: ФОК Мальченко А.Д.
                                                    \n
                                                    15:00-16:20: 
                                                    \n
                                                    16:30-17:50: 
                                                    \n
                                                    17:50-19:20:
                                                    \n
                                                    19:30-20:50: '''.replace('    ', ''))

        elif (last_chat_text.lower() in pairs1 and datetime.datetime.today().weekday() == 2) or (last_chat_text.lower() in pairs1Tommorow and datetime.datetime.today().weekday() == 1) or last_chat_text.lower() == 'среда1':
            greet_bot.send_message(last_chat_id, '''Среда (1)
                                                    \n
                                                    09:00-10:20: Пр. Аналитическая геометрия, 482
                                                    \n
                                                    10:30-11:50: Пр. Основы риторики и коммуникации 264
                                                    \n
                                                    12:00-13:20: Лекц. Аналитическая геометрия, Гольдман М.Л., 260
                                                    \n
                                                    13:30-14:50: Обед
                                                    \n
                                                    15:00-16:20: 
                                                    \n
                                                    16:30-17:50: 
                                                    \n
                                                    17:50-19:20: 
                                                    \n
                                                    19:30-20:50: '''.replace('    ', ''))

        elif (last_chat_text.lower() in pairs1 and datetime.datetime.today().weekday() == 3) or (last_chat_text.lower() in pairs1Tommorow and datetime.datetime.today().weekday() == 2) or last_chat_text.lower() == 'четверг1':
            greet_bot.send_message(last_chat_id, '''Четверг (1)
                                                    \n
                                                    09:00-10:20: 
                                                    \n
                                                    10:30-11:50: Лекц. Компьютерные науки и технологии программирования, Аносова Н.П., 398
                                                    \n
                                                    12:00-13:20: Пр. Алгебра, 471
                                                    \n
                                                    13:30-14:50: Обед
                                                    \n
                                                    15:00-16:20: Лаб Комп. науки и техн. прогр. ДК-1
                                                    \n
                                                    16:30-17:50: 
                                                    \n
                                                    17:50-19:20: 
                                                    \n
                                                    19:30-20:50: '''.replace('    ', ''))

        elif (last_chat_text.lower() in pairs1 and datetime.datetime.today().weekday() == 4) or (last_chat_text.lower() in pairs1Tommorow and datetime.datetime.today().weekday() == 3) or last_chat_text.lower() == 'пятница1':
            greet_bot.send_message(last_chat_id, '''Пятница (1)
                                                    \n
                                                    09:00-10:20: Пр. Математический анализ, 264
                                                    \n
                                                    10:30-11:50: Лекц. Математический анализ, Марченко В.В., 261
                                                    \n
                                                    12:00-13:20: Лекц. Безопастность жизнедеятельности Клуб / Лекц. Алгебра, Попов А.М., 398 
                                                    \n
                                                    13:30-14:50: Обед
                                                    \n
                                                    15:00-16:20: Пр. БЖД 258 / Пр. Алгебра 258
                                                    \n
                                                    16:30-17:50:
                                                    \n
                                                    17:50-19:20:
                                                    \n
                                                    19:30-20:50: '''.replace('    ', ''))

        elif (last_chat_text.lower() in pairs1 and datetime.datetime.today().weekday() == 5) or (last_chat_text.lower() in pairs1Tommorow and datetime.datetime.today().weekday() == 4) or last_chat_text.lower() == 'суббота1':
            greet_bot.send_message(last_chat_id, 'Saturday pairs')

        elif (last_chat_text.lower() in pairs1 and datetime.datetime.today().weekday() == 6) or (last_chat_text.lower() in pairs1Tommorow and datetime.datetime.today().weekday() == 5) or last_chat_text.lower() == 'воскресенье1':
            greet_bot.send_message(last_chat_id, 'Sunday pairs')

        elif (last_chat_text.lower() in pairs2 and datetime.datetime.today().weekday() == 0) or (last_chat_text.lower() in pairs1Tommorow and datetime.datetime.today().weekday() == 6) or last_chat_text.lower() == 'понедельник2':
            greet_bot.send_message(last_chat_id, '''Понедельник (2):
                                                    \n
                                                    09:00-10:20: 
                                                    \n
                                                    10:30-11:50: Лекц. Математический анализ, Марченко В.В., 398
                                                    \n
                                                    12:00-13:20: Лекц. Алгебра, Попов А.М., 399
                                                    \n
                                                    13:30-14:50: Обед
                                                    \n
                                                    15:00-16:20: Пр. Иностранный язык 475 / Русский язык 402
                                                    \n
                                                    16:30-17:50: Пр. Иностранный язык 475 / Русский язык 402 / ДПО "Модуль переводчика 475"
                                                    \n
                                                    17:50-19:20: ДПО "Модуль переводчика" 475
                                                    \n
                                                    19:30-20:50: '''.replace('    ', ''))

        elif (last_chat_text.lower() in pairs2 and datetime.datetime.today().weekday() == 1) or (last_chat_text.lower() in pairs1Tommorow and datetime.datetime.today().weekday() == 0) or last_chat_text.lower() == 'вторник2':
            greet_bot.send_message(last_chat_id, '''Вторник (2)
                                                    \n
                                                    09:00-10:20: Пр. Математический анализ, 261
                                                    \n
                                                    10:30-11:50: Пр. Основы риторики и коммуникации, 473
                                                    \n
                                                    12:00-13:20: Обед
                                                    \n
                                                    13:30-14:50: ФОК Мальченко А.Д.
                                                    \n
                                                    15:00-16:20: 
                                                    \n
                                                    16:30-17:50: 
                                                    \n
                                                    17:50-19:20: 
                                                    \n
                                                    19:30-20:50: '''.replace('    ', ''))
да 
        elif (last_chat_text.lower() in pairs2 and datetime.datetime.today().weekday() == 2) or (last_chat_text.lower() in pairs1Tommorow and datetime.datetime.today().weekday() == 1) or last_chat_text.lower() == 'среда2':
            greet_bot.send_message(last_chat_id, '''Среда (2)
                                                    \n
                                                    09:00-10:20: 
                                                    \n
                                                    10:30-11:50: Пр. Аналитическая геометрия, 256
                                                    \n
                                                    12:00-13:20: Лекц. Аналитическая геометрия, Гольдман М.Л., 260
                                                    \n
                                                    13:30-14:50: Обед
                                                    \n
                                                    15:00-16:20: 
                                                    \n
                                                    16:30-17:50: 
                                                    \n
                                                    17:50-19:20: 
                                                    \n
                                                    19:30-20:50: '''.replace('    ', ''))

        elif (last_chat_text.lower() in pairs2 and datetime.datetime.today().weekday() == 3) or (last_chat_text.lower() in pairs1Tommorow and datetime.datetime.today().weekday() == 2) or last_chat_text.lower() == 'четверг2':
            greet_bot.send_message(last_chat_id, '''Четверг (2)
                                                    \n
                                                    09:00-10:20: Пр. Математический анализ, 400
                                                    \n
                                                    10:30-11:50: Лекц. Компьютерные науки и технологии программирования, Аносова Н.П., 398
                                                    \n
                                                    12:00-13:20: Обед
                                                    \n
                                                    13:30-14:50: Лаб Комп. науки и техн. прогр. ДК-1
                                                    \n
                                                    15:00-16:20: Пр. Алгебра, 473
                                                    \n
                                                    16:30-17:50: 
                                                    \n
                                                    17:50-19:20:
                                                    \n
                                                    19:30-20:50: '''.replace('    ', ''))

        elif (last_chat_text.lower() in pairs2 and datetime.datetime.today().weekday() == 4) or (last_chat_text.lower() in pairs1Tommorow and datetime.datetime.today().weekday() == 3) or last_chat_text.lower() == 'пятница2':
            greet_bot.send_message(last_chat_id, '''Пятница (2)
                                                    \n
                                                    09:00-10:20:
                                                    \n
                                                    10:30-11:50: Лекц. Математический анализ, Марченко В.В., 261
                                                    \n
                                                    12:00-13:20: Лекц. Безопастность жизнедеятельности Клуб / Лекц. Алгебра, Попов А.М., 398
                                                    \n
                                                    13:30-14:50: Пр. БЖД 471 / Пр. Алгебра 471
                                                    \n
                                                    15:00-16:20: Обед
                                                    \n
                                                    16:30-17:50: 
                                                    \n
                                                    17:50-19:20: 
                                                    \n
                                                    19:30-20:50: '''.replace('    ', ''))

        elif (last_chat_text.lower() in pairs2 and datetime.datetime.today().weekday() == 5) or (last_chat_text.lower() in pairs1Tommorow and datetime.datetime.today().weekday() == 4)  or last_chat_text.lower() == 'суббота2':
            greet_bot.send_message(last_chat_id, 'Saturday pairs')

        elif (last_chat_text.lower() in pairs2 and datetime.datetime.today().weekday() == 6) or (last_chat_text.lower() in pairs1Tommorow and datetime.datetime.today().weekday() == 5) or last_chat_text.lower() == 'воскресенье2':
            greet_bot.send_message(last_chat_id, 'Sunday pairs')


        '''
        elif last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
            today += 1
        '''
        new_offset = last_update_id + 1
        
if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
