# 1 - Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz
sayi = int(input("Sayi: "))

if (sayi > 50) and (sayi < 100):
    print(f"Girdiğiniz sayı: {sayi}. Sayı 50 ve 100 arasındadır")
else:
    print(f"Girdiğiniz sayı: {sayi}. Sayı 50 ve 100 arasında değildir")

# 2 - Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz

number = int(input("Number: "))
if (number > 0) and (number % 2 == 1):
    print("Sayı tek ve pozitifdir")

# Username ve Parola bilgileri ile giriş kontrolü yapınız

input_username = input("username: ")
input_password = input("password: ")

username = "abduleyy"
password = "121231231"

if username == input_username:
    if password == input_password:
        print("Giriş başarıyla yapıldı!")
    else: 
        print("Şifre Yanlış")
else:
    print("Kullanıcı adı yanlış")

