import pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def openBrowserTab(testName):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://humanbenchmark.com/tests/" + testName)
    browser.maximize_window()
    return browser

def getDynamicCoordinates(posX, posY):
    width, height = pyautogui.size()
    dynamicCoordinates = []
    dynamicCoordinates.append((posX * width) / 1920) # coordiantes are calculated from FHD since coordinates originated from there
    dynamicCoordinates.append((posY * height) / 1080) 
    return dynamicCoordinates