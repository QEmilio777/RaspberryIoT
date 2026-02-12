import RPi.GPIO as GPIO
from time import sleep
import MCP3008_simple as MCP3008

# photores_pin = 40

GPIO.setmode(GPIO.BOARD)
# GPIO.setup(photores_pin, GPIO.INPUT)

try:
    while True:
        photoval = MCP3008.getResult(0, 12)
        print(photoval)
        sleep(.1)
    

except KeyboardInterrupt:
    GPIO.cleanup()
    print("gpio pins ready to go")