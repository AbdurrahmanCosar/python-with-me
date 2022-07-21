"""
Tuple aslında list veri yapısına benzer.
List değişebilir(mutable) bir yapıya sahipken Tuple (immutable) ise değişemez . 
List yapısı dizisel bir yapı tuple ise bir eşlem(mapping) yapısıdır. 
Tuple içerisinde oluşturulan veriler değiştirilemez veya silinemez.
Bu da Tuple'ı daha performanslı hale getirir. 
"""



list_ = [1,2,3] # List
tuple_ = (1,2,3) # Tuple
tuple_2 = 1,'yedi',True # Tuple

print(list_[1]) # Listenin 1. elemanı
print(tuple_[1]) # Tupleın 1. elemanı

list_[0] = 5 # Listelerde çalışır
tuple_[0] = 5 # Tupleda çalışmaz

list_.append(3) # Listeye bu şekilde eleman ekleyebiliriz
tuple_.append(3) # Tuplelara eleman ekleyemeyiz.

print(tuple_.count(1)) # 5 tuple da kaç tane var bu şekilde alabiliriz.
# Not: Burada 1 rakamı 2 tane var olarak görünür çünkü True'da 1 değeri döndürür.


print(len(list_)) # Listenin uzunluğu
print(len(tuple_)) # Tupleın uzunluğu


# Listeyi Tuple'a çevirme
_newTuple = tuple([5,6,7])
print(type(_newTuple)) 