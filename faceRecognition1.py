import numpy as np
import cv2
 
capture = cv2.VideoCapture(0)
ret, frame = capture.read()
 
while(True):
    ret, frame = capture.read()
    # gray = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    cv2.imshow('Test', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
capture.release()
cv2.destroyAllWindows()