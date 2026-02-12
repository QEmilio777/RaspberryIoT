from keypad_memory import Keypad
import RPi.GPIO as GPIO
from time import sleep

result = ""
values = []

keypad_result_val = Keypad()
keypad_result_val.begin()

try:
    while True:
        result = keypad_result_val.get_values()
        if result:
            values.append(result)
            if result == "D":
                values.pop()
                print(f"Has digitado estos valores: {values}")
                values.clear()
            print(result)


except KeyboardInterrupt:
    sleep(0.1)
    GPIO.cleanup()
    print("GPIO pins ready to go")
    