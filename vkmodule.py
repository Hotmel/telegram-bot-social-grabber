# -*- coding: utf-8 -*-
import config, pgmodule, requests, json

## 
# \file 
# \brief Модуль для работы с социальной сетью ВКонтакте
# \authors Борис Бочкарев http://vk.com/id23382988
# \version 0.2

## 
# Метод генерации ссылки для авторизации в ВК
# \param chat_id ID чата из Telegram
# \return Ссылку для авторизации в текстовом виде
def vkauthstr(chat_id):
	textMsg = '''Для авторизации в ВК вам необходимо пройти по ссылке:\n\n
	https://oauth.vk.com/authorize?client_id=5558925&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,messages&response_type=token&v=5.53\n\n
	и отправить итоговую ссылку мне'''
	return textMsg

## 
# Метод для получения списка друзей
# \param token Токен, полученные от VK.API
# \return Список всех друзей со списками вида: [id_пользователя,Фамилия,Имя]
def vkfriends(token):
	response = requests.get("https://api.vk.com/method/friends.get?access_token="+str(token)+"&offset=0&order=name&fields=[name]&name_case=nom")
	arrayResp = json.loads(response.content.decode("UTF-8"))["response"]
	friends = []
	for friend in arrayResp:
		localArray = [friend["uid"],friend["first_name"],friend["last_name"]]
		friends.append(localArray)
	return friends 

## 
# Метод для получения записей со стены пользователей
# \param user_id ID пользователя в ВК
# \return Список из 100 записей со стены пользователя со списками вида: [id_автора,текст_записи]
def vkwall(user_id):
	response = requests.get("https://api.vk.com/method/wall.get?offset=0&owner_id="+str(user_id)+"&count=100&filter=owner")
	arrayResp = json.loads(response.content.decode("UTF-8"))["response"]
	wall = []
	for item in arrayResp:
		if type(item) != int and str(item["text"]) != "":
			wall.append([item["from_id"],item["text"]])
	return wall

##
# Метод для получения новых сообщений
# \param token Токен для ВК
# \return Список из новых сообщений вида [id_пользователя/диалога, сообщение]
def vknewmsg(token): # TODO: получение нескольких сообщений от пользователя
	response = requests.get("https://api.vk.com/method/messages.getDialogs?offset=0&count=200&access_token="+str(token))
	arrayResp = json.loads(response.content.decode("UTF-8"))["response"]
	msgs = []
	for item in arrayResp: # TODO: сделать анализ репостов
		if type(item) != int and item["read_state"] == 0 and item["out"] == 0:
			msgs.append([item["uid"],item["body"]])
	return msgs

##
# Метод для получения Ф.И.
# \param id ID пользователя в ВК
# \return Строка вида "Фамилия Имя"
def vkfio(id):
	response = requests.get("https://api.vk.com/method/users.get?user_ids="+str(id)+"&name_case=Nom")
	arrayResp = json.loads(response.content.decode("UTF-8"))["response"]
	return arrayResp[0]['last_name'] + " " + arrayResp[0]['first_name']

##
# Метод для отправки сообщения
# \param id ID пользователя в ВК
# \param text Текст сообщения
# \param token Токен пользователя, от которого будет отправлено сообщение
def vksend(id,text,token):
	requests.get("https://api.vk.com/method/messages.send?user_id="+str(id)+"&message="+str(text)+"&access_token="+str(token))