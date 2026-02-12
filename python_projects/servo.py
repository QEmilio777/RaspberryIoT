import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

servo_pin = 40

GPIO.setup(servo_pin, GPIO.OUT, initial=GPIO.LOW)

pwm_servo = GPIO.PWM(servo_pin, 50)

pwm_servo.start(0)

try:
    while True:
        dc_input = float(input('the dc: '))
        pwm_servo.ChangeDutyCycle(dc_input)
        sleep(0.1)



except KeyboardInterrupt:
    pwm_servo.stop()
    del pwm_servo
    GPIO.cleanup()
    print('gpio pins ready to go')
