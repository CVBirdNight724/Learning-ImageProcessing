import pyautogui 
import numpy as np

if __name__ == "__main__":
    mornitor = pyautogui.size()
    pyautogui.moveTo(50, 50)
    pre_pos = np.array([50, 50])
    pyautogui.click(clicks = 2, interval=0.1)
    pyautogui.mouseDown()
    pos = np.array([mornitor.width-50, mornitor.height-50])

    pyautogui.dragTo(x=pos[0], y=pos[1], duration=0.3)
    pyautogui.mouseUp()

    a = "สวัสดี"
    print(list(a))
    # pyautogui.hotkey('alt','shift')
    # pyautogui.typewrite('l;ylfu',interval=0.1)
    # pyautogui.hotkey('alt','shift')