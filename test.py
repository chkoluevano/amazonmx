import amazon_mx

mainurl = 'https://www.amazon.com.mx/dp/B086GG3W24?ref=dacx_dp_7868297510501_4011434530001&me=AVDBXBAVVSXLQ&aaxitk=AD5KB6crxpEuiZD2AU6WZw'
price = amazon_mx.getPrice(mainurl)
print(price)