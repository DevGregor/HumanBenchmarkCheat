import time, pyautogui
from CodeBase import *

browser = openBrowserTab("reactiontime")

startBtn = getDynamicCoordinates(938,599)
pyautogui.click(startBtn[0],startBtn[1]) # presses start

while pyautogui.pixelMatchesColor(int(startBtn[0]),int(startBtn[1]), (206, 38, 54), tolerance=10) :
    print("WAIT")

print("CLICK")
pyautogui.click(startBtn[0],startBtn[1]) # ends game

time.sleep(500) # keeps window open