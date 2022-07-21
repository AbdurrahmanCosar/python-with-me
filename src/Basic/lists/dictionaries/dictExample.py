# 1 - Ürün bilgisini {id, isim, fiyat} kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız

products = {
    1 : {},
    2 : {}
}

productId_1 = int(input("1. Ürün ID'si: "))
productName_1 = str(input("1. Ürün Adı: "))
productPrice_1 = int(input("1. Ürün Fiyatı: "))

productId_2 = int(input("2. Ürün ID'si: "))
productName_2 = str(input("2. Ürün Adı: "))
productPrice_2 = int(input("2. Ürün Fiyatı: "))

products[1] = {"id" : productId_1, "name": productName_1, "price" : productPrice_1}
products[2] = {"id" : productId_2, "name": productName_2, "price" : productPrice_2}

print(products)

# 2- Ürün ID bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.
products_ = {
    123 : { "name": "Kolye", "price": 50},
    456 : { "name": "Bileklik", "price": 40}
}

searchProduct = int(input("Aratmak istediğiniz ürün ID'si: "))

info = products_[searchProduct]

print(f"Ürün adı: {info['name']}, Ürün fiyatı: {info['price']} ") # Eğer info'nun altında kırmızı çizgi belirirse [] içine " " yerine ' ' koymayı deneyiniz.
