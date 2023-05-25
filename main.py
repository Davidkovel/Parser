# task 2

import requests
from bs4 import BeautifulSoup

try:
    responce = requests.get("https://uk.wikipedia.org/wiki/Головна_сторінка")

    if responce.status_code == 200:
        soup = BeautifulSoup(responce.content, "html.parser")
        img = soup.find_all("img")

        for image in img:
            print("https://" + image["src"])
except:
    print("Немаэ пiдключення")