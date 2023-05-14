numbers = [1,2,3,4,5,]
"""
# Iterable
numbers listesi __iter__ adında bir özel fonksiyon içerir
bu iter fonksyionu bizim bu elemanlar arasında tek tek gezmemizi sağlar

"""

for num in numbers:
    print(num)

# Iterble bir obje içerisinde tek tek dolaşmamız için bir Iterator'e ihtiyacımzı var
# For döngüsü bizim için bunu sağlıyor ama biz yinede kendi iteratorümüzü oluşturalım


iterator = iter(numbers) # Bu şekilde iterable bir objeyi, bir iterator'e çevirebiliyoruz


print(next(iterator)) # next metodu içerisine bir iterator alır.
# ve bir sonraki elemanı yazdırır

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

#! Eğer listede bulunan eleman sayısını geçersek bize StopIteration hatasını döndürür