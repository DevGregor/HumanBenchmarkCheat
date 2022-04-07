import time, pyautogui
from CodeBase import *

browser = openBrowserTab("verbal-memory")
words = []

startBtn = getDynamicCoordinates(938, 575)
pyautogui.click(startBtn[0],startBtn[1]) # presses start

for x in range(100) : # change range in order to change the outcoming score
    content = browser.page_source
    currentWord = content.split('<div class="word">')[1].split("</div>",1)[0]
    wordSeen = False
    for x in words :
        if x == currentWord :
            wordSeen = True
            break
    if wordSeen == True :
        seenBtn = getDynamicCoordinates(874, 499)
        pyautogui.click(seenBtn[0],seenBtn[1]) # presses seen
        print("SEEN")
    else :
        newBtn = getDynamicCoordinates(1008, 499)
        pyautogui.click(newBtn[0],newBtn[1]) # presses new
        print("NEW")
        words.append(currentWord)
time.sleep(500) # keeps window open