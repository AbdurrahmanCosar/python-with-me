# Kendisine gönderilen 2 sayıdan hangisi büyük bulan fonksiyon yazınız.
def fnc1(a, b):
    if a > b:
        print(f"En büyük sayı {a}")
    elif b > a:
        print(f"En büyük sayı {b}")
    else:
        print("Sayılar eşit")
        
fnc1(10, 15)


# Kendisine gönderilen bir string bilgi içinde her karakter kaçar kez tekrarlanmış bulunuz

def fnc2(string):
    return { letter: string.count(letter) for letter in string}

print(fnc2("Selamlar"))
    

# kendisine gönderilen list, command, position ve value bilgilerine göre liste üzerinde güncelleme yapınız
    # [1,2,3], ("add, remove"), ("beginning | end"), value
    # list_operation([1,2,3],"add","end","4") => [1,2,3,4]
    # list_operation([1,2,3],"remove","end","1" => [2,3]
    
    
def update_list(liste, command, position, value = None):
    if (command == "remove" and position == "end"):
        return liste.pop()
    elif (command == "remove" and position == "beginning"):
        return liste.pop(0)
    elif (command == "add" and position == "end"):
        liste.append(value)
        return liste
    elif (command == "add" and position == "beginning"):
        liste.insert(0, value)
        return liste

re = update_list([1,2,3], "add", "end", "2")
print(re)
    
# kendisine gönderilen renk isimlerinin içinde "blue" rengi varsa True döndüren fonksiyonu yazınız
def fnc4(*args):
    if "blue" in args:
        return True
    return False

r = fnc4("purple","pink","yellow","blue","red","green","gray")
print(r)