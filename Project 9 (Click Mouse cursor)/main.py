import pyautogui
import time

# Give yourself a few seconds to move to the right window
time.sleep(3)

# select draft
pyautogui.moveTo(750, 350, duration=1)
pyautogui.click()

# Click at that position
# pyautogui.click()
# send immediately
# pyautogui.moveTo(1300,1050,duration=1)

# send schedule
pyautogui.moveTo(1350,1050,duration=1)
pyautogui.click()

# select schedule
pyautogui.moveTo(1350,1000,duration=1)
pyautogui.click()

# select time
pyautogui.moveTo(1000,600,duration=1)
pyautogui.click()

print(pyautogui.position())


pyautogui.FAILSAFE = True
