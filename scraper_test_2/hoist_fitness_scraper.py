
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

baseurl = "https://www.hoistfitness.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

# k = requests.get('https://www.hoistfitness.com/collections/shop-all?pg={}').text
# soup=BeautifulSoup(k,'html.parser')
# productlist = soup.find_all("div",{"class":"prod-info"})
# print(productlist)

productlinks = []
for x in range(1):  
    k = requests.get('https://www.hoistfitness.com/collections/shop-all?pg={}'.format(x)).text  
    soup=BeautifulSoup(k,'html.parser')  
    productlist = soup.find_all("div",{"class":"prod-info"})

    for product in productlist:
        link = product.find("a").get('href')
        productlinks.append(baseurl + link)
    
print(productlinks)

data=[]
for link in productlinks:
    f = requests.get(link,headers=headers).text
    hun=BeautifulSoup(f,'html.parser')

    try:
        price=hun.find("span",{"class":"price-item price-item--regular"}).text.replace('\n',"")
    except:
        price = None

    try:
        about=hun.find("div",{"class":"overview"}).text.replace('\n',"")
    except:
        about=None

    # try:
    #     rating = hun.find("span", attrs={"data-rating" : True}).text.replace('\n',"")
    # except:
    #     rating=None

    try:
        name=hun.find("h3",{"class":"title"}).text.replace('\n',"")
    except:
        name=None

    item = {"name":name,"price":price, "about":about}

    data.append(item)

    df = pd.DataFrame(data)

    print(df)

    sleep(10)
    