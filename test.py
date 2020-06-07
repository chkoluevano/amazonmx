import amazon_mx

mainurl = 'https://www.amazon.com.mx/Kotex-Super-Tampones-caja-tampones/dp/B0106CUP0G/ref=lp_19584639011_1_2?s=hpc&ie=UTF8&qid=1591487437&sr=1-2'
price = amazon_mx.getPrice(mainurl)
print(price)