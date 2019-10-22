# This Python file uses the following encoding: utf-8
import RPi.GPIO as GPIO    #Importamos la librería GPIO
import time                #Importamos time (time.sleep)
GPIO.setmode(GPIO.BCM)     #Ponemos la placa en modo BCM
salida = 21          #Usamos el pin GPIO 21 como TRIGGER
entrada = 26           #Usamos el pin GPIO 26 como ECHO
led = 12
GPIO.setup(led,GPIO.OUT)#salida para el led
GPIO.setup(salida,GPIO.OUT)  #Configuramos Trigger como salida
GPIO.setup(entrada,GPIO.IN)      #Configuramos Echo como entrada
GPIO.output(salida,False)    #Ponemos el pin 25 como LOW


try:
    while True:     #Iniciamos un loop infinito
        GPIO.output(salida,True)   #Enviamos un pulso de ultrasonidos
        time.sleep(0.00001)              #Una pequeñña pausa

        GPIO.output(salida,False)  #Apagamos el pulso
        start = time.time()              #Guarda el tiempo actual mediante time.time()

        while GPIO.input(entrada)==0:  #Mientras el sensor no reciba señal...
            start = time.time()          #Mantenemos el tiempo actual mediante time.time()
        while GPIO.input(entrada)==1:  #Si el sensor recibe señal...
            stop = time.time()           #Guarda el tiempo actual mediante time.time() en otra variable

        elapsed = stop-start             #Obtenemos el tiempo transcurrido entre envío y recepción
        distance = (elapsed * 34300)/2   #Distancia es igual a tiempo por velocidad partido por 2   D = (T x V)/2
        print distance                   #Devolvemos la distancia (en centímetros) por pantalla
        if distance < 9:
            print ('warning hay algo...')
            GPIO.output(led,GPIO.HIGH)
        elif distance > 10:
            GPIO.output(led,GPIO.LOW)
        
        #aqui inicio el contador de tiempo
        tie = time.localtime()
        minuto = tie[5]
        #print (minuto)
        if minuto == 45:
            GPIO.cleanup() 
            break
        time.sleep(1)                    #Pequeña pausa para no saturar el procesador de la Raspberry
except KeyboardInterrupt:                #Si el usuario pulsa CONTROL+C...
    print "quit"                         #Avisamos del cierre al usuario
    GPIO.cleanup()                       #Limpiamos los pines GPIO y salimos
