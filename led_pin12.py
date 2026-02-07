import RPi.GPIO as GPIO # libreria de los puertos digitales
import time # libreria para pausas en el código

LED_PIN = 12 # numero pin del led

GPIO.setmode(GPIO.BCM) # numeracion BCM para los pines
GPIO.setup(LED_PIN, GPIO.OUT) # el LED_PIN como salida

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH) # LED_PIN en estado alto (3.3V)
        print("Encendiendo el led") # mensaje para el usuario
        time.sleep(1) # pausa de 1 segundo
        
        GPIO.output(LED_PIN, GPIO.LOW) # LED_PIN en estado bajo (0V)
        print("Apagando el led")
        time.sleep(1)
    
except KeyboardInterrupt:
    time.sleep(0.1)
    print("Programa detenido de manera correcta\n")

finally:
    time.sleep(1)
    GPIO.cleanup() # liberar los recursos de GPIO
    print("Pines libres")
