
#* 1 - Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

def question1(kelime, kackez):
    for i in range(kackez):
        print(kelime)

question1("Merhaba", 3)


#* 2 - Dikdörtgenin alan ve çevresini hesaplayan fonksiyonu yazınız.

def question2(uzun_kenar, kisa_kenar):

    cevre_hesapla = 2 * (uzun_kenar + kisa_kenar)
    alan_hesapla = uzun_kenar * kisa_kenar

    print(f"Dikdörtgenin çevresi: {cevre_hesapla}cm \nDikdörtgenin alanı {alan_hesapla}cm")

question2(10,5)

#* 3 - Yazı Tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü ile)

def question3(cevap):

    yazi_tura = ["yazı", "tura"]

    import random
    sonuc = random.choice(yazi_tura)

    if cevap.lower() == sonuc:
        print("Tebrikler doğru tahmin")
    else:
        print("Maalesef yanlış")
question3("Yazı")

#* 4 - Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.

def question4(sayi1, sayi2):

    for sayi in range(sayi1 ,sayi2 + 1):
        if sayi > 1:
            for i in range(2, sayi):
                if sayi % i == 0:
                    break
            else:
                print(sayi)
question4(5, 10)


#* 4 - Kendisine gönderilen bir sayının tam bölenlerini liste şeklinde döndüren fonksiyonu yazınız.

def question4(sayi):
    tam_bolenler = []

    for i in range(2 ,sayi):
        if sayi % i == 0:
            tam_bolenler.append(i)

    return tam_bolenler

print(question4(15))