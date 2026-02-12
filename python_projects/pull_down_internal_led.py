import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

pin_led = 38
pin_button = 40

ON = 1
OFF = 0

GPIO.setup(pin_led, GPIO.OUT)
GPIO.setup(pin_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
try:
	while True:
		read_in = GPIO.input(pin_button)
		print(read_in)
		if read_in == 1:
			GPIO.output(pin_led, ON)
		if read_in == 0:
			GPIO.output(pin_led, OFF)

		sleep(0.1)

except KeyboardInterrupt:
	GPIO.cleanup()
	print('--GPIO pins ready to go')
