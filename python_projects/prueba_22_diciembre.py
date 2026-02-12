import RPi.GPIO as GPIO
import time

pin_switch = 40
pin_switch_val = 0
up_pin_switch_val = 0
pin_led = 38
prev_state = 0
switch = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin_led, GPIO.OUT)

try:
    while True:
        up_pin_switch_val = pin_switch_val
        
        if up_pin_switch_val == 1 and prev_state == 0:
            switch = not switch
        
        if switch:
            GPIO.output(pin_led, True)
        if switch == False:
            GPIO.output(pin_led, False)
        
        pin_switch_val = GPIO.input(pin_switch)
            
        prev_state = up_pin_switch_val
        time.sleep(0.1)
    
except KeyboardInterrupt:
    time.sleep(0.1)
    GPIO.cleanup()
    print("GPIO ready to go")