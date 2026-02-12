import RPi.GPIO as GPIO
from time import sleep

buzz_pin = 40
GPIO.setmode(GPIO.BOARD)

GPIO.setup(buzz_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(buzz_pin, 1)
        print('estoy alto')
        sleep(1)
        GPIO.output(buzz_pin, 0)
        print('estoy bajo')
        sleep(5)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('--GPIO pins ready to go')
