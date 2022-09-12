myList = [1, 2, 3, 4, 5]
myList2 = ["a", "b", "c", "d", "e", "f"]
myList3 = [100, 200, 300, 400, 500]

# Liste yapılarını birleştirmek için zip() kullanırız.

print(list(zip(myList, myList2, myList3))) # Index numaralarına göre 3 listeyi birbiriyle birleştirir
# Fazladan karakter varsa bu gözardı edilir



#* For döngüsünde kullanmak istersek:

for item in zip(myList, myList2):
    print(item) # Her bilgi bir tuple nesnesi içerisinde birleştirilir


#* Elemanlar arasında  tek tek dolaşabilmek için:
for a, b, c in zip(myList, myList2, myList3):
    print(a, b, c) # 3 listedeki elemanları index numarasına göre sıra sıra eşleştirir