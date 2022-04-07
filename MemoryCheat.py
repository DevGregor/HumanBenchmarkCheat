import time, pyautogui
from sniffio import current_async_library_cvar
from CodeBase import *

browser = openBrowserTab("memory")

startBtn = getDynamicCoordinates(950, 550)
pyautogui.click(startBtn[0],startBtn[1]) # presses start

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
        dynamicTileCoordinates = getDynamicCoordinates(tile.location["x"], tile.location["y"])
        pyautogui.click(dynamicTileCoordinates[0] + 30, dynamicTileCoordinates[1] + 150)
time.sleep(500) # keeps window open