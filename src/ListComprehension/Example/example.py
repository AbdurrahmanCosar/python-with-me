fiyatlar = [1000, 2000, 3000, 4000, 0, 5000]
vergiler = []

# * NORMAL *

for fiyat in fiyatlar:
    if fiyat > 0:
        vergiler.append(fiyat * 1.18)
    else:
        print("Vergi Hesaplanamadı!")


# * Comprehension *

vergiler = [fiyat * 1.18 for fiyat in fiyatlar if fiyat > 0]
vergiler = [fiyat * 1.18 if fiyat > 0 else "Vergi Hesaplanamadı!" for fiyat in fiyatlar]


print(vergiler)


result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))

result = [(x, y) for x in range(3) for y in range(3)]

print(result)