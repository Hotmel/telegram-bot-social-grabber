# -*- coding: utf-8 -*-
import psycopg2,sys,config

## 
# \file 
# \brief Модуль для работы с базой данных PostgreSQL
# \authors Борис Бочкарев http://vk.com/id23382988
# \version 0.1

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