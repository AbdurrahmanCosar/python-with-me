
"""
message = "Merhaba" şeklinde default parametre tanımlıyoruz
eğer fonksiyon çalıştırılırken ikinci parametre girilmezse varsayılan olarak Merhaba yazacak
"""
def sayHi(name, message = "Merhaba"): 

    print(f"{message}, {name}")

sayHi("Abduley", "Selam")
sayHi("Abduley")


"""
Eğer fonksiyon çalıştırılırken herhangi bir parametre girilmezse "Good Morning :) User" yazdırır
"""
def goodMorning(user = "User", goodmorning = "Good Morning :)"):
    
    print(f"{goodmorning} {user}")

goodMorning()


#! DİKKAT

"""
default parametre tanımladığınız değişken her zaman sonda olmalıdır.

! WRONG - YANLIŞ
def myFunc(user = "user", message):
    ...

* TRUE - DOĞRU
def myFunc(message, user = "user")
    ...

veya

def myFunc(user = "user", message = "Hello")

"""

#------------------
#* Bir fonksiyonu başka bir fonksiyona default parametre olarak gönderme

def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def islem(a, b, func = toplama): # 3. parametre girilmezse fonksiyon olarak her zaman toplama'yı alacak
    return func(a, b)

result = islem(5, 7, toplama) # Fonksiyonu çağırmıyoruz. toplamanın referansını aldığımız için () koymaya gerek yok