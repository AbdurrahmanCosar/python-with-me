numbers = [1,2,3,4,5,25,41,96,73]

# 1- numbers listesindeki her bir elemanı yazdırın.
for number in numbers:
	print(number)

# 2- numbers listesindeki hangi sayılar 5'in katıdır?
for number in numbers:
	if number % 5 == 0:
		if number == 5:
			continue
		print(f"5'in katı olan sayılar: {number}")

# 3- numbers listesindeki sayıların toplamı kaçtır?
total = 0
for number in numbers:
	total = total + number
print(total)

# 4- numbers listesindeki çift sayıların karesini alınız.
for number in numbers:
	if number % 2 == 0:
		print(number, number*number)

products = ["iphone 8", "iphone X", "iphone XR", "samsung 510"]
# 5- products listesindeki tüm ürünlerin 2. karakterlerini ekrana yazdırın.
for product in products:
	print(product[1])

# 6- product listeindei içinde iphone geçen kaç ürün vardır?
count = 0
for product in products:
	index = product.find("iphone")
	if index >-1:
		count += 1