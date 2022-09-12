products = [
	{'name': "iphone 8", "price": 4000},
	{'name': "iphone 8 Plus", "price": 5000},
	{'name': "iphone X", "price": 6000},
	{'name': "iphone XR", "price": 7000},
]

# 1- Tüm ürün bilgilerini listeleyiniz
for p in products:
	print(f"İSİM: {p['name']} - ÜCRET: {p['price']}")

# 2- Ürünlerin fiyatları toplamı nedir?
total = 0
for p in products:
	total = total + p["price"]
print(total)

# 3- Ürünlerden fiyatı en fazla 6000 olan ürünleri gösteriniz.
for p in products:
	if p["price"] < 6000:
		print(p["name"])

# 4- Kullanıcıdan alınan anahtar kelimeyi içeren ürünleri bulunuz
user_input = input("KeyWord = ")

for p in products:
	if (p["name"].find(user_input.lower())> -1):
		print(f"ÜRÜN BİLGİLERİ::\nİSİM: {p['name']} - ÜCRET: {p['price']}")
