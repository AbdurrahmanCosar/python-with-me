# *args = tuple
# **kwargs = dict

def user(**kwargs):
    print(type(kwargs))
    
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    
user(username = "abduley", email="minidev@gmail.com") # Bu bir dictionary oluşturur. Değişken sayıda parametre girebiliriz



def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
    
myFunc(10,20,30,40,50,60, name = "abduley", country = "Turkiye")
# ilk 3 argüman a, b, c parametrelerine karşılık gelir
# daha sonra yazdıklarımız args parametresine karşılık gelir
# daha sonra key = value şeklinde gönderdiğimiz argümanlar kwargs parametresine karşılık gelir
    