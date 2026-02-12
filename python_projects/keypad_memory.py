import RPi.GPIO as GPIO
from time import sleep

class Keypad:
    
    def __init__(self, trigger="A"):
        self.rows = [11, 13, 15, 29]
        self.columns = [31, 33, 35, 37]
        
        self.word = ""
        
        self.trigger = trigger
        
        self.values = []
        
        self.row_index_out = 0
        self.column_index_out = 0

        self.switch = False
        self.prev_state = 0
        
        self.read_column = 0
        
        self.value = ""

        self.keypad = [[1, 2, 3, "A"], [4, 5, 6, "B"], [7, 8, 9, "C"], ["*", 0, "#", "D"]]
        
#         self._initialize = False
    
    
    def begin(self):
        GPIO.setmode(GPIO.BOARD)
        
        for r in self.rows:
            GPIO.setup(r, GPIO.OUT)

        for c in self.columns:
            GPIO.setup(c, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        
        for r in self.rows:
            GPIO.output(r, False)
        
#         self._initialize = True
        
    
    def keypad_function(self):
        
        for r in self.rows:
            GPIO.output(r, False)
        
        for row_index, r in enumerate(self.rows):
            GPIO.output(r, True)
            for column_index, c in enumerate(self.columns):
                self.read_column = GPIO.input(c)
                if self.read_column:
                    self.row_index_out = row_index
                    self.column_index_out = column_index
                    return 1
        return 0
    
    
    def get_values(self):
#         self.word = ""
        keypad_memory = self.keypad_function()
        if keypad_memory == 1 and self.prev_state == 0:
            self.switch = not self.switch
        
        self.prev_state = keypad_memory
        
        if self.switch:
#             print(f"{keypad[row_index_out][column_index_out]}")
            self.word = f"{self.keypad[self.row_index_out][self.column_index_out]}"
            self.switch = not self.switch
            sleep(0.1)
            return self.word
        
        if not self.switch:
            sleep(0.1)
            return 0
    
    
    def return_values(self):
        while self.value != self.trigger:
            self.value = self.get_values()
            if self.value:
                self.values.append(self.value)
        self.values.pop()
        v = self.values
        self.values = []
        self.value = ""
        return "".join(map(str, v))
        
        
        
        
        
        
        
        
    
        