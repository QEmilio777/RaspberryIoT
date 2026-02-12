import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)

output_led = 38
GPIO.setup(output_led, GPIO.OUT)


quit = 'n'
on = 1
off = 0
while quit != 'y':
	times = int(input('how many blinks?: '))
	for _ in range(times):
		GPIO.output(output_led, on)
		sleep(1)
		GPIO.output(output_led, off)
		sleep(1)
	quit = input('would you like to exit, Press "y". Else, any othe key'
							' to continue: ')

GPIO.cleanup()
