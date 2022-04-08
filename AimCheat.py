import pyautogui
from CodeBase import *

browser = openBrowserTab("aim")

for x in range(31) : # there are 30 targets to click + the start target = 31 targets
    target = browser.find_element_by_class_name("css-q4kt6s.e6yfngs1") # class name of the target
    location = target.location
    print(location)
    pyautogui.click(location["x"], location["y"])
keepWindowOpen(browser)