# -*- coding: utf-8 -*-
import requests
import redis

#           Config vars
token = os.environ['TELEGRAM_TOKEN']

testoOriginale=Hook['params']['message']['text']
idChat=Hook['params']['message']['chat']['id']
URL='https://api.telegram.org/bot' + Hook['env']['TELEGRAM_TOKEN'] + '/sendMessage'
req=requests.get(URL,verify=False,data={'chat_id':idChat,'text':testoOriginale})
