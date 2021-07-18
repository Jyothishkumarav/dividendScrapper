import json
import urllib

import requests

telgramToken = '1912863077:AAGH-iVztSPAw5K117Us-GKEx9pj-j3GUzw'
telefframDividendChatId = '-586722077'
URL = "https://api.telegram.org/bot{}/".format(telgramToken)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def send_message(text):
    payload = dict()
    payload['text'] = text
    payload['chat_id'] = telefframDividendChatId
    params = urllib.parse.urlencode(payload, quote_via=urllib.parse.quote)
    url = URL + "sendMessage"
    response = requests.get(url, params=params)
    print(response)
    #get_url(url)

