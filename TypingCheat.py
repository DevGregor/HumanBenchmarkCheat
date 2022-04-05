import time, pyautogui
from CodeBase import *

browser = openBrowserTab("typing")

content = browser.page_source
text = content.split('<div class="letters notranslate" tabindex="1">')[1].split("</div>", 1)[0]
text = text.replace('<span class="incomplete current">',"") # removes first span because it's diffrent from the others
text = text.replace('<span class="incomplete">',"")
text = text.replace("</span>","")

print("-----------------------------------------------------------------------------------------")
print(text)
print("-----------------------------------------------------------------------------------------")
pyautogui.typewrite(text)

time.sleep(500) # keeps window open