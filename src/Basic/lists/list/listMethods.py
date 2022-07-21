numbers = [1,5,8,57,2,7,5,5]
letters = ['a', 'b','e','s','a','y','z']

# En Büyük ve En Küçük Elemanı Alma
response = min(numbers) # En küçük sayıyı alır.
response = max(numbers) # En büyük sayıyı alır.
response = min(letters) # Alfabetik olarak en küçük değeri alır. Kelime varsa uzunluk olarak en kısayı alır.
response = max(letters) # Alfabetik olarak en büyük değeri alır. Kelime varsa uzunluk olarak en uzunu alır

# Listeye Yeni Eleman Ekleme
numbers.append(169) # Listeye bu şekilde eleman ekliyoruz.

numbers.insert(3,6) # 3 numaralı indexe "6" elemanını ekliyoruz.
numbers.insert(-1,50) # -1. indexe "50" sayısını ekliyoruz.
numbers.insert(len(numbers), 210) # Listenin en sonuna "210" elemanını ekliyoruz.

# Listeden Eleman Silme
numbers.pop() # Listenin en sonundaki elemanı siler.
numbers.pop(-1) # -1. indexteki elemanı siler.

numbers.remove(8) # Liste içerisinden 8 değerini siler.
letters.remove('a') # Lise içerisinde "a" değerini siler.

# Sıralama
numbers.sort() # Sayıları küçükten büyüğe doğru sıralar.
letters.sort() # Harfleri alfabetik olarak sıralar.

# Büyükten Küçüğe Sıralama
numbers.sort() # Önce küçükten büyüğe sıralıyoruz
numbers.reverse() # Daha sonra ters çeviriyoruz.

# Liste İçinde Arama
print(numbers.count(5)) # Listede kaç tane 5 değeri olduğunu alıyoruz.
print(letters.count("a")) # Listede kaç tane "a" değeri olduğunu alıyoruz.

numbers.index(5) # 5 değerinin liste içerisinde kaçıncı indexte olduğunu alıyoruz.
letters.index("a") # a değerinin lsite içerisinde kaçıncı indexte olduğunu alıyoruz.

# Liste Elemanlarını Silme
numbers.clear() # Liste içerisindeki bütün elemanları siliyoruz.
letters.clear()