import requests
from bs4 import BeautifulSoup
import pyttsx3
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sendersemail', 'password')
    subject = 'Price fell down!'
    body = 'https://www.amazon.in/WOW-Brightening-Vitamin-Face-Wash/dp/B07SZ243VZ/ref=sr_1_6?dchild=1&keywords=wow+face+wash&qid=1594306550&smid=A27LPMZIGZ21IK&sr=8-6'
    content = f'Subject: {subject}\n\n{body}'
    server.sendmail('email', 'receiver email', content)
    server.close()


URL = 'https://www.amazon.in/WOW-Brightening-Vitamin-Face-Wash/dp/B07SZ243VZ/ref=sr_1_6?dchild=1&keywords=wow+face+wash&qid=1594306550&smid=A27LPMZIGZ21IK&sr=8-6'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='productTitle')
price = soup.find(id='priceblock_dealprice').get_text().strip()
speak(price)
price = price[1:5]
price = float(price)
send_email()
