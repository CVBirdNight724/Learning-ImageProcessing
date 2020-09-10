import numpy as np
from PIL import ImageGrab
import cv2
import time

if __name__ == "__main__":

    while True:
        screen = np.array(ImageGrab.grab())
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        cv2.imshow('Screen', screen)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        elif cv2.waitKey(1) & 0xFF == ord('s'):
            tm = time.localtime()
            filename = ('BackUp/Capture_' + str(tm.tm_year) + str(tm.tm_mon) + str(tm.tm_mday) + 
                        str(tm.tm_hour) + '_' + str(tm.tm_hour) + '_' + str(tm.tm_min) +
                        '_' + str(tm.tm_sec) + '.jpg')
            cv2.imwrite(filename, screen)