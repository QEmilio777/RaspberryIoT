import RPi.GPIO as GPIO
import MCP3008_simple as MCP
from time import sleep

GPIO.setmode(GPIO.BOARD)

red_pin_out = 40
green_pin_out = 38
blue_pin_out = 36

GPIO.setup(red_pin_out, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(green_pin_out, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(blue_pin_out, GPIO.OUT, initial=GPIO.LOW)

mypwm_red = GPIO.PWM(red_pin_out, 1000)
mypwm_green = GPIO.PWM(green_pin_out, 1000)
mypwm_blue = GPIO.PWM(blue_pin_out, 1000)


mypwm_red.start(0)
mypwm_green.start(0)
mypwm_blue.start(0)

try:
    while True:
        read_red_pot = MCP.getResult(0, 10)
        read_green_pot = MCP.getResult(1, 10)
        read_blue_pot = MCP.getResult(2, 10)
        
        red_dc = (100/1023) * read_red_pot
        green_dc = (100/1023) * read_green_pot
        blue_dc = (100/1023) * read_blue_pot
        
        mypwm_red.ChangeDutyCycle(red_dc)
        mypwm_green.ChangeDutyCycle(green_dc)
        mypwm_blue.ChangeDutyCycle(blue_dc)
        
        print(f"{red_dc}, {green_dc}, {blue_dc}")
        print(f"{read_red_pot}, {read_green_pot}, {read_blue_pot}")
        
        sleep(0.1)
        
except KeyboardInterrupt:
    mypwm_red.stop()
    mypwm_green.stop()
    mypwm_blue.stop()
    
    del mypwm_red
    del mypwm_green
    del mypwm_blue
    
    GPIO.cleanup()
    print('--GPIO pins ready to go')