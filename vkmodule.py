# -*- coding: utf-8 -*-
import config, pgmodule, requests, json

## 
# \file 
# \brief Модуль для работы с социальной сетью ВКонтакте
# \authors Борис Бочкарев http://vk.com/id23382988
# \version 0.1

## 
# Метод генерации ссылки для авторизации в ВК
# \param chat_id ID чата из Telegram
# \return Ссылку для авторизации в текстовом виде
def vkauthstr(chat_id):
	textMsg = '''Для авторизации в ВК вам необходимо пройти по ссылке:\n
	http://oauth.vk.com/authorize?client_id='''+str(config.idAppVK)+'''&scope=friends&redirect_uri=http://y909539n.bget.ru/vkauth.php&display=mobile&response_type=token&state='''+str(chat_id)
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