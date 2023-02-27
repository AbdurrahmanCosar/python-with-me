try:
    x = int(input("X: "))
    y = int(input("Y: "))

    print(x / y)
except ZeroDivisionError: # Sadece bir sayıyı 0'a bölmeye çalışırken aldığımız hatada çalışır!
    print("Bölmek istediğiniz sayı 0 olamaz!")

except ValueError: # X veya Y sayısal bir değer olmadığı zaman bu blok çalışır
    print("X ve Y sayısal değer olmalıdır")

except (SyntaxError, IndentationError): # Farklı hataları tek bir except bloğuda bu şekilde kullanabiliriz
    pass

except Exception as e: # as e ile karşılaştığımız herhangi bir hatanın detaylı bilgisini alabiliriz.
    print(e)

else: # Eğer except bloklarının hiçbiri çalışmazsa else bloğunu kullanabiliriz
    print("Çalışıyor!")



# Mini App

while True:

    try:
        num1 = int(input("Num1 : "))
        num2 = int(input("Num2 : "))

        print( num1 + num2)

    except Exception as e:
        print("Bir hata oluştu\n{}".format(e))
    
    else:
        break

    finally: # Bu blok, hata olsa da olmasa da çalışır. Örneğin bir veri tabanı bağlatısı yaptık. Bağlantıyı kapatacağımız zaman bu bloğu kullanırız.
        print("Finally bloğu çalıştı")