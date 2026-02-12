import RPi.GPIO as GPIO
import MCP3008_simple as MCP3008
from time import sleep

GPIO.setmode(GPIO.BOARD)

try:
    while True:
        lighval = MCP3008.getResult(1, 10)
        print(f"ligh value: {lighval}")
        sleep(0.2)

except KeyboardInterrupt:
    sleep(0.1)
    GPIO.cleanup()
    print('GPIO pins ready to go')