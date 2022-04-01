from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://humanbenchmark.com/tests/verbal-memory")
browser.maximize_window()
time.sleep(5) # press start
words = []

for x in range(6) :
    content = browser.page_source
    currentWord = content.split('<div class="word">')[1].split("</div>",1)[0]
    wordSeen = False

    for x in words :
        if x == currentWord :
            wordSeen = True
            break
    print(wordSeen) # True means seen | False means new
    words.append(currentWord)
    time.sleep(5)