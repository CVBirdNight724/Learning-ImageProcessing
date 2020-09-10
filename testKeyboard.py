import pyautogui 
import numpy as np
import json

class control:
    def __init__(self):
        self.mornitor = np.array([pyautogui.size().width, pyautogui.size().height])
        self.pos = np.array([0, 0])
        with open('Backup/keyboardThai.json') as f:
            self.key = json.load(f)
        print(self.key)

    def mouseMove(self, nextPos):
        pyautogui.dragTo(x=nextPos[0], y=nextPos[1], duration=0.1)
        self.pos = np.array([nextPos[0], nextPos[1]])
        return None

    def mouseClick(self, clicks=1, button=0):
        if button == 0:
            button = 'left'
        elif button == 1:
            button = 'middle'
        elif button == 2:
            button = 'right' 
        pyautogui.click(clicks=clicks, interval=0.01, button=button, duration=0.1)
        return None

    def mouseCrop(self, nextPos, button=0):
        if button == 0:
            button = 'left'
        elif button == 1:
            button = 'middle'
        elif button == 2:
            button = 'right'
        pyautogui.mouseDown(button=button)
        pyautogui.dragTo(x=nextPos[0], y=nextPos[1], duration=0.1)
        pyautogui.mouseUp(button=button)

    def keyboardEng(self, text):
        t = np.random.uniform(0.05, 0.2)
        pyautogui.typewrite(text, interval=t)

    def keyboardTh(self, text):
        t = np.random.uniform(0.05, 0.2)
        st = ''
        for ch in list(text):
            st += self.key[ch]
        pyautogui.hotkey('alt','shift')
        pyautogui.typewrite(st, interval=t)
        pyautogui.hotkey('alt','shift')


if __name__ == "__main__":
    ct = control()
    ct.mouseMove(nextPos=[100, 100])
    ct.mouseClick(clicks=1)
    # ct.mouseCrop(nextPos=[1000,1000])
    ct.keyboardEng('Hello')
    ct.keyboardTh('สวัสดี')