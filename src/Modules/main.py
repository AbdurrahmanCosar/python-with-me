import module as module # Bu şekilde başka modülleri dosyamıza çağırabiliriz


# Bir modül import ederek o modül içeriğini import ettiğimz dosyada kullanabiliriz
# Bu sayede projemiz büyüdükçe oluşacak olan karmaşanın önüne geçebiliriz


print(module.num)
print(module.toplama(10,20))


#! -----Modüle bir isim verme-----

import module as m
# Bu şekilde modül içerisindeki bütün elemanlara ulaşabiliriz
print(m.numbers)


#! -----Modül içerisinden bir eleman çekme-----

from module import student
# Bu şekilde modül içerisinden sadece student değerini alıyoruz
# Dolayısıyla kullanırken module yazmamıza gerek yok. Direkt student çeklinde kullanabiliriz
# virgül(,) ile ayırarak birden fazla elemanı çağırabiliriz
# Örn:  from module import student, num, toplama

print(student)

#! -----Modül içerisindeki her şeyi import etme-----

from module import *
# * koyarak bütün elemanları import ederiz.
# Bu sayede module ismini kullanmamıza gerek yok
print(numbers)