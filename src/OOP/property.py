class Product:
    def __init__(self, name, price, descrption):
        self.name = name
        self._price = price # Private değişkenlerin başına _ koyuyoruz
        self.description = descrption

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError()

    @property
    def short_decription(self):
        return self.description[:10]


p = Product("iphone", 40000, "iphone'un yeni modeliyle birlkte birçok yeni özellik geldi")
print(p.price)

p.price = 3000
print(p.price)

print(p.short_decription)