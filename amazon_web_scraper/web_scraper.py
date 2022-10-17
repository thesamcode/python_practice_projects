from time import time
from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib

# URL = 'https://www.amazon.com/Sony-Content-Creators-Vlogging-Microphone/dp/B08965JV8D/ref=sr_1_1?crid=25Q374L0YOFCO&keywords=sony+camera&qid=1664654803&qu=eyJxc2MiOiI2LjM3IiwicXNhIjoiNi41MCIsInFzcCI6IjUuOTQifQ%3D%3D&sprefix=sony+camer%2Caps%2C154&sr=8-1'

# # use this to get computer's user agent info http://httpbin.org/get
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84"}

# page = requests.get(URL, headers=headers)

# soup1 = BeautifulSoup(page.content, "html.parser")

# soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

# title = soup2.find(id='productTitle').get_text()

# price = soup2.find(id='priceblock_ourprice').get_text()

# print(title)


URL = 'https://www.etsy.com/listing/817123177/extra-large-panoramic-abstract-acrylic?click_key=47f834f023845f2558df2a35c0f6e0858e9664e5%3A817123177&click_sum=7d2e78bb&ref=hp_saved_searches-1-1&sts=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.84"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

# find_by_class = soup1.find_all(class_="wt-text-body-03 wt-line-height-tight wt-break-word")

productname = soup1.body.main.h1


productprice = soup1.find_all(class_="wt-text-title-03 wt-mr-xs-1", )

p_tags = soup1.select('span.wt-screen-reader-only' )
for p_tag in p_tags:
    print(p_tag.get_text(strip=True))

# print(p_tags)