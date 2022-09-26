# Fonksiyonlara nasıl parametre eklenir?

def sayHi(name): # Fonksiyonun içine ekleyeceğimiz parametreleri parantezlerin içine yazıyoruz
    return "Hi " + name


run_function = sayHi("Abduley") 
print(run_function)
# Fonksiyonu çalıştırırken içerisine parametre ekledik
# Bu parametre name değişkeninin içine kopyalanacak


def toplama(sayi1, sayi2): # toplama adındaki fonksiyonumuzun içerisine 2 tane parametre giriyoruz
    return sayi1 + sayi2 # Sonuç olarak bu 2 parametrenin toplamını döndürüyor bize

toplama_islemi = toplama(5, 10)  
print(toplama_islemi)

"""
Fonksiyonu çalıştırıken içerisine 2 parametre giriyoruz.
Eğer içerisine parametre girmezsek veya eksik girersek:
    toplama() missing 2 required positional arguments: 'sayi1' and 'sayi2'
hatasını alırız

"""