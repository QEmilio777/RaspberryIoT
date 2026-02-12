import RPi.GPIO as GPIO
from time import sleep

led_pin_out = 38
pin_up = 36
pin_down = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin_out, GPIO.OUT)
GPIO.setup(pin_up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin_down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

mypwm_led = GPIO.PWM(led_pin_out, 100)
mypwm_led.start(0)

toggle_up = False
toggle_down = False
prev_state_up = 0
prev_state_down = 0
increment = 0
bp = 3
a = 100**(1/bp)
mypwm_led_val = 0

try:
	while True:
		read_pin_up = GPIO.input(pin_up)
		read_pin_down = GPIO.input(pin_down)

		if read_pin_up == 1 and prev_state_up == 0:
			if increment < bp:
				increment += 1
			mypwm_led_val = a**increment
			if mypwm_led_val >= 99:
                                mypwm_led_val = 100
			toggle_up = not toggle_up

		if read_pin_down == 1 and prev_state_down == 0:
			if increment > 0:
				increment -= 1
			mypwm_led_val = a**increment
			if mypwm_led_val <= 1:
				mypwm_led_val = 0

			toggle_down = not toggle_down

		if read_pin_up == 0:
			mypwm_led.ChangeDutyCycle(mypwm_led_val)

		if read_pin_down == 0:
			mypwm_led.ChangeDutyCycle(mypwm_led_val)

		prev_state_up = read_pin_up
		prev_state_down = read_pin_down
		print(mypwm_led_val)
		sleep(0.1)

except KeyboardInterrupt:
	pass
finally:
	mypwm_led.stop()
	del mypwm_led
	GPIO.cleanup()
	print('--GPIO pins ready to go')
