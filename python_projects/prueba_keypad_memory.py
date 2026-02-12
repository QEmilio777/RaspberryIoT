import RPi.GPIO as GPIO
from time import sleep


rows = [11, 13, 15, 29]
columns = [31, 33, 35, 37]

row_index_out = 0
column_index_out = 0

switch = False
prev_state = 0

keypad = [[1, 2, 3, "A"], [4, 5, 6, "B"], [7, 8, 9, "C"], ["*", 0, "#", "D"]]

GPIO.setmode(GPIO.BOARD)

for r in rows:
    GPIO.setup(r, GPIO.OUT)

for c in columns:
    GPIO.setup(c, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    


def keypad_function():
    global row_index_out
    global column_index_out 
    for row_index, r in enumerate(rows):
        GPIO.output(r, True)
        for column_index, c in enumerate(columns):
            read_column = GPIO.input(c)
            if read_column:
                row_index_out = row_index
                column_index_out = column_index
                return 1
    return 0

try:
    while True:
        
        keypad_memory = keypad_function()
        if keypad_memory == 1 and prev_state == 0:
            switch = not switch
        
        if switch:
            print(f"{keypad[row_index_out][column_index_out]}")
            switch = not switch
            
        prev_state = keypad_memory
            
        for r in rows:
            GPIO.output(r, False)
                
        sleep(0.1)
            
except KeyboardInterrupt:
    sleep(0.1)
    GPIO.cleanup()
    print("GPIO ready to go")
    
    