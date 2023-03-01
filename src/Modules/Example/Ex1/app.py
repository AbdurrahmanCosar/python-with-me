"""

    module1 (db) : urunler (name, id , fiyat)
    module2 (methods) : urunEkle(), urunGuncelle(), urunleriGetir()
    moudle3 (app):

        yeni ürün ekleme => urunEkle("iphone 11 pro", 7000)
        ürün güncelleme => urunGuncelle(1, "iphone 12 pro", 8000)
        ürünleri listele => urunleriGetir()

"""

from methods import *

urunEkle("Lenovo", 20500)
urunGuncelleme(1, "iPad")
urunleriGetir()

