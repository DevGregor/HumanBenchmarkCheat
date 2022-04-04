import time, pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://humanbenchmark.com/tests/reactiontime")
browser.maximize_window()

pyautogui.click(938,599) # starts game

isGreen = False
color = pyautogui.pixel(938, 599)
while color == "(206, 38, 54)" : # red
    color = pyautogui.pixel(938, 599)
    if color.MatchesPixel(206, 38, 54) : # green
        pyautogui.click(938,599) # ends game
time.sleep(500) # keeps window open