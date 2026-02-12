import RPi.GPIO as GPIO
from time import sleep

first_led = 29
second_led = 31
third_led = 33
fourth_led = 35
fifth_led = 37

fast = 0.5
medium = 1
slow = 3

on = True
off = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(first_led, GPIO.OUT)
GPIO.setup(second_led, GPIO.OUT)
GPIO.setup(third_led, GPIO.OUT)
GPIO.setup(fourth_led, GPIO.OUT)
GPIO.setup(fifth_led, GPIO.OUT)

binary_list = [0, 0, 0, 0, 0]
counter = 0
accumulator = 0
while counter < 5:

	for index,number in enumerate(binary_list):
		if number == 0:
			binary_list[index] = 1
			break
		else:
			binary_list[index] = 0
			accumulator = 1

			if binary_list[index + 1] == 0:
				binary_list[index + 1] = accumulator
				break

	GPIO.output(first_led, binary_list[0])
	GPIO.output(second_led, binary_list[1])
	GPIO.output(third_led, binary_list[2])
	GPIO.output(fourth_led, binary_list[3])
	GPIO.output(fifth_led, binary_list[4])

	sleep(fast)

	counter = sum(binary_list)

GPIO.output(first_led, 0)
GPIO.output(second_led, 0)
GPIO.output(third_led, 0)
GPIO.output(fourth_led, 0)
GPIO.output(fifth_led, 0)

GPIO.cleanup()
