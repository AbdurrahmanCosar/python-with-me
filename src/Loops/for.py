# FOR DÖNGÜSÜ İLE BİR GRUP ÜZERİNDE ÇALIŞIRIZ

numbers = [1,2,3,4,5,6,7,8,9]

for i in numbers: # i, sırasıyla numbers listesindeki her bir elemanın yerine geçer
    print(i)

for x in numbers: # Döngü numbers listesindeki eleman sayısı kadar döndüğü için o kadar Hello! yazdırır
    print("Hello!") 


renkler = ["mavi", "kırmızı", "yeşil", "turuncu", "pembe", "mor"]

for renk in renkler:
    print(renk)
    for r in renk: # Liste içerisindeki elemanların harflerini tek tek yazdırır
        print(r)


myTuple = [(1,2), (4,5), (6,7)] # Listenin içinde tuplelar var

for y in myTuple:
    print(y) # Her bir tuple'ı ekrana yazdırır


myDict = {
    "n1":1,
    "n2":2,
    "n3":3,
    "n4":4,
}

for i in myDict:
    print(i) # Bu şekilde sadece key bilgilerini alırız
    print("------")
    print(myDict[i]) # Bu şekilde value bilgilerini alırız

for i in myDict.values(): # Bu şekilde value bilgilerini alırız
    print(i) 


for key, value in myDict.items(): # Bu şekilde key ve value bilgilerini alırız
    print(f"{key} -> {value}")