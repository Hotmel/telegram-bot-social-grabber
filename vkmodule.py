# -*- coding: utf-8 -*-
import config, pgmodule, requests, json

## Класс для работы с соц.сетью ВК

## метод генерации ссылки для авторизации в ВК
def vkauthstr(chat_id):
	textMsg = '''Для авторизации в ВК вам необходимо пройти по ссылке:\n
	http://oauth.vk.com/authorize?client_id='''+str(config.idAppVK)+'''&scope=friends&redirect_uri=http://y909539n.bget.ru/vkauth.php&display=mobile&response_type=token&state='''+str(chat_id)
	return textMsg

## метод для получения списка друзей
def vkfriends(token):
	response = requests.get("https://api.vk.com/method/friends.get?access_token="+str(token)+"&offset=0&order=name&fields=[name]&name_case=nom")
	arrayResp = json.loads(response.content.decode("UTF-8"))["response"]
	friends = []
	for friend in arrayResp:
		localArray = [friend["uid"],friend["first_name"],friend["last_name"]]
		friends.append(localArray)
	return friends # возвращает список всех друзей со списками вида: id_пользователя,Фамилия,Имя

## метод для получения записей со стены пользователей
def vkwall(user_id):
	response = requests.get("https://api.vk.com/method/wall.get?offset=0&owner_id="+str(user_id)+"&count=100&filter=owner")
	arrayResp = json.loads(response.content.decode("UTF-8"))["response"]
	wall = []
	for item in arrayResp:
		if type(item) != int and str(item["text"]) != "":
			wall.append([item["from_id"],item["text"]])
	return wall # возвращает список 100 записей со стены пользователя со списками вида: id_автора,текст_записи