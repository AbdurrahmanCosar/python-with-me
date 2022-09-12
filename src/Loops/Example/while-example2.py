# Kullancıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayınız
# ** ürün sayısını kullancııya sorun
# ** dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun
# ** ürün ekleme işlemi bttiğinde ürünleri ekranda while ile listelerin

i = 0
adet = int(input("Kaç adet ürün ekleyeceksiniz?: "))
urunler = []

while i < adet:
	urunAdi = input("Ürün adı: ")
	fiyat = input("Ürün fiyatı: ")
	urunler.append({
		"urunAdi": urunAdi,
		"fiyat" : fiyat
		})
	i += 1

a = 0
while a < len(urunler):
	
	print(f"Ürün Adı: {urunler[a]['urunAdi']} - Ürün Fiyatı: {urunler[a]['fiyat']}")
	a += 1