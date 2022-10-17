# Hoist Fitness

import pandas as pd
import requests as r
from bs4 import BeautifulSoup

req1 = r.get('https://partakefoods.com/collections/all')

soup = BeautifulSoup(req1.text, 'html.parser')

product_list = []
products = soup.find_all('li', class_='grid__item')
for product in products:
    product_name = product.find('h3').text
    product_price = product.find('span',class_='price-item price-item--regular').text
    product_price = product_price.replace('$',"").replace('From','').strip()
    product_list.append({'name':product_name, 'price':product_price})
    
df = pd.DataFrame(product_list)

df.to_csv('shopify_scrape_results.csv', index=False)

# print(product_list)

# products[0].find('span',class_='reg-price').text

