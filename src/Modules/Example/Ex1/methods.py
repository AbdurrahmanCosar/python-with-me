from db import products

#*yeni ürün ekleme => urunEkle("iphone 11 pro", 7000)
#*ürün güncelleme => urunGuncelle(1, "iphone 12 pro", 8000)
#*ürünleri listele => urunleriGetir()

def urunleriGetir():
    
    for i in products:
        print(f"({i.get('id')}), {i.get('name')}, {i.get('price')}TL \n")


def urunEkle(name:str, price:int):

    if type(price) is not int:
        raise TypeError("Ürün fiyatları int olmalıdır!")
    



    
    new_product = {"id": len(products) + 1 ,"name": name, "price": price}
    products.append(new_product)
    
def urunGuncelleme(id:int, name:str = None, price:int = None):

    try:
        for product in products:
            if product["id"] == id:
                name_ = product["name"] if name == None else name 
                price_ = product["price"] if price == None else price 
                product["name"] = name_
                product["price"] = price_
                break
        

    except KeyError:
        print("Aradığınız ürün bulunamadı!")
    except Exception as e:
        print(e)
