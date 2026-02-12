import RPi.GPIO as GPIO
import MCP3008_simple as MCP_3008
from time import sleep

pir_pin = 40
buzz_pin = 38

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pir_pin, GPIO.IN)
GPIO.setup(buzz_pin, GPIO.OUT)

sleep(15)
print("start")

try:
    while True:
        pir_val = GPIO.input(pir_pin)
        photo_val = MCP_3008.getResult(0, 12)
        
        if pir_val == 1 and photo_val < 1500:
            print("detecting something")
            GPIO.output(buzz_pin, True)
            sleep(5)
            GPIO.output(buzz_pin, False)
            sleep(2)
            GPIO.output(buzz_pin, True)
            sleep(5)
            GPIO.output(buzz_pin, False)
            sleep(2)
        else:
            GPIO.output(buzz_pin, False)
        
        GPIO.output(buzz_pin, False)
        sleep(.2)
        

except KeyboardInterrupt:
    GPIO.cleanup()
    print("gpio pins ready to go")


