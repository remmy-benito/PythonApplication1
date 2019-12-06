from bs4 import BeautifulSoup
import os
import time
import xlwt

#define workbook variables
wb = xlwt.Workbook()
ws = wb.add_sheet('Imdb_Emails')
ws.write(0,0,'Emails')

#create a list of emails
emailList=[]

#initialize cell location variable
r=0

#root directory of html
directory = r'E:\ImdbEmails\12-6-2019'

for filename in os.listdir(directory):
       html_full_path = os.path.join(directory, filename)
       print('Iterated over ' + html_full_path)


       soup = BeautifulSoup(open(html_full_path, encoding="utf8").read(), "html.parser")
       for email in soup.select("a[href^='mailto:']"):
        print(email['href'])
        href=email['href']
        try:
            str1, str2 = href.split(':')
        except ValueError:
            break

        emailList.append(str2)

for email in emailList:
    r=r+1
    ws.write(r,0,email)

wb.save('emails1262019.xls')
       




