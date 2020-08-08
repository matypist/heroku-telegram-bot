# -*- coding: utf-8 -*-
import requests
import redis

testoOriginale=Hook['params']['message']['text']
idChat=Hook['params']['message']['chat']['id']
URL='https://api.telegram.org/bot' + Hook['env']['token_ripeti'] + '/sendMessage'
req=requests.get(URL,verify=False,data={'chat_id':idChat,'text':testoOriginale})
