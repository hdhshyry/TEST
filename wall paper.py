import os
import pyautogui
import time as t
pyautogui.hotkey('winleft', 'd')
os.startfile(r'C:\Users\Moalem\Desktop\ali\History')
pyautogui.hotkey('winleft', 'up')
pyautogui.moveTo(798,449)
pyautogui.click()
pyautogui.press('down')
t.sleep(0.1)
pyautogui.press('up')
t.sleep(0.3)
pyautogui.hotkey('Alt','j')
pyautogui.hotkey('Alt','b')
pyautogui.hotkey('Alt','F4')