# This Python file uses the following encoding: utf-8
import os, sys
import os, sys
import RPi.GPIO as GPIO # Importar libreria de GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
p=GPIO.PWM(13,50)
p.start(7.5)
p.ChangeDutyCycle(14.5)#180º
time.sleep(1)
GPIO.cleanup()
