# Fehca: 07 de febrero de 2026
# Autor: Manuel Quezada
# Descripción: Programa para indicar la potencia de un motor CD
# ENA = pin 21; IN1 = pin 26; IN2 = pin 19

import RPi.GPIO as GPIO
from time import sleep

# Definicion de Pines

ENA = 21
IN1 = 26
IN2 = 19

#Nomenclatura a utilizar
GPIO.setmode(GPIO.BCM)

#Habilitar pines en salida
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

#Definiendo el valor de salida
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)

#Habilitar PWM a 1Khz
pwm = GPIO.PWM(ENA, 1000)
pwm.start(0)

print("Programa para control de un motor CD")
print("Para salir del programa presione Ctrl + x")
try:
    while True:
        print("Ingresa la potencia con un entero entre 1 - 100")
        valor = input("")
        
        if not valor.isdigit():
            print("Entrada incorrecta")
            continue # regresa al inicio del while
        
        potencia  = int(valor)
        
        if 0 <= potencia <= 100:
            pwm.ChangeDutyCycle(potencia)
            GPIO.output(IN1, GPIO.LOW)
            GPIO.output(IN2, GPIO.HIGH)
            print(f"La potencia ingresada es: {potencia}")
        else:
            print("Potencia fuera de los limites")
        
        sleep(0.1)
        

except KeyboardInterrupt:
    print("Fin del programa\n")
    
finally:
    sleep(0.1)
    print("Finally ejecutado")
    pwm.stop()
    del pwm
    GPIO.cleanup()