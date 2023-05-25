# task 4

import requests
from bs4 import BeautifulSoup

try:
    responce = requests.get("https://www.example.com")

    if responce.status_code == 200:
        soup = BeautifulSoup(responce.text, "html.parser")

        for script in soup.find_all(["style", "script"]):
            script.extract()
        text = " ".join(soup.stripped_strings)
        words = len(text.split())
        print(words)

except:
    print("Немаэ пiдключення")
