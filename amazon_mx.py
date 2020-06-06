import requests
from bs4 import BeautifulSoup

def getPrice(mainurl):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64;x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    req = requests.get(mainurl, headers=headers)
    soup = BeautifulSoup(req.text, "html.parser")
    title = soup.find('span',id='productTitle')
    price = soup.find('span', id = 'priceblock_ourprice')
    if price is None:
        price = soup.find('span', id = 'priceblock_saleprice')
    titulo = title.contents[0].strip()
    precio = price.contents[0]
    currency = "MX"
    f = open("price.txt",'r')
    txtPrice = f.read()
    f.close() 
    if txtPrice != precio:
        txtPrice = int(float(txtPrice[1:].replace(',','')))
        newPrice = int(float(precio[1:].replace(',','')))
        if txtPrice>newPrice:
            d = txtPrice - newPrice
            obs = f'El precio de {titulo} bajó ${d} pesos, su valor actual es {newPrice}'
        else:
            d = newPrice - txtPrice
            obs = f'El precio de {titulo} subió ${d} pesos, su valor actual es {newPrice}'
        f = open("price.txt",'w')
        f.write(precio) 
        f.close()
    else:
        obs = f"EL precio de {titulo} se mantiene en {txtPrice}"
    return obs




   