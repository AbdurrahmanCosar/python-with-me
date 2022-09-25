
#* Fonksiyon tanımlarken def kullanıyoruz

# Örnek:  def isim()
def hello():
    print("Hello")

# Fonksiyon çağırırken fonksiyonun adını yazıp sonuna parantez açıp kapatıyoruz
hello()


def sayilar(): # "sayilar" adında bir fonksiyon tanımlıyoruz

    # Yapılacak işlemi yazıyoruz
    for i in range(11): 
        print(i)

# Fonksiyonu çalıştırıyoruz
sayilar()


a = 10
b = 20

def topla():
    print(a + b)

topla()
