from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import requests
import speech_recognition as sr

def chatbot():
	r = sr.Recognizer()

	api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

	engine = pyttsx3.init()
	rate = engine.getProperty('rate')
	engine.setProperty('rate', 130)
	engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

	bot = ChatBot('Bot')
	bot.set_trainer(ListTrainer)
	try:
		
		mic=sr.Microphone()
		with mic as source:
			audio=r.listen(source)
		message=r.recognize_google(audio)
		#message = input('You:')
		print ('You:'+message)
		if message.strip()!= 'Bye':
			word_list = message.split()
			if "weather" in message:
				city = word_list[-1]
				url = api_address + city
				json_data = requests.get(url).json()
				formatted_data = json_data['weather'][0]['description']
				reply = formatted_data
			else:
				reply = bot.get_response(message)
			print('Jessica:',reply)
			engine.say(reply)
			engine.runAndWait()
			# if message.strip()== 'Bye':
				# print('Jessica : Bye')
				# break
	except sr.UnknownValueError:

		engine.runAndWait()
		print("Hey there are you with me..")
while True:
	chatbot()