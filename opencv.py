import cv2
from picamera2 import Picamera2


picam = Picamera2()

picam.preview_configuration.main.size = (1080, 720)
picam.preview_configuration.main.format = "RGB888"
picam.preview_configuration.controls.FrameRate = 60
picam.preview_configuration.align()

picam.configure('preview')

picam.start()


while True:
    frame = picam.capture_array()
    
    cv2.imshow("cam1", frame)
    
    if (cv2.waitKey(1) == ord('q')):
        break


cv2.destroyAllWindows()
print("Programa finalizado")
