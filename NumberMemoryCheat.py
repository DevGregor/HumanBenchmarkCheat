import time, pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://humanbenchmark.com/tests/number-memory")
browser.maximize_window()

pyautogui.click(954, 572) # presses start
content = browser.page_source
sleepTimer = 1

for x in range(20) : # change range in order to change the outcoming score
    content = browser.page_source
    numberToRemember = content.split('<div class="big-number ">')[1].split("</div", 1)[0]
    sleepTimer += 1 # for each try you gain 1s
    time.sleep(sleepTimer)
    print(numberToRemember)
    pyautogui.typewrite(numberToRemember)
    pyautogui.click(954, 529)
    pyautogui.click(950, 571)
time.sleep(500) # keeps window open