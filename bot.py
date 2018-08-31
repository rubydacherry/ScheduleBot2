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
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_update_id = last_update['update_id']

        '''
        last_chat_name = last_update['message']['chat']['first_name']
        last_chat_name = 'кто-то'
        '''

        if last_chat_text.lower() in pairs1 and datetime.datetime.today().weekday() == 0:
            greet_bot.send_message(last_chat_id, 'Monday pairs')

        elif last_chat_text.lower() in pairs1 and datetime.datetime.today().weekday() == 1:
            greet_bot.send_message(last_chat_id, 'Tuesday pairs')

        elif last_chat_text.lower() in pairs1 and datetime.datetime.today().weekday() == 2:
            greet_bot.send_message(last_chat_id, 'Wednesday pairs')

        elif last_chat_text.lower() in pairs1 and datetime.datetime.today().weekday() == 3:
            greet_bot.send_message(last_chat_id, 'Thursday pairs')

        elif last_chat_text.lower() in pairs1 and datetime.datetime.today().weekday() == 4:
            greet_bot.send_message(last_chat_id, 'Friday pairs')

        elif last_chat_text.lower() in pairs1 and datetime.datetime.today().weekday() == 5:
            greet_bot.send_message(last_chat_id, 'Saturday pairs')

        elif last_chat_text.lower() in pairs1 and datetime.datetime.today().weekday() == 6:
            greet_bot.send_message(last_chat_id, 'Sunday pairs')

        elif last_chat_text.lower() in pairs2 and datetime.datetime.today().weekday() == 0:
            greet_bot.send_message(last_chat_id, 'Monday pairs')

        elif last_chat_text.lower() in pairs2 and datetime.datetime.today().weekday() == 1:
            greet_bot.send_message(last_chat_id, 'Tuesday pairs')

        elif last_chat_text.lower() in pairs2 and datetime.datetime.today().weekday() == 2:
            greet_bot.send_message(last_chat_id, 'Wednesday pairs')

        elif last_chat_text.lower() in pairs2 and datetime.datetime.today().weekday() == 3:
            greet_bot.send_message(last_chat_id, 'Thursday pairs')

        elif last_chat_text.lower() in pairs2 and datetime.datetime.today().weekday() == 4:
            greet_bot.send_message(last_chat_id, 'Friday pairs')

        elif last_chat_text.lower() in pairs2 and datetime.datetime.today().weekday() == 5:
            greet_bot.send_message(last_chat_id, 'Saturday pairs')

        elif last_chat_text.lower() in pairs2 and datetime.datetime.today().weekday() == 6:
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
