"""
Her yerde print kullanamayız. Örneğin web geliştirme yapıyorsak return etmemiz gerekir
Bu return etmeyi fonksiyonun içerisinde yapıyoruz. Daha sonra fonksiyonumuzu bir değişkene atıyoruz veya
direkt print'in içerisinde çalıştırıyoruz
"""
def toplam():
    return f"Toplam = {10 + 20}"

a = toplam()
print(a)
print(2022 - 118)
# Veya

print(toplam())

# -------------------

# Mini App
dogum_tarihi = int(input("Doğum Tarihinizi Giriniz: ")) # Kullanıcıdan doğum tarihini alıyoruz.

def yil(): # Şimdiki yılı alacağımız bir fonksiyon tanımlıyoruz.
    import datetime # Datetime modülünü çağırıyoruz.
    return datetime.datetime.now().year # Datetime modülü içerisinden yıl methodunu çağırıyoruz.

def yasHesapla(): # Yaş hesaplayacağımız fonksiyonu tanımlıyoruz.

    """Eğer doğum tarihi bulunduğumuz yıldan fazlaysa veya 1904'ten küçükse başka bir cevap return ediyoruz."""
    if dogum_tarihi >= yil() or dogum_tarihi <= 1904:
        return "Lütfen geçerli bir doğum tarihi giriniz!"

    islem = yil() - dogum_tarihi # Bulunduğumuz yıldan kullanıcının doğum tarihini çıkarıyoruz.
    return f"Yaşınız = {islem}" # Kullanıcının yaşını bildiren bir cevap return ediyoruz.

yas_hesaplayici = yasHesapla() # Yaş hesapla fonksiyonunu bir değişkene atıyoruz

print(yas_hesaplayici) # Atadığımız değişkeni konsola yazdırıyoruz
