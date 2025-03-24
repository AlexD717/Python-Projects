import pyautogui
import win32api, win32con
import time
import random

time.sleep(1)

simulationButton = [175, 72]
draftArea = [142, 66]
status = [737, 66]
makeSmallerButton = [659, 112]
makeBiggerButton = [627, 112]
bottomMemberList = [1545, 879]

def Click(x, y, pause=0.4):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(random.uniform(0.05, 0.1))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(pause + random.uniform(0.05, 0.1))

# Checks if the green bottom check box has been checked. If it has nothing in the planet should be changed
def BridgeSucessful():
    Click(simulationButton[0], simulationButton[1])
    if (pyautogui.pixel(status[0], status[1])[1] > 120):
        return True
    else:
        return False
    
def OptimizeSelectedStructure():
    i = 0
    while BridgeSucessful():
        i += 1
        Click(draftArea[0], draftArea[1])
        Click(makeSmallerButton[0], makeSmallerButton[1])
        if (i == 10):
            break
    Click(draftArea[0], draftArea[1])
    Click(makeBiggerButton[0], makeBiggerButton[1])

for i in range(23):
    OptimizeSelectedStructure()
    Click(bottomMemberList[0], bottomMemberList[1])
    pyautogui.press("down")
    time.sleep(1)