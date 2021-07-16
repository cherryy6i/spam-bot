#install pyautogui with the command:  pip install pyautogui

import pyautogui
import webbrowser as wb
import time
wb.open("https://www.instagram.com")
time.sleep(10)
for i in range(10):
    pyautogui.press("6")
    pyautogui.press("i")
    pyautogui.press("enter") 
    
