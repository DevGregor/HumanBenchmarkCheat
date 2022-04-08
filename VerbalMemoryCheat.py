from CodeBase import *

browser = openBrowserTab("verbal-memory")
browser.find_element_by_class_name("css-de05nr.e19owgy710").click()
buttons = browser.find_elements_by_class_name("css-de05nr.e19owgy710") # stores both the 'NEW' and 'SEEN' button
words = []

for x in range(300) : # change range in order to change the outcoming score
    content = browser.page_source
    currentWord = content.split('<div class="word">')[1].split("</div>",1)[0]
    wordSeen = False
    for x in words :
        if x == currentWord :
            wordSeen = True
            break
    if wordSeen == True :
        buttons[0].click()
        print("SEEN")
    else :
        buttons[1].click()
        print("NEW")
        words.append(currentWord)
keepWindowOpen(browser)