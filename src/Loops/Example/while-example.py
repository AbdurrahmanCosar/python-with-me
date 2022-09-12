numbers = [4,6,7,8,923,23,31,45,565,7,67,98,75,32]

# 1 - numbers listesini while ile ekrana yazdırın.

i = 0
while i<len(numbers):
	print(numbers[i])
	i += 1

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın
baslangicDegeri = int(input("Başlangıç: "))
bitisDegeri = int(input("Bitiş: "))

i = baslangicDegeri

while i < bitisDegeri:
	i+= bitisDegeri
	if i%2 == 1:
		print(i)

# 3- 1-100 arası sayıları azalan şekilde yazdırın
i = 100
while i > 0:
	print(i)
	i -= 1

# 4 - Kullanıcıdan alacağınız 5 sayıyı ekrana sıralı bir şekilde yazdırın

numbers = []
i = 0
while i<5:
	number = int(input("Sayı: "))
	numbers.append(number)
	i +=1

numbers.sort()
print(numbers)