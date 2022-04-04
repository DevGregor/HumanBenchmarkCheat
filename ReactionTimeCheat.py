from ast import While
import time, pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://humanbenchmark.com/tests/reactiontime")
browser.maximize_window()

pyautogui.click(938,599) # starts game

isGreen = False
while isGreen == False :
    content = browser.page_source
    if "Click!" in content :
        isGreen = True
        pyautogui.click(938,599) # ends game
time.sleep(500) # keeps window open