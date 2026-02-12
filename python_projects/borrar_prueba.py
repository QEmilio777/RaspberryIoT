import MCP3008_simple as MCP_3008
import LCD1602 as lcd
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

lcd.init(0x27, 1)

try:
    while True:
        photo_val = MCP_3008.getResult(0, 12)
        print(photo_val)
        sleep(0.5 )
    
    
except KeyboardInterrupt:
    lcd.clear()
    GPIO.cleanup()
    print("done")