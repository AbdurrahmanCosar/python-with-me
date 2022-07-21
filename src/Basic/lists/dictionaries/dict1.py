"""
Python collection veri tiplerinden olan dictionary 
yani sözlük veri yapısı key ve value şeklinde verileri saklayabileceğimiz bir veri yapısıdır. 
Dictionary veri yapısı Json veri yapısına oldukça benzerdir.
Dictionary liste elemanlarına key ve value değerlerine göre ulaşıp elemanlar üzerinde güncelleme yapabiliriz. 
"""

#! key - value

myDict = {
    # key : "value"
    "book" : "kitap",
    "apple" : "elma",
    "car" : "araba",
    "dictionary" : "sözlük"   
}

# Value ve Keyleri alma
print(myDict["book"]) # myDict sözlüğünden "book" elemanını valuesini alıyoruz. Bize "kitap" yazdırır
print(myDict.keys()) # myDict sözlüğündeki bütün keyleri yazdırır
print(list(myDict.keys())) # myDict sözlüğündeki bütün keyleri bir liste içerisinde yazdırır



# Sözlük içine sözlük tanımlayabiliriz.
students = {
    1 : {"name" : "Onur", "age": 15, "university" : False}, 
    2 : {"name" : "Çınar", "age": 16, "university" : False}, 
    3 : {"name" : "Hasan", "age": 22, "university" : True} 
}

print(students[1]["name"]) # 1 numaralı öğrencinin ismini alıyoruz
print(students[3]["university"]) # 3 numaralı öğrenci üniversite öğrencisi mi?

# Sözlük içine liste tanımlayabiliriz
player1 = {
    "name": "Yunus",
    "level" : 100,
    "scores" : [400,500,700]
}

print(player1["scores"]) # Bize oyuncunun skorlarının bulunduğu listeyi döndürür
print(max(player1["scores"])) # Bize oyuncunun en yüksek skorunu döndürür
print(min(player1["scores"])) # Bize oyuncunun en düşük skorunu döndürür

