# min() fonksiyonu ile sayısal olarak en düşük veya alfabetik olarak en sonda olanı bulabiliriz
# max() fonksiyonu ile sayısal olarak en büyük veya alfabetik olarak en sonda olanı bulabiliriz

# min() ve max() fonksiyonlarını lambda fonksiyonu aracılığı ile sözlüklerde kullanabiliriz

numbers = [65,41,34,17,3,98,55]
letters = ["a", "z", "y", "u"]
name = ["abduley", "ufuk", "kemal"]

result = min(numbers) # numbers listesindeki en küçük elemanı alırız
result = max(numbers) # numbers listesindeki en büyük elemanı alırız

result = min(letters) # letters listesindeki alfabetik olarak en baştaki harfi alırız
result = max(letters) # letters listesindeki alfabetik olarak en sondaki harfi alırız

result = min(name) # Alfabetik olarak en baştaki ismi alır
result = max(name) # Alfabetik olarak en sondaki ismi alır

result = min([len(n) for n in name]) # Karakter uzunluğu en kısa ismi alır
result = max([len(n) for n in name]) # Karakter uzunluğu en uzun ismi alır

result = min(name, key = lambda n: len(n)) # Karakter uzunluğu en kısa ismi alır
result = max(name, key = lambda n: len(n)) # Karakter uzunluğu en uzun ismi alır

computers = [
    {"title" : "lenovo", "price": 30000},
    {"title" : "casper", "price": 28000},
    {"title" : "asus", "price": 15000}
]

result = min(computers, key = lambda computer: computer["price"]) # computers'in içindeki sözlüklerde price değeri en küçük olanı alır
result = max(computers, key = lambda computer: computer["price"])["title"] # computers'in içindeki sözlüklerde price değeri en büyük olanın title'ını alır

print(result)