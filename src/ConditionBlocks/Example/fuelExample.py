# Bir aracın yakıt tipine göre (benzine, dizel) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan bir uygulama yapınız 


benzinFiyat = 21.48
dizelFiyat = 23.51

ortalama_yakit_tuketimi = float(input("100 km'deki ortalama yakıt tüketimi: "))
gidilecek_yol = float(input("Gidilecek yol kaç km: "))
yakit_tipi = input("Yakıt tipiniz nedir?: ")

toplam_yakit_tuketimi = gidilecek_yol * (ortalama_yakit_tuketimi / 100)

if yakit_tipi == "benzin":
    toplam_yakit_ucreti = benzinFiyat * toplam_yakit_tuketimi
elif yakit_tipi == "dizel":
    toplam_yakit_ucreti = dizelFiyat * toplam_yakit_tuketimi
else:
    print("Geçerli bir yakıt türü giriniz.")


if toplam_yakit_ucreti != 0:
    print(toplam_yakit_ucreti)
