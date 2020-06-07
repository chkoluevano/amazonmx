# amazonmx
Obtiene el precio de un producto por medio de una URL de amazon méxico ( excepto libros)

## Usage
```python
import amazon_mx
#Samsung Galaxy M31 Red 
mainurl = 'https://www.amazon.com.mx/dp/B086GG3W24?ref=dacx_dp_7868297510501_4011434530001&me=AVDBXBAVVSXLQ&aaxitk=AD5KB6crxpEuiZD2AU6WZw'
price = amazon_mx.getPrice(mainurl)
# El precio de Samsung Galaxy M31 Red es $6,999.00
```
