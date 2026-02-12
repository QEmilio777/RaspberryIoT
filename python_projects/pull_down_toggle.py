import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

pin_led = 38
pin_button = 40
toggle = False
prev_state = 0

ON = 1
OFF = 0

GPIO.setup(pin_led, GPIO.OUT)
GPIO.setup(pin_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		read_in = GPIO.input(pin_button)
		print(read_in)

		if read_in == 1 and prev_state == 0:
			toggle = not toggle

		if read_in == 0 and prev_state == 1:
			if toggle:
				GPIO.output(pin_led, ON)
			else:
				GPIO.output(pin_led, OFF)

		if read_in == 0 and toggle:
			GPIO.output(pin_led, ON)

		prev_state = read_in
		sleep(0.1)

except KeyboardInterrupt:
	GPIO.cleanup()
	print('--GPIO pins ready to go')
