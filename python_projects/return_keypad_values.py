import RPi.GPIO as GPIO
from keypad_memory import Keypad

keypad = Keypad(trigger="D")

keypad.begin()

keypad_read = keypad.return_values()
print(keypad_read)
GPIO.cleanup()
print("GPIO pins ready to go")
