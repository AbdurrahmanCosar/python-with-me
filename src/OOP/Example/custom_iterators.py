# Kendi iteratorumuzu oluşturalım


numbers = [1,2,3,4,5]
string = "Hello World"

def my_for(iterable, func):
    
    iterator = iter(iterable) # Dışarıdan gelen iterable objeyi bir iteratöre dönüştürüyoruz

    while True:
        try:
            num = next(iterator) # Bir sonraki elemanı alıyoruz
            func(num) # Dışarıdan çağırılan fonksiyonun içine her seferinde sonraki elemanı gönderiyoruz
        except StopIteration: # Listenin dışına çıktığımız zaman bu hatayı alırız
            break

my_for(numbers, print)
my_for(string, print)

