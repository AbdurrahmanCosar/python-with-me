# 1 - Faktoriyel fonksiyonu oluşturup fonksyiona gelen değer için hata mesajları verin.

def faktoriyel(num):

    if type(num) is not int:
        raise TypeError("Girdiğiniz değer 'int' olmalıdır!" )

    if (num < 0):
        raise ValueError("Negatif sayıların faktoriyeli hesaplanamaz!")
    
    
    
    r = 1
    for num in range(1, num + 1):
        r *= num
    return r

try:
    print(faktoriyel(2))
except Exception as e:
    print(e)

# 2 - Girilen parola içinde türkçe karakter hatası veriniz
def check_password(password):

    turkish_letter = "üçşöğ"

    for i in password:
        
        if (i.lower() in turkish_letter) or (i in "ıİ"):
            raise ValueError("Parolanız Türkçe Karakter İçeremez")
        
check_password("Merhaba Türkiye")

