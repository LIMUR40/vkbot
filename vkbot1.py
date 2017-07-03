# -*- coding: utf-8 -*-
import time
import vk_api
vk = vk_api.VkApi(login = 'KING-007@mail.ru', password = 'Rattlytullip42')
vk_api.VkApi(token = 'c8190a69d9cc045f5a59c9c13780e6288b3937ea445c694e4e4f6c60186e5e4e966d6c9c4a91cb9c0c6b8') #Авторизоваться как сообщество
vk.auth()
values = {'out': 0,'count': 100,'time_offset': 60}

def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})

while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
            write_msg(item[u'user_id'],u'Привет, Хабр!')
    time.sleep(1)