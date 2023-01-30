sayilar = [ 1, 2, 3, 5, 9, 7]
kareleri = []

# XXX
for sayi in sayilar:
    kareleri.append( sayi ** 2)
    
# VVV
def kareAl(sayi):
    return sayi ** 2



# map(func, iterable)
result = list(map(kareAl, sayilar)) """ Sayilar listesinin içinde tek tek gezerek her bir elemanı kareAl fonksiyonuna gönderir. Sonucu görebilmek için listeye çeviriyoruz"""

# with Lambda
result = list(map(lambda sayi: sayi ** 2, sayilar)) # Lambda fonksiyonunu da kullanabiliriz.
print(result)

# to Integer
str_sayilar = ["1", "2", "3", "4"]

r = list(map(int, str_sayilar)) # str_sayilar listesindeki her bir elemanı integer'a çeviriyoruz
print(r)

# Karakter uzunlukları
students = ["Ahmet", "Ali", "Caner", "Hayri"]
s = list(map(len, students))
print(s)

# dict
users = [
    {"name" : "Murat", "soyad" : "Yılmaz"},
    {"name" : "Kemal", "soyad" : "Yılmaz"}
]

result = list(map(lambda x: x["name"]), users)
print(result)

