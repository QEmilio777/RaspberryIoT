import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
pin_forty = 40
GPIO.setup(pin_forty, GPIO.OUT)

try:
	while True:
		readin = GPIO.input(pin_forty)
		print(readin)
		sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
	print('all done')
