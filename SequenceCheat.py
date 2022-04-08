from CodeBase import *
import time, pyautogui

browser = openBrowserTab("sequence")
browser.find_element_by_class_name("css-de05nr.e19owgy710").click()

currentLvl = 0

for x in range(30) : # change range in order to change the outcoming score
    currentLvl += 1
    sequence = []
    while len(sequence) < currentLvl:
        squares = browser.find_elements_by_xpath("//div[@class='square active']")
        for square in squares:
            sequence.append(square)
        time.sleep(0.5)
    time.sleep(0.5 * currentLvl) # need to wait until squares are clickable
    for s in sequence :
        print(s.location)
        pyautogui.click(s.location["x"] + 100, s.location["y"] + 150)
    print("Sequence " + str(currentLvl) + " finished")
keepWindowOpen(browser)