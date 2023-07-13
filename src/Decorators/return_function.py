def us_al(number):

    def inner(power):
        return number ** power
    
    return inner


two = us_al(2)
print(two(3))



def yetki_sorgula(page):
    def inner(role):
        if role == "Admin":
            return "{0} rolü {1} sayfasına ulaşabilir.".format(role, page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz.".format(role, page)
        
    return inner

user1 = yetki_sorgula("Products")
print(user1("Admin")) 