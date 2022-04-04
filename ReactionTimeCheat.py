import time, pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://humanbenchmark.com/tests/reactiontime")
browser.maximize_window()

pyautogui.click(938,599) # starts game

while pyautogui.pixelMatchesColor(938,599, (206, 38, 54)) : # red
    color = pyautogui.pixel(938, 599)
    if pyautogui.pixelMatchesColor(938,599, (75, 219, 106)) : # green
        pyautogui.click(938,599) # ends game
time.sleep(500) # keeps window open