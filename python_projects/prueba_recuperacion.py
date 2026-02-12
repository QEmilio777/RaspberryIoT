import RPi.GPIO as GPIO
from time import sleep

buzz_pin = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzz_pin, GPIO.OUT)


try:
    while True:
        GPIO.output(buzz_pin, True)
        sleep(2)
        GPIO.output(buzz_pin, False)
        sleep(1)
        GPIO.output(buzz_pin, True)
        sleep(5)
        GPIO.output(buzz_pin, False)
        sleep(2)
   
except KeyboardInterrupt:
    GPIO.cleanup()
    print("gpio pins ready to go")