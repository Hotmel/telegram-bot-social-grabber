# -*- coding: utf-8 -*-
import config, telebot
from telebot import types
import vkmodule
import pgmodule

## 
# \file 
# \brief Пример бота для работы с сообщениями из ВК
# \authors Борис Бочкарев http://vk.com/id23382988
# \version 0.1

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def start(message):
	keys = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
	keys.add("Авторизация в ВК")
	keys.add("Получить новые сообщения из ВК")
	bot.send_message(message.chat.id, "Ваш выбор?", reply_markup=keys)

@bot.message_handler(content_types=["text"])
def sendmessage(message):
	if message.text == "Авторизация в ВК":
		bot.send_message(message.chat.id, vkmodule.vkauthstr(message.chat.id))
	elif message.text == "Получить новые сообщения из ВК":
		# запрашиваем все сообщения -в_цикле- получаем фио пользователя - вормируем сообщение и отправляем
		msgList = vkmodule.vknewmsg(pgmodule.getToken(message.chat.id,"vk"))
		keys = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
		for msg in msgList:
			uid,body = msg[0],msg[1]
			fio = vkmodule.vkfio(uid)
			Msg = fio + "\n" + body
			bot.send_message(message.chat.id, Msg)
			keys.add("ID: "+str(uid)+" | "+fio)
		bot.send_message(message.chat.id, "Кому ответить?", reply_markup=keys)
	elif message.text.find("https://oauth.vk.com/blank.html") != -1: # если пришла ссылка с авторизацией
		token = message.text.split("#")[1].split("&")[0].split("=")[1]
		print(token)
		pgmodule.updateToken(message.chat.id,token)
		bot.send_message(message.chat.id, "Авторизация в ВК прошла успешно!")
		# клавиатура с меню
		keys = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
		keys.add("Авторизация в ВК")
		keys.add("Получить новые сообщения из ВК")
		bot.send_message(message.chat.id, "Ваш выбор?", reply_markup=keys)
	elif message.text.find("ID: ") != -1 and message.text.find(" | ") != -1:
		Id = message.text.split(" ")[1]
		pgmodule.saveID(message.chat.id,Id)
	else: 
		user_id = pgmodule.getID(message.chat.id)
		pgmodule.delID(message.chat.id,user_id)
		vkmodule.vksend(user_id,message.text,pgmodule.getToken(message.chat.id,'vk'))
		# клавиатура с меню
		keys = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
		keys.add("Авторизация в ВК")
		keys.add("Получить новые сообщения из ВК")
		bot.send_message(message.chat.id, "Ваш выбор?", reply_markup=keys)

if __name__ == '__main__':
	bot.polling(none_stop=True)