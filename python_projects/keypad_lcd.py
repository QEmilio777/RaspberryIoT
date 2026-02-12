import RPi.GPIO as GPIO
from time import sleep
import LCD1602 as lcd
from keypad_memory import Keypad

lcd.init(0x27, 1)

keypad = Keypad()
keypad.begin()

trigger = True

password = ["1", "C", "9", "5", "B"]


try:
    while trigger:
        lcd.write(0, 0, "Enter values: ")
        values = keypad.return_values()
        lcd.clear()
        lcd.write(0, 0, "Values entered: ")
        lcd.write(0, 1, values)
        sleep(5)
        values = list(values)
        if values == password:
            print("correcto")
            lcd.clear()
            lcd.write(0, 0, "Correcto")
            sleep(4)
            trigger = False
        else:
            print("incorrecto")
        lcd.clear()


except KeyboardInterrupt:
    sleep(0.1)
    lcd.clear()
    GPIO.cleanup()
    print("GPIO pins ready to go")

finally:
    sleep(0.1)
    lcd.clear()
    GPIO.cleanup()
    print("GPIO pins ready to go")