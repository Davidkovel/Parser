# Bonus

import requests
from bs4 import BeautifulSoup

try:
    responce = requests.get("https://weather.com/uk-UA/weather/today/l/2261b41a35498e667410cb84dfb95d455f977b64d2c02b673df410b7d9ec31ed")

    if responce.status_code == 200:
        soup = BeautifulSoup(responce.text, "html.parser")
        city = soup.find('h1', class_="CurrentConditions--location--1YWj_")
        weather = soup.find('span', class_="CurrentConditions--tempValue--MHmYY")
        if city:
            city_name = city.text.strip()
            weather = weather.text.strip()
            print(city_name)
            print(f"Температура - {weather}")
        else:
            print("Мiсто не знайдено")
except:
    print("Немаэ пiдключення")
