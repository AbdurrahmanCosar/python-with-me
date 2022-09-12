# ---- RANGE ----

r = range(10) # 0'dan 9'a kadar bir rakamları içeren bir liste oluşturur
r = range(5, 10) # 5'den, 10'a kadar rakamları içeren bir liste oluşturur fakat 10 dahil değil
r = range(50, 100, 10) # 50'den 100'e kadar 10ar 10ar gider fakat 100 dahil değil
r = range(70, 30, -1) # Sondan başa gider. Büyük sayı başta olmak zorunda

response = list(r)
print(response)

for i in range(19):
	print(i)

for x in range(100,200):
	if (x % 2 == 0):
		print(i)
