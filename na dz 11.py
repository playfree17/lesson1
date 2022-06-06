import requests
from bs4 import BeautifulSoup
from PIL import Image
print("Виберіть який курс валют ви бажаєте оглянути: долар США, євро, фунт стерлінгів, злотий")
y = input("Напишіть, яка валюта. Долар США - $, євро - €, фунт стерлінгів - £, злотий - Zł: ")
if y == "$":
    response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,features="html.parser")
        soup_list = soup.find_all("td",{"data-label":"Офіційний курс"})
        g = soup_list[7]
        print(f"Курс долара США — {g.text}")
    print("-----$--------Курс долара США за остані місяці--------$-----")
    img = Image.open("na dz 11.JPG")
    img.show()
if y == "€":
    response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("td", {"data-label": "Офіційний курс"})
        g = soup_list[8]
        print(f"Курс євро — {g.text}")
    print("-----€--------Курс євро за остані місяці--------€-----")
    img = Image.open("na dz 11.1.JPG")
    img.show()
if y == "£":
    response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("td", {"data-label": "Офіційний курс"})
        g = soup_list[29]
        print(f"Курс фунт стерлінгів — {g.text}")
    print("-----£--------Курс фунт стерлінгів за остані місяці--------£-----")
    img = Image.open("na dz 11.2.JPG")
    img.show()
if y == "Zł":
    response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("td", {"data-label": "Офіційний курс"})
        g = soup_list[11]
        print(f"Курс злотів — {g.text}")
    print("-----Zł--------Курс злотів за остані місяці--------Zł-----")
    img = Image.open("na dz 11.3.JPG")
    img.show()