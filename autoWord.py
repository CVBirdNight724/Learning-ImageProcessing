import pyautogui 

if __name__ == "__main__":
    mornitor = pyautogui.size()
    pyautogui.click(x=100, y=100, clicks = 2, interval=0.1)
    pyautogui.typewrite('{', interval=0.05)
    for i in range(33, 126+1):
        pyautogui.typewrite('"', interval=0.01)
        pyautogui.hotkey('alt','shift')
        pyautogui.typewrite(chr(i), interval=0.01)
        pyautogui.hotkey('alt','shift')
        pyautogui.typewrite('": ', interval=0.01)
        pyautogui.typewrite('chr(', interval=0.01)
        pyautogui.typewrite(str(i), interval=0.01)
        pyautogui.typewrite('), ', interval=0.01)