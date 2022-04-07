from CodeBase import *
import time, pyautogui

browser = openBrowserTab("sequence")

startBtn = getDynamicCoordinates(950, 550)
pyautogui.click(startBtn[0],startBtn[1]) # presses start

currentLvl = 0

for x in range(30): # change range in order to change the outcoming score
    currentLvl += 1
    sequence = []
    while len(sequence) < currentLvl:
        squares = browser.find_elements_by_xpath("//div[@class='square active']")
        for square in squares:
            sequence.append(square)
        time.sleep(0.5)
    time.sleep(0.5 * currentLvl) # need to wait until squares are clickable
    for s in sequence:
        print(str(sequence.index(s) + 1) + " : " + str(s.location))
        currentSquare = getDynamicCoordinates(s.location["x"], s.location["y"])
        pyautogui.click(currentSquare[0] + 100, currentSquare[1] + 150)
    print("Sequence " + str(currentLvl) + " finished")
time.sleep(500) # keeps window open