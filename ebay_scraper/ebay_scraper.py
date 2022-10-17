import requests
from bs4 import BeautifulSoup
import pandas as pd

searchterm = 'sony+a6500'

def get_data(searchterm):
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={searchterm}&_sacat=0&LH_TitleDesc=0&LH_Complete=1&LH_Sold=1&_oac=1&rt=nc&_oaa=1&_dcat=31388'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def parse(soup):
    productslist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        product = {
            'title': item.find('span', {'role': 'heading'}).string,
            # 'soldprice': float(item.find('span', {'class': 's-item__price'}).text.replace('$', '').replace(',', '').strip()),
            # 'solddate': item.find('div', {'class': 's-item__title--tagblock '}).find('span', {'class':'POSITIVE'}),
            # 'solddate': item.find('div', {'class': 's-item__title--tagblock '}).find('span', {'class': 'POSITIVE'}.text),
            'bids': item.find('span', {'class': 's-item__bids'}),
            'link': item.find('a', {'class': 's-item__link'})['href'],
        }
        productslist.append(product)
        
    return productslist

def output(productslist, searchterm):
    productsdf = pd.DataFrame(productslist)
    productsdf.to_csv(searchterm + 'output.csv', index=False)
    print('Saved to CSV')
    return

soup = get_data(searchterm)
productslist = parse(soup)
output(productslist, searchterm)