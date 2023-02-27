try: # Try hata oluşabilecek kod blokları için kullanılır
    x = 10
    y = int(input("Bir sayı giriniz: "))
    print(x + y)
except: # Eğer Try'ın içerisinde bir hata oluşursa bu blok devreye girer ve ekrana Bilinmeyen bir hata oluştu yazdırır
    print("Bilinmeyen bir hata oluştu")