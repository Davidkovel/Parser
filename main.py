# task 1

import requests
from bs4 import BeautifulSoup

try:
    query = requests.get("https://www.example.com")
    soup = BeautifulSoup(query.content, "html.parser")
    title = soup.find("title").text
    print(title)
except:
    print("Немаэ пiдключення")
