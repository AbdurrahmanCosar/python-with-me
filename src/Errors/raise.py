# Raise ile hiçbir hata olmamasına rağmen hata oluşturabilirsiniz.

def colorize(color):

    colors = ("blue", "red", "orange", "green")

    if type(color) is not str:
        raise TypeError("renk bir string olmalıdır!")
    
    if color not in colors:
        raise ValueError("Girmiş olduğunuz değer renkler listesinde bulunmuyor!")
    
    print("Girmiş olduğunuz renk: {}".format(color))

try:
    colorize(10)
except (TypeError, ValueError) as err:
    print(err)
    