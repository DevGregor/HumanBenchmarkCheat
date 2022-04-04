import time, pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# clicks are lined up for the buttons if the page is opened on the main screen

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://humanbenchmark.com/tests/verbal-memory")
browser.maximize_window()
words = []

pyautogui.click(938,599) # presses start

for x in range(100) : # change range in order to change the outcoming score
    content = browser.page_source
    currentWord = content.split('<div class="word">')[1].split("</div>",1)[0]
    wordSeen = False
    for x in words :
        if x == currentWord :
            wordSeen = True
            break
    if wordSeen == True :
        pyautogui.click(874,499) # presses seen
        print("SEEN")
    else :
        pyautogui.click(1008,499) # presses new
        print("NEW")
        words.append(currentWord)
time.sleep(500)