
"""

Aşağıda while döngüsü ile num değişkenini her arttırdığımzda 
elde ettiğimiz bir sayıyı liste içerisinde tutup daha sonra o listeyi kullanıcıya döndürerek
bellekte yer işgal etmektense, yield kullanarak elde ettiğimiz veriyi direkt kullanıcıya ulaştırıyor
ve sonraki veriye odaklanyoruz

Bu sayede bellekte yer işgal etmiyoruz

! Önceki veriye tekrar ulaşamayız

! Yield, aynı return mantığında kullanıcıya değer döndürür fakat program sonlanmaz

! Generator objesi döner ve buobjeyi next() metodunu kullanarak ihtiyacımız olduğu
! kadarını bellek içerisinde yer işgal etmeden geri döndürebiliriz

! Iterator'dür

"""


def counter(max):

    num = 1

    while 1 <= max:
        yield num # Elde ettiğimiz değeri kullanıcıya döndürür ve sonraki değere odaklanırız
        num += 1


iterator = counter(10)

print(help(iterator)) # __iter__ metoduna sahiptir 


result = next(iterator)
print(result)


# For döngüü içerisinde kullanabiliriz
for i in iterator:
    print(i)


# Listeye çevirme
result = list(iterator)

generator = (i for i in range(1,11)) # Bu şekilde bize generator objesi döndürür
list_object = [i for i in range(1,11)] # Bu şekilde bize liste döndürür