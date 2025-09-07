import pyautogui
import time
time.sleep(3)

def sendMail():
    # Give yourself a few seconds to move to the right window
    time.sleep(1)

    # select draft
    pyautogui.moveTo(750, 350, duration=1)
    pyautogui.click()

    # send immediately
    pyautogui.moveTo(1300,1050,duration=1)
    pyautogui.click()

    # sendBySchedule();



    print(pyautogui.position())


    pyautogui.FAILSAFE = True


def sendBySchedule():
    # send schedule
    pyautogui.moveTo(1350, 1050, duration=1)
    pyautogui.click()

    # select schedule
    pyautogui.moveTo(1350, 1000, duration=1)
    pyautogui.click()

    # select time
    pyautogui.moveTo(1000, 600, duration=1)
    pyautogui.click()




for i in range(1,5):
    sendMail()
