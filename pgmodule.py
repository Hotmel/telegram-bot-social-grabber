# -*- coding: utf-8 -*-
import psycopg2,sys,config

## 
# \file 
# \brief Модуль для работы с базой данных PostgreSQL
# \authors Борис Бочкарев http://vk.com/id23382988
# \version 0.2

## 
# Метод для получения токена
# \param id_chat ID чата из Telegram
# \param social Социальная сеть, например 'vk'
# \return Токен для данной социальной сети данного чата
def getToken(id_chat, social):
	if social == 'vk':
		connect = psycopg2.connect(user=config.userDB, password=config.passwordDB, host='127.0.0.1', database='socialcollector', port=5432)
		cursor = connect.cursor()
		cursor.execute("SELECT token FROM users WHERE id_chat = '"+str(id_chat)+"'")
		result = cursor.fetchone()[0]
		connect.close()
		return result
	else:
		return 'error'

##
# Метод для обновления токена
# \param id_chat ID чата из Telegram
# \param token Новый Токен
def updateToken(id_chat, token):
	connect = psycopg2.connect(user=config.userDB, password=config.passwordDB, host='127.0.0.1', database='socialcollector', port=5432)
	cursor = connect.cursor()
	cursor.execute("UPDATE users SET token = '"+str(token)+"' WHERE id_chat = '"+str(id_chat)+"'")
	connect.commit()
	connect.close()

##
# Метод для сохранения ID того, кому собираемся отвечать
# \param id_chat ID чата из Telegram
# \param id ID пользователя, кому будем отвечать
def saveID(id_chat,id):
	connect = psycopg2.connect(user=config.userDB, password=config.passwordDB, host='127.0.0.1', database='socialcollector', port=5432)
	cursor = connect.cursor()
	cursor.execute("INSERT INTO answer(id_chat,id_user) VALUES('"+str(id_chat)+"','"+str(id)+"')")
	connect.commit()
	connect.close()

##
# Метод для удаления ID того, кому отвечали
# \param id_chat ID чата из Telegram
# \param id ID пользователя, кому будем отвечать
def delID(id_chat,id):
	connect = psycopg2.connect(user=config.userDB, password=config.passwordDB, host='127.0.0.1', database='socialcollector', port=5432)
	cursor = connect.cursor()
	cursor.execute("DELETE FROM answer WHERE id_chat = '"+str(id_chat)+"' AND id_user = '"+str(id)+"'")
	connect.commit()
	connect.close()	

##
# Метод для получения ID того, кому отвечаем
# \param id_chat ID чата из Telegram
# \return ID того, кому отвечаем
def getID(id_chat):
	connect = psycopg2.connect(user=config.userDB, password=config.passwordDB, host='127.0.0.1', database='socialcollector', port=5432)
	cursor = connect.cursor()
	cursor.execute("SELECT id_user FROM answer WHERE id_chat = '"+str(id_chat)+"'")
	result = cursor.fetchone()[0]
	connect.close()
	return result
