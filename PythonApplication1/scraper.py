import webbrowser
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.timings
import time
import pyperclip


#this number correlates with the IMDB #
x = 1

while x <= 100:
    #open web browser
    app = Application().start(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    time.sleep(1)

    #convert the format of x to match the 0000000 format of imdb
    x = str(x).zfill(7)
    pyperclip.copy('https://pro.imdb.com/name/nm' + x)

    #to activate search bar (Chrome)
    pywinauto.keyboard.send_keys('^e')
    time.sleep(1)
    pywinauto.keyboard.send_keys('{BACKSPACE}')
    #convert x to the imdb link format '0000000'

    #paste the copied text
    pywinauto.keyboard.send_keys('^v')
    time.sleep(1)
    pywinauto.keyboard.send_keys('{ENTER}')
    time.sleep(5)

    pywinauto.keyboard.send_keys('^s')
    time.sleep(1)
    pywinauto.keyboard.send_keys('{ENTER}')
    time.sleep(5)

    x = int(x) + 1
    print(x)

    pywinauto.keyboard.send_keys('^w')
    time.sleep(1)

    

