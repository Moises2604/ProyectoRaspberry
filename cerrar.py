#-*-coding:utf-8-*-
import RPi.GPIO as GPIO # Importar libreria de GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(13,GPIO.OUT)

p=GPIO.PWM(13,50)
p.start(7.5)



p.ChangeDutyCycle(4.0)#0º
time.sleep(1)
GPIO.cleanup()
