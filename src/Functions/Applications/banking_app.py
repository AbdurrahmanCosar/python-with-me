Abduley = {
    "ad": "Abduley",
    "hesapNo": "1235451432",
    "bakiye": 3000,
    "ekHesap": 1000
}

Abdurrahman = {
    "ad": "Abdurrahman",
    "hesapNo": "1237451432",
    "bakiye": 2000,
    "ekHesap": 500
}


def para_cek(kullanıcı, miktar):
    ekBakiye = kullanıcı.get("ekHesap")
    
    onceki_bakiye = kullanıcı.get("bakiye")
    yeni_bakiye = onceki_bakiye - miktar
    
    if onceki_bakiye >= miktar:
        
        kullanıcı.update({"bakiye": yeni_bakiye})
        print(kullanıcı.get("bakiye"))
    else:
        if onceki_bakiye + ekBakiye >= miktar:
            
            yeni_bakiye = onceki_bakiye + ekBakiye - miktar
            kullanıcı.update({"bakiye": yeni_bakiye})
            kullanıcı.update({"ekHesap": 0})
            print(kullanıcı.get("bakiye"))
        else:
            print("Yeterli bakiyeniz bulunmuyor")

def para_yatir(kullanıcı, miktar):
    onceki_bakiye = kullanıcı.get("bakiye")
    yeni_bakiye = onceki_bakiye + miktar
    
    kullanıcı.update({"bakiye": yeni_bakiye})
    print(kullanıcı["bakiye"])

def bakiye_sorgula(kullanıcı):
    print(kullanıcı["bakiye"])
    
def banking(kullanıcı, islem, miktar = 0):
    
    if islem == "Para Çek":
        para_cek(kullanıcı, miktar)
    elif islem == "Para Yatır":
        para_yatir(kullanıcı, miktar)
    elif islem == "Bakiye Sorgula":
        bakiye_sorgula(kullanıcı)
        
banking(Abdurrahman, "Para Çek", 2200)