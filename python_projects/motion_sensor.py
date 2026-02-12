import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

motion_pin = 40
red_pin = 38
green_pin = 36

GPIO.setup(motion_pin, GPIO.IN)
GPIO.setup(red_pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(green_pin, GPIO.OUT, initial=GPIO.LOW)

sleep(20)

try:
    while True:
        read_motion = GPIO.input(motion_pin)
        if read_motion == 1:
            GPIO.output(green_pin, 0)
            GPIO.output(red_pin, 1)
        if read_motion == 0:
            GPIO.output(green_pin, 1)
            GPIO.output(red_pin, 0)
            
        print(read_motion)
        sleep(0.1)
        

except KeyboardInterrupt:
    GPIO.cleanup()
    print('--gpio pins ready to go')