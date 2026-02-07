import RPi.GPIO as GPIO
from time import sleep

in2_pin = 12
in1_pin = 6
enableA = 5

in3_pin = 16
in4_pin = 20
enableB = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(in2_pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(in1_pin, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(in3_pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(in4_pin, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(enableA, GPIO.OUT)
GPIO.setup(enableB, GPIO.OUT)

pwm_motor = GPIO.PWM(enableA, 7000)
pwm_motor_2 = GPIO.PWM(enableB, 7000)

pwm_motor.start(0)
pwm_motor_2.start(0)

try:
    while True:
        
        GPIO.output(in2_pin, GPIO.HIGH)
        GPIO.output(in1_pin, GPIO.LOW)
        GPIO.output(in3_pin, GPIO.HIGH)
        GPIO.output(in4_pin, GPIO.LOW)
        
        for duty in range(0, 101, 1):
            pwm_motor.ChangeDutyCycle(duty)
            pwm_motor_2.ChangeDutyCycle(duty)
            sleep(0.01)
        
        sleep(5)
        
        
        for duty in range(100, -1, -1):
            pwm_motor.ChangeDutyCycle(duty)
            pwm_motor_2.ChangeDutyCycle(duty)
            sleep(0.01)
        
        GPIO.output(in2_pin, GPIO.LOW)
        GPIO.output(in1_pin, GPIO.HIGH)
        GPIO.output(in3_pin, GPIO.LOW)
        GPIO.output(in4_pin, GPIO.HIGH)
        
        for duty in range(0, 101, 1):
            pwm_motor.ChangeDutyCycle(duty)
            pwm_motor_2.ChangeDutyCycle(duty)
            sleep(0.01)
        
        sleep(5)
        
        
        for duty in range(100, -1, -1):
            pwm_motor.ChangeDutyCycle(duty)
            pwm_motor_2.ChangeDutyCycle(duty)
            sleep(0.01)
        
        #################
        
        # GPIO.output(in3_pin, GPIO.HIGH)
        # GPIO.output(in4_pin, GPIO.LOW)
        
        # for duty in range(0, 101, 1):
        #     pwm_motor_2.ChangeDutyCycle(duty)
        #     sleep(0.01)
        
        # sleep(5)
        
        
        # for duty in range(100, -1, -1):
        #     pwm_motor_2.ChangeDutyCycle(duty)
        #     sleep(0.01)
        
        # GPIO.output(in3_pin, GPIO.LOW)
        # GPIO.output(in4_pin, GPIO.HIGH)
        
        # for duty in range(0, 101, 1):
        #     pwm_motor_2.ChangeDutyCycle(duty)
        #     sleep(0.01)
        
        # sleep(5)
        
        
        # for duty in range(100, -1, -1):
        #     pwm_motor_2.ChangeDutyCycle(duty)
        #     sleep(0.01)
        
            
    
except KeyboardInterrupt:
    sleep(0.1)
    print("Salida correcta")
finally:
    sleep(0.1)
    pwm_motor.stop()
    del pwm_motor
    GPIO.cleanup()