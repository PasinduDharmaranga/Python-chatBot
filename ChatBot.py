from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+50)
bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('E:\My chatbot\chatterbot-corpus\chatterbot_corpus\data\english/'):
	data = open('E:\My chatbot\chatterbot-corpus\chatterbot_corpus\data\english/'+ files , 'r').readlines()
	bot.train(data)

# while True:
	# message = input('You:')
	# if message.strip()!= 'Bye':
		# reply = bot.get_response(message)
		# print('ChatBot:',reply)
		# engine.say(reply)
		# engine.runAndWait()
	# if message.strip()== 'Bye':
		# print('ChatBot : Bye')
		# break
		
		
		
		
		



