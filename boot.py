import sys
import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop
import os


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command
        
    
    if command == 'Cerrar':
        os.system('python abrir.py')
        bot.sendMessage(chat_id, str('se cerro la puerta c:'))
    elif command == 'Funciones':
        bot.sendMessage(chat_id, str('hola soy un bot, me llamo RapBot' ))
        bot.sendMessage(chat_id, str('puedo ayudarte en distintas funciones, solo teclea la que desees' ))
        bot.sendMessage(chat_id, str('Abrir Puerta = Abrir' ))
        bot.sendMessage(chat_id, str('Cerrar Puerta = Cerrar' ))
        bot.sendMessage(chat_id, str('Activar sensor ultrasonico = Alarma' ))
        bot.sendMessage(chat_id, str('Encender Led = Led-on'))
        bot.sendMessage(chat_id, str('Apagar LEd = Led-off' ))
        bot.sendMessage(chat_id, str('Fecha y hora actual = Time' ))
    elif command == 'Abrir':
        os.system('python cerrar.py')
        bot.sendMessage(chat_id, str('se abrio la puerta :c'))
    elif command == 'Alarma':
        bot.sendMessage(chat_id, str('La alarma esta encendida'))
        os.system('python sonico1.py')
        bot.sendMessage(chat_id, str('La alarma ese apago'))
    elif command == 'Led-on':
        os.system('python led.py')
        bot.sendMessage(chat_id, str('Led encendido'))
    elif command == 'Party':
        bot.sendMessage(chat_id, str('Inicia el luz estrobo'))
        os.system('python estrobo.py')
        bot.sendMessage(chat_id, str('Se acabo luz estrobo'))
    elif command == 'Led-off':
        os.system('python led-off.py')
        bot.sendMessage(chat_id, str('Led Apagado'))
    elif command == 'Time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == 'Bai':
        bot.sendMessage(chat_id, str('Adios popo '))
    else:
	bot.sendMessage(chat_id, str('escribiste mal la peticion sorry :)'))
    



bot = telepot.Bot('717919448:AAE3qOLh2B5KQHsK5s_NTzhqhZPscx4oQwM')

MessageLoop(bot, handle).run_as_thread()

print 'Hazme una peticion...'
while 1:
    time.sleep(10)
