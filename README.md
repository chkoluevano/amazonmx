# amazonmx
Obtiene el precio de un producto por medio de una URL de amazon méxico ( excepto productos con variantes (ropa)) usando BeautifulSoup

## Usage
```python
import amazon_mx
#Samsung Galaxy M31 Red 
mainurl = 'https://www.amazon.com.mx/dp/B086GG3W24?ref=dacx_dp_7868297510501_4011434530001&me=AVDBXBAVVSXLQ&aaxitk=AD5KB6crxpEuiZD2AU6WZw'
price = amazon_mx.getPrice(mainurl,isBook=False)
# El precio de Samsung Galaxy M31 Red es $6,999.00
#
#
#Libro de Slavoj Žižek 
mainurl = 'https://www.amazon.com.mx/permanencia-negativo-Hitchcock-Intervenciones-post-contempor%C3%A1neas-ebook/dp/B077S6JFRC/ref=sr_1_6?__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=zizek&qid=1591576445&s=digital-text&sr=1-6'
price = amazon_mx.getPrice(mainurl,isBook=True)
# [{'tipo': 'Kindle', 'precio': '$57.00'}]

```