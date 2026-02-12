# import RPi.GPIO as GPIO
import MCP3008_simple as MCP
from gpiozero import Servo
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory
myfactory = PiGPIOFactory()

# GPIO.setmode(GPIO.BOARD)

servo_pin = 21
my_servo = Servo(servo_pin, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000,
                 pin_factory=myfactory)

my_servo.value = 0

# GPIO.setup(servo_pin, GPIO.OUT)

# pwm_servo = GPIO.PWM(servo_pin, 50)
# pwm_servo.start(0)


try:
    while True:
        read_pot_val = MCP.getResult(0, 10)
        
        dc = (2/1023)*read_pot_val - 1
        # pwm_servo.ChangeDutyCycle(dc)
        my_servo.value = dc
        
        print('pot_val: ', read_pot_val, 'dc_val: ', dc)
        
        sleep(0.1)

except KeyboardInterrupt:
    print('--GPIO pins ready to go')