import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.co.uk/dp/B07TSG8D54"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84"}

resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, "lxml")

item = {
    "name": soup.select_one("span#productTitle").text.strip(),
    "price": soup.select_one("span.a-price span").text,
}

print(item)