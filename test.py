import amazon_mx

mainurl = 'https://www.amazon.com.mx/permanencia-negativo-Hitchcock-Intervenciones-post-contempor%C3%A1neas-ebook/dp/B077S6JFRC/ref=sr_1_6?__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=zizek&qid=1591576445&s=digital-text&sr=1-6'
price = amazon_mx.getPrice(mainurl,book=True)
print(price)