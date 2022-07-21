languages = ["Python","Java","C++","Javascript"]


response = languages # Liste elemanlarını yazdırır.
response = type(languages) # Liste elemanlarının türünü yazdırır.
response = languages[0:2] # 0'dan 1. elemana kadar alır.
response = languages[2:] # 2. elemandan sonuna kadar alır
response = languages[-4:-1] # -4. elemandan -2. elemana kadar yazdırır

response = languages[-1] = "Vuejs" # -1. elemanı "Vuejs" ile değiştirir
response = len(languages) # Listenin uzunluğunu alırız.
response = languages + ["Angular", "React"] # Listenin sonuna "Angular ve React" ekler.

del languages[0] # 0. elemanı listeden siler
del languages # Listeyi siler

response = languages
"""Bunu yazarsak hata alırız çünkü 
aşağıda listeyi yazdırmaya çalışıyor ve yukarıda listeyi sildiğimiz içinyazdıracak bir lsite bulunmuyor."""

print(response)