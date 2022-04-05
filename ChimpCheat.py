import time, pyautogui
from CodeBase import *

browser = openBrowserTab("chimp")

startBtn = getDynamicCoordinates(951, 580)
pyautogui.click(startBtn[0],startBtn[1]) # presses start
lvl = 0

for x in range(20) : # change range in order to change the outcoming score
    targets = []
    targets = browser.find_elements_by_xpath("//div[@class='css-19b5rdt']/div") # gets the child div of the div with css-19b5rdt as class
    sortedTargets = []
    for target in targets :
        posNr = int(target.get_attribute('innerHTML'))
        print(str(posNr) + " : " + str(target.location))
        sortedTargets.insert(posNr - 1, target) # numbers start from 1 and not zero so we have to do -1
    print("-------------------------------")
    for sortedTarget in sortedTargets :
        print(str(sortedTargets.index(sortedTarget) + 1) + " : " + str(sortedTarget.location))
        pyautogui.click(sortedTarget.location["x"] + 20, sortedTarget.location["y"] + 120) # coordinates are off and need to be fixed manually
    lvl += 1
    print("-------------------------------")
    print("LEVEL " + str(lvl) + " FINISHED")
    print("-------------------------------")
    pyautogui.click(953, 579) # presses continue
time.sleep(500) # keeps window open