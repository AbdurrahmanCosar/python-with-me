def toplama(num1, num2):
    return num1 + num2

def cikarma(num1, num2):
    return num1 - num2

def islem(fnc1, fnc2, islem_adi):

    if islem_adi == "toplama":
        print(fnc1(10, 5))
    elif islem_adi == "cikarma":
        print(fnc2(7,4))
    else:
        print("geçersiz")


islem(toplama, cikarma, "toplama")