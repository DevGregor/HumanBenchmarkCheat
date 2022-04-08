import time, pyautogui
from CodeBase import *

browser = openBrowserTab("number-memory")
browser.find_element_by_class_name("css-de05nr.e19owgy710").click()
content = browser.page_source
sleepTimer = 1

for x in range(20) : # change range in order to change the outcoming score
    content = browser.page_source
    numberToRemember = content.split('<div class="big-number ">')[1].split("</div", 1)[0]
    sleepTimer += 1 # for each try you gain 1s
    time.sleep(sleepTimer)
    print(numberToRemember)
    pyautogui.typewrite(numberToRemember)
    for x in range(2):
        browser.find_element_by_class_name("css-de05nr.e19owgy710").click()
keepWindowOpen(browser)