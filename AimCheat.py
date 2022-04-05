import time, pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://humanbenchmark.com/tests/aim")
browser.maximize_window() # window needs to be a certain size so full screen should always work

pyautogui.click(950, 422) # presses start

for x in range(30) : # there are 30 targets to click
    target = browser.find_element_by_class_name("css-z6vxiy.e6yfngs3") # class name of the target
    location = target.location
    print(location)
    pyautogui.click(location["x"], location["y"] + 100) # coordinates are off so 100px are added towards the Y position
time.sleep(500) # keeps window open