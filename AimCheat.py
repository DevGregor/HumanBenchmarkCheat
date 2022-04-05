import time, pyautogui
from CodeBase import *

browser = openBrowserTab("aim")

startBtn = getDynamicCoordinates(950, 422)
pyautogui.click(startBtn[0],startBtn[1]) # presses start

for x in range(30) : # there are 30 targets to click
    target = browser.find_element_by_class_name("css-z6vxiy.e6yfngs3") # class name of the target
    location = target.location
    print(location)
    targetBtn = getDynamicCoordinates(location["x"], location["y"])
    pyautogui.click(targetBtn[0], targetBtn[1] + 100) # coordinates are off and need to be fixed manually
time.sleep(500) # keeps window open