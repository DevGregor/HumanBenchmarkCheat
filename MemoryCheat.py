import time, pyautogui
from CodeBase import *

browser = openBrowserTab("memory")
browser.find_element_by_class_name("css-de05nr.e19owgy710").click()
currentLvl = 0

for x in range(30) : # change range in order to change the outcoming score
    tilesShown = False
    tiles = []
    currentLvl += 1
    while tilesShown == False :
        tiles = browser.find_elements_by_xpath("//div[@class='active css-lxtdud eut2yre1']")
        if(len(tiles) == currentLvl + 2) :
            tilesShown = True
    time.sleep(3)
    for tile in tiles :
        pyautogui.click(tile.location["x"] + 20, tile.location["y"] + 80)
keepWindowOpen(browser)