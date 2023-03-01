num = 50

numbers = [10,50, 190]

student = {
    "name" : "Abduley",
    "number" : "169",
    "grades" : [90,95,80]
}

def toplama(*args):

    for i in args:
        if type(i) is not int:
            raise TypeError("Toplama fonksiyonunun içine gönderilen değerler int olmalıdır")

    return sum(args)