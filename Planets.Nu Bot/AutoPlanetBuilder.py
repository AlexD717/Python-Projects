import HelpfulFunctions
import pyautogui
import win32api, win32con
import time
import random

HelpfulFunctions.AskQuestion("Make sure that you have one of your active planets selected", HelpfulFunctions.confirmativeReplies)

greenCheckBoxPos = [328, 608]
nextArrowPos = [382, 605]
buildingMenu = [105, 367]
plus100Button = [688, 206]
minesButton = [487, 130]

def Click(x, y, pause=0.4):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(random.uniform(0.05, 0.1))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(pause + random.uniform(0.05, 0.1))

# Checks if the green bottom check box has been checked. If it has nothing in the planet should be changed
def PlanetCanBeChanged():
    if (pyautogui.pixel(greenCheckBoxPos[0], greenCheckBoxPos[1])[1] > 160):
        return True
    else:
        return False
    
def BuildOnAllPlanets():
    while PlanetCanBeChanged():
        print("\nBuilding on new planet")
        print("Opening building panel")
        Click(buildingMenu[0], buildingMenu[1]) # Opens building menu, factories default selected
        print("Building factories")
        for i in range(2):
            Click(plus100Button[0], plus100Button[1]) # Build max number of factories
        print("Openening mine menu")
        Click(minesButton[0], minesButton[1]) # Selects mines to build
        print("Building mines")
        for i in range(2):
            Click(plus100Button[0], plus100Button[1]) # Build max number of mines
        print("Marking planet as completed")
        Click(greenCheckBoxPos[0], greenCheckBoxPos[1]) # Marks planet as completed
        print("Going on to next planet")
        Click(nextArrowPos[0], nextArrowPos[1]) # Goes to next planet
        time.sleep(1)

BuildOnAllPlanets()