import RPi.GPIO as GPIO
from time import sleep
import time

GPIO.setmode(GPIO.BOARD)

echo_pin = 40
trig_pin = 38

GPIO.setup(echo_pin, GPIO.IN)
GPIO.setup(trig_pin, GPIO.OUT)


try:
    while True:
        GPIO.output(trig_pin, 0)
        sleep(2E-6)
        GPIO.output(trig_pin, 1)
        sleep(10E-6)
        GPIO.output(trig_pin, 0)
        while GPIO.input(echo_pin) == 0:
            pass
        start = time.time()
        while GPIO.input(echo_pin) == 1:
            pass
        end = time.time()
        travel_time = end-start
        
        print(f"total time in : {travel_time:.6f} segundos")
        sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('gpio pins ready to go')

            