# 1 - Girilen 2 sayıdan hangisi büyüktü ? 
sayi1 = int(input("Sayi 1 : "))
sayi2 = int(input("Sayi 2 : "))

print(sayi1 > sayi2)

# 2 - Girilen bir sayının tek mi, çift mi olduğunu yazdırın.
sayi = int(input("Sayi giriniz: "))
result = (sayi1 % 2 == 0)# Çift ise True, Tek ise False
print(result)

# 3 - Girilen bir sayının negatif pozitif durumunu yazdırın.
print(sayi > 0) # Sayı pozitif ise True, Negatif ise False

# 4 - Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
email = "info@gencyazilimci.com"
password = "12345"

enterEmail = str(input("Email : "))
enterPassword = str(input("Password : "))

emailCheck = (enterEmail == email) # Eşleşiyor ise True
passwordCheck = (enterPassword == password) # Eşleşiyor ise True

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

vize1 = float(input("Vize 1: "))
vize2 = float(input("Vize 2: "))
final = float(input("Final : "))

ortalama = (((vize1 + vize2) /2) * 0.6) + (final * 0.4)
print(f"not ortalamanız {ortalama} ve dersten geçme durmunuz {ortalama>=50} ")