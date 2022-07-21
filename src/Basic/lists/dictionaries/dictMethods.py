carInformation = {
    "marka" : "Fiat",
    "model" : "Egea",
    "yil" : 2022
}

# Sözlüğe eleman ekleme
carInformation['renk'] = "kırmız" # key = renk, value = kırmız
# Upss! Yanlış yazdık. Peki nasıl düzeltebiliriz?
carInformation['renk'] = "kırmızı" # İşte bu şekilde elemanları düzenleyebilirsiniz.
print(carInformation)

print(carInformation["marka"]) # carInformation sözlüğünde marka bilgisini alırız
print(carInformation.get("marka")) # carInformation sözlüğünde marka bilgisini alırız

print(carInformation.keys()) # sözlükteki keyleri alırız
print(carInformation.values()) # sözlükteki valueleri alırız
print(list(carInformation.items())) # Hem keyleri hem de valueleri bir liste içerisinde alırız

print("renk" in carInformation) # "rebk" bilgisinin carInformation sözlüğünde olup olmadığını sorgularız
print(len(carInformation)) # Sözlüğün kaç elemanlı olduğunu alırız.

carInformation.pop("renk") # "yil" bilgisini sözlükten sileriz
carInformation.popitem() # Son elemanı siler

# Kopyalama işlemi

cI = carInformation # referans olarak kopyalama yapıyoruz

cI["marka"] = "Mercedes"

print(carInformation)
print(cI)
# İkiside aynı adresi temsil ettiği için birinde düzenleme yaparsak otomatik diğerinde de düzenleme olur.
# Eğer referans olarak değil de farklı bir kopyasını çıkarmak istiyorsak
cI = carInformation.copy() # Bu şekilde farklı bir kopyasını çıkarabiliriz.


del carInformation("model") # model bilgisini sileriz
del carInformation # sözlüğü siler
carInformation.clear() # Sözlüğün içindeki tüm elemanları sielr

# Nasıl Update yaparız?

carInformation.update({
    "marka" : "BMW",
    "renk": "Mavi"
})