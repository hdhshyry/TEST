import os
import pyautogui
import time
def borrrow (x=4,y=4):    
    for i in range(y):
        pyautogui.press('tab')
    pyautogui.press('enter')
    for i in range(5):
        pyautogui.press('tab')
        time.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.press('BackSpace')
    pyautogui.typewrite(r'C:\Users\Moalem\Music')
    pyautogui.press('enter')
    time.sleep(0.5)
    for i in range(x):
        time.sleep(0.4)
        pyautogui.press('tab')
pyautogui.hotkey('winleft','r')
pyautogui.typewrite('control mmsys.cpl sounds')
pyautogui.press('enter')
time.sleep(0.5)
for i in range(3):
    pyautogui.press('tab')
time.sleep(0.3)
for i in range(2):
    pyautogui.press('right')
time.sleep(0.5)
for i in range(3):
    pyautogui.press('tab')
time.sleep(0.5)
for i in range(8):
    pyautogui.press('down')
time.sleep(0.5)
borrrow()
#step 2
for i in range(5):
    pyautogui.press('down')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.3)
for i in range(7):
    time.sleep(0.3)
    pyautogui.press('tab')
pyautogui.press('down') 
borrrow()
# Step 3
for i in range(3):
    pyautogui.press('down')
time.sleep(0.3)
pyautogui.press('enter')
for i in range(7):
    time.sleep(0.3)
    pyautogui.press('tab')
for i in range(29):
    pyautogui.press('down')
borrrow(y=3)
pyautogui.press('down')
pyautogui.press('up')
pyautogui.press('enter')
for i in range(7):
    time.sleep(0.3)
    pyautogui.press('tab')
for i in range(5):
    pyautogui.press('down')
borrrow(y=3)
for i in range(2):
    pyautogui.press('down')
pyautogui.press('enter')
for i in range (7):
    pyautogui.press('tab')
pyautogui.press('enter')
# sTep 4


   
# ......
#   .......
# os.system('{0}\\System32\\control.exe '.format(os.environ['WINDIR']))
# # os.startfile(           r'C:\Users\Moalem\Desktop\ali')

# # for i in range(1):
# time.sleep(1)
# pyautogui.hotkey('winleft','up')
# pyautogui.moveTo(1245,99)
# time.sleep(1)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(1248,120)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(471,276)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(475,220)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(345,316)
# pyautogui.click()


                                                                        