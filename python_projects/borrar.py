import MCP3008_simple as MCP
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.OUT)

pwm = GPIO.PWM(40, 1000)
pwm.start(0)

try:
    while True:
        val = MCP.getResult(0, 10)
        dc = (100/1023) * val
        if dc > 99:
            dc = 99
        pwm.ChangeDutyCycle(dc)
        print(f"pot: {val}")
        print(f"led: {dc}")
        sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('pins ready to go')