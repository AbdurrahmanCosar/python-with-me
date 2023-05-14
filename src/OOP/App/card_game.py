# Kart sınıfı

# Kart sınıfından türetilen her bir nesne bir kart türünü temsil edecek.
# Kart sınıfının tip ve deger isminde 2 instance özelliği olsun. (tip:sinek deger:5)

# sinek5 = Kart("sinek","5")
# karoAs = Kart("karo","A")

# Kart sınıfının kartıGetir() ismindeki instance metodu kart bilgilerini yazdırsın.

# sinek5.kartıGetir() => sinek 5

# Deste sınıfı

# deste1 = Deste()

# kart tipleri   => karo,sinek,kupa,maça
# kart değerleri => A,2,3,4,5,6,7,8,9,10,J,Q,K

# Deste sınıfındaki kartlar listesine 52 kartı for ve list comphension ile ekleyiniz.
# Destede kalan kart sayısı için kartSayisi() isminde bir metot.
# Destedeki kartları karıştırmak için KartlariKaristir() isminde bir metot.
# kartDagit() ismindeki metot belirtilen adet kadar kartı dağıtmalıdır. Destedeki kalan kart sayısına dikkat.
# kartAt() ismindeki metot elden bir kart atmak için kullanılsın.

from random import shuffle

class Kart:

    def __init__(self, type, value):
        self.type = type
        self.value = value

    # def kartGetir(self):
    #     print(f"{self.type} {self.value}")

    def __repr__(self) -> str: # Araştırma
        return f"{self.type} {self.value}"

sinek5 = Kart("sinek","5")
karoAs = Kart("karo","A")

print(sinek5)
print(karoAs)

class Deste:
    cardTypes = ["karo", "sinek", "kupa", "maça"]
    cardValues = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    def __init__(self):
        self.cards = [Kart(c_type, c_value) for c_type in Deste.cardTypes for c_value in Deste.cardValues]

    def __iter__(self):
        return iter(self.cards)
    
    def kartSayisi(self):
        return len(self.cards)

    def kartlariKaristir(self):
        if self.kartSayisi < 52:
            raise ValueError("Deste bozulmadan kartları karıştırabilirsiniz.")
        shuffle(self.cards)

    def kartDagit(self, adet: int):
        kartSayisi = self.kartSayisi()

        if kartSayisi == 0:
            raise ValueError("Bütün kartlar dağıtıldı.")
        adet = min([kartSayisi, adet])

        kartlar = self.cards[-adet:]
        self.cards = self.cards[:-adet]
        return kartlar
            

    def kartAt(self):
        return self.kartDagit(1)[0]

d = Deste()

d.kartAt()

for i in d:
    print(i)
