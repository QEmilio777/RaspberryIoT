import RPi.GPIO as GPIO
import MCP3008_simple as MCP
from gpiozero import Servo
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory
myfactory = PiGPIOFactory()

GPIO.setmode(GPIO.BOARD)

servo_pin = 40

GPIO.setup(servo_pin, GPIO.OUT)

pwm_servo = GPIO.PWM(servo_pin, 50)
pwm_servo.start(0)


try:
    while True:
        read_pot_val = MCP.getResult(0, 10)
        
        dc = (10/1023)*read_pot_val + 2
        pwm_servo.ChangeDutyCycle(dc)
        
        print('pot_val: ', read_pot_val, 'dc_val: ', dc)
        
        sleep(0.1)

except KeyboardInterrupt:
    pwm_servo.stop()
    del pwm_servo
    GPIO.cleanup()
    print('--GPIO pins ready to go')