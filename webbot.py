from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from bs4 import BeautifulSoup
import requests
import time
import telegram
from telegram.error import BadRequest, RetryAfter, TimedOut, Unauthorized, NetworkError
import os

def checkwebsite():
    url = "http://m.orange.es/tienda/objetos-conectados/smart-tv/lg/televisor-49-uj620v-negro-km0/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    if str(soup).find("agotado temporalmente") ==-1:
       return True
    return False



def main():
    TOKEN=os.environ['token_bot']
    chatid=os.environ['chat_id']
    bot = telegram.Bot(token=TOKEN)

    while True:
        if checkwebsite():
            try:
                bot.send_message(chat_id=chatid,text="Es posible que haya stock de la TV LG 49")
            except Exception as e:
                time.sleep(20)

        time.sleep(200)
        

if __name__ == '__main__':
    main()