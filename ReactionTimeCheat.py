import pyautogui
from CodeBase import *

browser = openBrowserTab("reactiontime")
pyautogui.click(600, 340) # starts 1st round

for x in range(5) : # you need to do it 5 times
    while pyautogui.pixelMatchesColor(int(600),int(340), (206, 38, 54), tolerance=10) :
        print("WAIT")
    print("CLICK")
    pyautogui.doubleClick(600, 340) # ends round & starts next round
keepWindowOpen(browser)