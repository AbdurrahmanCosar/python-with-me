# __init__


class Product:
    """
    Ekstra methodlar tanımlayabiliriz
    Class içine bir özellik eklemek için kullanılır
    """

    def __init__(self, _name, _price, isActive = False): # init fonksiyonu default olarak self parametresi alıyor
        self.name = _name
        self.price = _price
        self.isActive = isActive
        print("Nesne Oluşturuldu")

    #! Türetilen her nesne için çalışacak bir fonksiyondur


p1 = Product("Samsung S10", 5000) # self için parametre göndermiyoruz
p2 = Product("iPhone 12", 8000)

print(p1.name, p1.price, True)
print(p2.name, p2.price, False)

"""
Self: Üretilecek olan nesneyi kasteder
Bir nesne ürettiğimiz zaman self onun yerini tutar
Self yukarıdaki p1 ve p2 yerine geçer

"""