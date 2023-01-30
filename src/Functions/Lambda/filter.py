age = [15, 17, 24, 32]

# List
result = list(filter(lambda x: x>=18, age)) #age listesindeki 18'e eşit veya 18'den büyük olanlarını filtreler
print(result)

# For loop
for i in filter(lambda x: x>=18, age):
    print(i)

    
name = ["ada", "ali", "caner", "murat", "berk"]



""" name listesinde 0. indexi 'a' olan elemanları bir liste içerisine büyük harfle yazdırıyoruz """

# filter(lambda n: n[0] == 'a', name) -> name listesindeki 0. indexi 'a' olan elemanları alıyoruz
# map(lambda n: n.upper()) -> filer ile aldığımız elemanların her birini tek tek gezerek büyük harfle yazdırıyoruz

result = list(map(lambda n: n.upper(), filter(lambda n: n[0] == 'a', name)))
print(result)


users = [
    {"name" : "onur", "comment" : ["comment1", "comment2"]},
    {"name" : "özgür", "comment" : []},
    {"name" : "çınar", "comment" : ["comment1"]}
]


sonuc = list(map(lambda u: u["name"].title(), filter(lambda u: len(u["comment"])>0, users)))
#or
sonuc = [user["name"].title() for user in users if len(user["comment"])>0]
print(sonuc)