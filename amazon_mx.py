import requests
from bs4 import BeautifulSoup

def isValid(mainURL):
    if mainURL.startswith('https://www.amazon.com.mx/'):
        return True
    return False

def getPrice(mainurl, isBook=False):
    if isValid(mainurl):
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64;x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate",     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        req = requests.get(mainurl, headers=headers)
        soup = BeautifulSoup(req.text, "html.parser")
        title = soup.find('span',id='productTitle')
        if not isBook:
            price = soup.find('span', id = 'priceblock_ourprice')
            if price is None:
                price = soup.find('span', id = 'priceblock_saleprice')
            titulo = title.contents[0].strip()
            precio = price.contents[0]
            currency = "MX"
            return  f"El precio de {titulo} se mantiene en {precio}"
        else:
            listOfBooks = soup.find_all('ul',{'class':'a-unordered-list a-nostyle a-button-list a-horizontal'})
            books = []
            for m in listOfBooks:
               li = m.find_all('li')
               for l in li:
                   a = l.find_all('a',{'class':'a-button-text'})
                   if a is not None:
                       book = {}
                       spanInsideA = a[0].find_all('span')
                       typeOfBook = (spanInsideA[0].text)
                       book["tipo"]  = typeOfBook
                       BookPrice = (spanInsideA[1].text).strip()
                       book["precio"] = BookPrice
                       books.append(book)

            return books

    else:
        return "Invalid URL amazonMX "




   