import webbrowser
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.timings
import time
import pyperclip

#this number correlates with the IMDB # and you'll want to enter it where you left off
starting_value = 19088


#this will be the working variable
x = starting_value

def save_scraper_page():
    control_tab_value = 1

    while control_tab_value <= 20:
        if control_tab_value == 1:


            #Go to the first tab and save
            pywinauto.keyboard.send_keys('^1')
            pywinauto.keyboard.send_keys('^s')
            time.sleep(1)
            pywinauto.keyboard.send_keys('{ENTER}')
            time.sleep(1)
            pywinauto.keyboard.send_keys('{LEFT}')
            pywinauto.keyboard.send_keys('{ENTER}')
            control_tab_value += 1

        else:
            pywinauto.keyboard.send_keys('^{TAB}')
            pywinauto.keyboard.send_keys('^s')
            time.sleep(.5)
            pywinauto.keyboard.send_keys('{ENTER}')
            pywinauto.keyboard.send_keys('{LEFT}')
            pywinauto.keyboard.send_keys('{ENTER}')
            control_tab_value += 1

def reset_window():
    time.sleep(5)
    pywinauto.keyboard.send_keys('%f')
    pywinauto.keyboard.send_keys('x')
    time.sleep(1)
    app = Application().start(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    time.sleep(1)


def scraper(value):
    #convert the format of x to match the 0000000 format of imdb hyperlinks
    if value % 20 == 0:
        save_scraper_page()
        reset_window()

    else:
        value = str(x).zfill(7)
        pyperclip.copy('https://pro.imdb.com/name/nm' + value)

        #open new tab to search
        pywinauto.keyboard.send_keys('^t')

        #to activate search bar (Chrome)
        pywinauto.keyboard.send_keys('^e')
        pywinauto.keyboard.send_keys('{BACKSPACE}')

        #paste the copied text
        pywinauto.keyboard.send_keys('^v')
        pywinauto.keyboard.send_keys('{ENTER}')

        print(value)



#Run the scraper
while x < 50000:
    if x == starting_value:
        #open web browser
        app = Application().start(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        time.sleep(1)

        #Run a modified version of scraper() method for first time
        value = str(x).zfill(7)
        pyperclip.copy('https://pro.imdb.com/name/nm' + value)

        #to activate search bar (Chrome)
        pywinauto.keyboard.send_keys('^e')
        time.sleep(1)
        pywinauto.keyboard.send_keys('{BACKSPACE}')
        #convert x to the imdb link format '0000000'

        #paste the copied text
        pywinauto.keyboard.send_keys('^v')
        time.sleep(1)
        pywinauto.keyboard.send_keys('{ENTER}')
    
        print(value)
        x = x + 1
        continue


    else:
        scraper(x)
        x = x + 1
       
        
 
        






    

