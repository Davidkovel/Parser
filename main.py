# task 3

import requests
from bs4 import BeautifulSoup

try:
    responce = requests.get("https://www.example.com")

    if responce.status_code == 200:
        soup = BeautifulSoup(responce.text, "html.parser")
        soup_list = soup.find_all("a")

        for image in soup_list:
            href = f"{image.get('href')}"
            if href.startswith("https://"):
                print(href)
except:
    print("Немаэ пiдключення")