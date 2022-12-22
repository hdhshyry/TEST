import os
import shutil
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
pyautogui.hotkey('winleft', 'd')
source_folder = r'J:\program\wav\\'
destination_folder = r'C:\Users\Moalem\Music\\'
# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder + file_name
    destination = destination_folder + file_name
    # copy only files
    if os.path.isfile(source):
        shutil.copy(source, destination)
        print('copied', file_name)
for i in range(50):
    pyautogui.press('volumeup')
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
