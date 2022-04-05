import time, pyautogui
from CodeBase import *

browser = openBrowserTab("number-memory")

startBtn = getDynamicCoordinates(954, 572)
pyautogui.click(startBtn[0],startBtn[1]) # presses start

content = browser.page_source
sleepTimer = 1

for x in range(20) : # change range in order to change the outcoming score
    content = browser.page_source
    numberToRemember = content.split('<div class="big-number ">')[1].split("</div", 1)[0]
    sleepTimer += 1 # for each try you gain 1s
    time.sleep(sleepTimer)
    print(numberToRemember)
    pyautogui.typewrite(numberToRemember)
    firstClick = getDynamicCoordinates(954, 529)
    pyautogui.click(firstClick[0],firstClick[1])
    secondClick = getDynamicCoordinates(950, 571)
    pyautogui.click(secondClick[0],secondClick[1])
time.sleep(500) # keeps window open