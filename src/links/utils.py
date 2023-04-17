import requests
from bs4 import BeautifulSoup
import lxml

def get_link_data(url):
    
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39',
    'Accept-Language':'en',
    }

    response = requests.get(url=url,headers=headers)

    soup = BeautifulSoup(response.text,'lxml')

    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()
    price = soup.select_one(selector=".a-offscreen").getText()
    price = float(price[1:])
    
    return name,price