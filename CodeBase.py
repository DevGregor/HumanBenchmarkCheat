import pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def openBrowserTab(testName):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://humanbenchmark.com/tests/" + testName)
    browser.maximize_window()
    print(pyautogui.size())
    return browser

def getDynamicCoordinates(posX, posY):
    width, height = pyautogui.size()
    dynamicCoordinates = []
    x = posX / 1920 # coordiantes are calculated from FHD since coordinates originated from there
    y = posY / 1080
    dynamicCoordinates.append(x * width) 
    dynamicCoordinates.append(y * height) 
    return dynamicCoordinates