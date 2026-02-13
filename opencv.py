import cv2
from picamera2 import Picamera2
from time import sleep

picam = Picamera2()

picam.preview_configuration.set.size = (1080, 720)
picam.preview_configuration.main.format = "RGB888"
picam.preview_configuration.controls.FrameRate = 60
picam.preview_configuration.align()

picam.configure('preview')

picam.start()

try:
    
    while True:
        frame = picam.capture_array()
        
        if (cv2.waitKey(0) == 'q'):
            break
        
        cv2.imshow(frame, "cam1")
        
        sleep(10)
        
        
except KeyboardInterrupt:
    print("Ctrl ejecutado")
    pass
finally:
    cv2.destroyAllWindows()
    print("Programa finalizado")
