import RPi.GPIO as GPIO
import MCP3008_simple as MCP
from time import sleep

GPIO.setmode(GPIO.BOARD)

xaxis_channel = 0
yaxis_channel = 1

push_button = 40
GPIO.setup(push_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:
    while True:
        read_xaxis = MCP.getResult(xaxis_channel, 10)
        read_yaxis = MCP.getResult(yaxis_channel, 10)
        button_state = GPIO.input(push_button)
        
        print('x_value: ', read_xaxis, 'y_value: ', read_yaxis, 'button: ', button_state)
        sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print('pins ready to go')
        
        