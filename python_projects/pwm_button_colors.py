import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

red_pin_out = 40
green_pin_out = 38
blue_pin_out = 36

red_pin_in = 37
green_pin_in = 35
blue_pin_in = 33

GPIO.setup(red_pin_out, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(green_pin_out, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(blue_pin_out, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(red_pin_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(green_pin_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(blue_pin_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

mypwm_red_out = GPIO.PWM(red_pin_out, 100)
mypwm_green_out = GPIO.PWM(green_pin_out, 100)
mypwm_blue_out = GPIO.PWM(blue_pin_out, 100)

mypwm_red_out.start(0)
mypwm_green_out.start(0)
mypwm_blue_out.start(0)

red_increment = 0
green_increment = 0
blue_increment = 0

bp = 5
a = 100**(1/bp)

red_dc = 0
green_dc = 0
blue_dc = 0

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
			if red_dc < 99:
				red_increment += 1
			else:
				red_increment = 0
			if red_increment == 0:
				red_dc = 0
			else:
				red_dc = a**red_increment
			# toggle_red_pin = not toggle_red_pin

		if read_green_pin == 0 and prev_state_green == 1:
			if green_dc < 99:
				green_increment += 1
			else:
				green_increment = 0
			if green_increment == 0:
				green_dc = 0
			else:
				green_dc = a**green_increment
			# toggle_green_pin = not toggle_green_pin

		if read_blue_pin == 0 and prev_state_blue == 1:
			if blue_dc < 99:
				blue_increment += 1
			else:
				blue_increment = 0
			if blue_increment == 0:
				blue_dc = 0
			else:
				blue_dc = a**blue_increment
			# toggle_blue_pin = not toggle_blue_pin


		print(f"red: {red_dc}")
		print(f"green: {green_dc}")
		print(f"blue: {blue_dc}")

		mypwm_red_out.ChangeDutyCycle(red_dc)
		mypwm_green_out.ChangeDutyCycle(green_dc)
		mypwm_blue_out.ChangeDutyCycle(blue_dc)

		prev_state_red = read_red_pin
		prev_state_green = read_green_pin
		prev_state_blue = read_blue_pin

		sleep(0.1)

except KeyboardInterrupt:
	mypwm_red_out.stop()
	mypwm_red_out.stop()
	mypwm_red_out.stop()

	del mypwm_red_out
	del mypwm_green_out
	del mypwm_blue_out

	GPIO.cleanup()
	print('--pins ready to go')


