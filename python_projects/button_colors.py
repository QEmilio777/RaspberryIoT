import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

red_pin_out = 40
green_pin_out = 38
blue_pin_out = 36

red_pin_in = 37
green_pin_in = 35
blue_pin_in = 33

GPIO.setup(red_pin_out, GPIO.OUT)
GPIO.setup(green_pin_out, GPIO.OUT)
GPIO.setup(blue_pin_out, GPIO.OUT)

GPIO.setup(red_pin_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(green_pin_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(blue_pin_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prev_state_red = 0
prev_state_green = 0
prev_state_blue = 0

toggle_red_pin = False
toggle_green_pin = False
toggle_blue_pin = False

try:
	while True:
		read_red_pin = GPIO.input(red_pin_in)
		read_green_pin = GPIO.input(green_pin_in)
		read_blue_pin = GPIO.input(blue_pin_in)

		if read_red_pin == 0 and prev_state_red == 1:
			toggle_red_pin = not toggle_red_pin

		if read_green_pin == 0 and prev_state_green == 1:
			toggle_green_pin = not toggle_green_pin

		if read_blue_pin == 0 and prev_state_blue == 1:
			toggle_blue_pin = not toggle_blue_pin



		GPIO.output(red_pin_out, toggle_red_pin)
		GPIO.output(green_pin_out, toggle_green_pin)
		GPIO.output(blue_pin_out, toggle_blue_pin)

		prev_state_red = read_red_pin
		prev_state_green = read_green_pin
		prev_state_blue = read_blue_pin

		sleep(0.1)

except KeyboardInterrupt:
	GPIO.cleanup()
	print('--pins ready to go')


