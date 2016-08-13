# -*- coding: utf-8 -*-
import psycopg2,sys,config

## Модуль с методами для работы с БД PostgreSQL

## Метод для получения токена
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