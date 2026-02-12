import RPi.GPIO as GPIO
from time import sleep

buzz_pin = 40
GPIO.setmode(GPIO.BOARD)

GPIO.setup(buzz_pin, GPIO.OUT, initial=GPIO.LOW)
mypwm_passive = GPIO.PWM(buzz_pin, 400)
mypwm_passive.start(70)

try:
    while True:
        for i in range(10, 2000, 1):
            mypwm_passive.ChangeFrequency(i)
            sleep(0.0001)
        for i in range(2000, 10, -1):
            mypwm_passive.ChangeFrequency(i)
            sleep(0.0001)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('--GPIO pins ready to go')
