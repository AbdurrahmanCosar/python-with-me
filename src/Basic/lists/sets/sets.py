#Setler indexlenemez ve sıralanamazlar


fruits = {"elma","muz","portakal","armut" } # Setler bu şekilde tanımlanır
result = "elma" in fruits # fruits setinin içinde elmayı sorgularız

fruits.add("karpuz") # Bu şekilde yeni eleman ekliyoruz
fruits.update(["vişne", "kavun"]) # Birden fazla elemanı bu şekilde ekleyebiliriz.

result = len(fruits) # fruits setinin uzunluğunu alırız

fruits.remove("mandalina") # KeyError alırız çünkü sette öyle bir eleman yok
fruits.discard("mandalina") # Eğer mandalina varsa siler, yoksa hata vermez


fruits.pop() # İçerisinden rastgele eleman siler. 
fruits.clear() # Bütün set elemanları silinir

result = fruits
print(result) # Elemanları rastgele bir sırayla yazdırır.

#-------------

# 2 seti birleştirme
meyveler = {"erik", "kayısı"}
sebzeler = {"bezelye", "soğan"}

r = meyveler.union(sebzeler) # union ile liste elemanlarını birleştirebiliriz
print(r)
# Not: Eğer eleman tekrarlanmışsa o elemanı sadece 1 kere yazdırır.

"""
Ne zaman set kullanmalıyız?
-> İndexleme, sıralama önemli değilse
-> Eleman eklemek istiyorsak fakat olan elemanı değiştirmek istemiyorsak
-> Eğer eleman eklemek istemiyorsanız tuple kullanabilirsiniz.
"""