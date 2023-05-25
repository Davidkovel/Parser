# task 1

import requests
from bs4 import BeautifulSoup

query = requests.get("https://www.example.com")

if query.status_code == 200:
    soup = BeautifulSoup(query.content, "html.parser")
    title = soup.find("title").text
    print(title)
else:
    print("Немаэ пiдключення ", query.status_code)
