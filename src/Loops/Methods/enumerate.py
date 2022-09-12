cars = ["bmw", "ferrari", "mercedes"]

"""
index = 0
for car in cars:
    print(f"{index + 1} - {cars[index]}")
    index += 1

Index numaralarını liste elemanlarına ulaşmak için kullanırız
"""

# -------- ENUMERATE --------
cars = ["ford", "toyota", "tesla"]


obj1 = enumerate(cars)

print(type(obj1)) # Tür olarak "enumerate" döner.
print(list(obj1)) # Liste olarak yazdırırsak her elemana bir index numarası verir.

for i in enumerate(cars):
    print(i) # Her bir elemanı tuple nesnesi şeklinde index numaralarıyla beraber yazdırır

for index, value in enumerate(cars):
    print(f"{index + 1} - {value}") # İndex ve value olarak ekrana yazdırır
    # Index + 1 yazdık çünkü 1'den başlasın istiyoruz


# + 1 yazmak yerine şu şekilde de yapabiliriz
for index, value in enumerate(cars, 1): # Buraya 1 koyarak 1 den başlamasını sağlarız
    print(f"{index} - {value}") 