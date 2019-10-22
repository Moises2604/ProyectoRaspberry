import RPi.GPIO as GPIO # Importar libreria de GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)

for i in range (0,25):                           

	GPIO.output(17,GPIO.HIGH)
	time.sleep(0.2)
	GPIO.output(17,GPIO.LOW)
	time.sleep(0.2)

GPIO.cleanup()
