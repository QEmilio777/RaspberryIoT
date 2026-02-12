import RPi.GPIO as GPIO
from keypad_memory import Keypad

result = Keypad()
result.begin()
new_results = result.return_values()
print(new_results)
GPIO.cleanup()
print("Pins ready to go")