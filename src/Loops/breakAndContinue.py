name = "Abdurrahman Coşar"

for harf in name: # name değişkenindeki bütün karakterleri yazdırır
	if harf == "h": # eğer karakterler arasında h varsa...
		break # ... döngüden çıkılır. 
	print(harf)

for harf in name:
	if harf == "d": # eğer karakterler arasında d varsa...
		continue # ... d harfini görmezden gelir ve devam ederiz. d harfi ekrana yazdırılmaz
	print(harf)


i = 0
while i < 5:

	if i == 3:
		break # i' eğer 3 ise döngüden çıkar ve diğer kod blokları çalışır
	print(i) # 0'dan 4'e kadar yazdırır
	i += 1


# WRONG
i = 0

"""
Eğer bu şekilde yaparsak her 3 e geldiğinde atlayacak. Her seferinde atladığı için i asla 5 olmayacak ve döngü sonsuza kadar devam edecek

while i < 5:
	if i == 3:
		continue
	print(i)
	i += 1
"""
# TRUE
i = 0

while i < 5:
	i += 1
	if i == 3:
		continue
	print(i)


# 1-100 arasındaki çift sayıların toplamını yazdırınızç

i = 0
total = 0

while i <= 100:
	i += 1
	if i % 2 == 1:
		continue
	total += i
print(f"Toplam = {total}")
	