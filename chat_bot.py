#!/usr/bin/env python3

from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
import os

"""rudimentary chatbot which will reply with text based off of its dataset
will respond more accurately the more it is trained"""
botty = ChatBot('BottyMcFace')

trainer = ChatterBotCorpusTrainer(botty)
resp = botty.get_response('How can I help?')


def response(resp):
	"""responses from the bot based off of the nltk_data"""
	while True:
		user = input('user: ')
		if user == 'bye' or user == 'Bye':
			break
		if user != 'bye' or user != 'Bye':
			reply = botty.get_response(user)
			print('#' * 10)
			print('bot reply: ', reply)


if __name__ == '__main__':
	response(resp)
