
def toplam(*args): # Değişken sayıda parametre göndereceğimizi bildirmek için * ekliyoruz
    # args yerine başka bir şey de yazabiliriz
    
    print(type(args)) # bize tuple değeri döndürür
    
    r = 0
    for i in args:
        r += i
    return r
        
print(toplam(5,10,15,20,25)) # bu parametreler fonksiyon içerisinde bir liste olarak değerlendiriliyor