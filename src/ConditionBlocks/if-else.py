# Koşul Blokları - Condition Blocks


#-------------
# soru
    # işlem
# diğer
    # işlem
#-------------
# 1.soru 
    # 1.soru
        # işlem
    # diğer
        #işlem
# 2. soru
    # işlem
# diğer
    # işlem
#-------------


input_user_name = input("Username: ")
input_password = input("Password: ")


user_name = "abdurrahmancosar"
password = "123456"


# 1. YÖNTEM
isLoggedin = (input_user_name == user_name) and (input_password == password) 

if (isLoggedin):
    print("Welcome")  
    # Kullanıcının girdiği şifre ve kullanıcı adı doğruysa konsola "Welcome" yazdıracak

else:
    print("Kullanıcı adı veya Parolanız hatalı!")
    # 1. koşul sağlanmadığında yani eğer kullanıcı adı ve şifre yanlış ise bu blok çalışacak.


# 2. YÖNTEM

if (input_user_name == user_name) and (input_password == password):
    print("Welcome")  
    # Kullanıcının girdiği şifre ve kullanıcı adı doğruysa konsola "Welcome" yazdıracak

else:
    print("Kullanıcı adı veya Parolanız hatalı!")
    # 1. koşul sağlanmadığında yani eğer kullanıcı adı ve şifre yanlış ise bu blok çalışacak.


# 3. YÖNTEM
if input_user_name == user_name: # Kullanıcı adı doğru ise bu blok çalışır
    if input_password == password: # Şifre doğru ise bu blok çalışır
        print("Hi user!") # Şifre ve Kullanıcı adı doğru ise konsola "Hi user!" yazdırır
    else: # Şifre yanlış ise bu blok çalışır
        print("Şifre yanlış") # Şifre yanlış ise konsola "Şifre yanlış" yazdırır
else: # Kullanıcı adı yanlış ise bu blok çalışır
    print("Kullanıcı adı yanlış!") # Kullanıcı adı yanlış ise konsola "Kullanıcı adı yanlış!" yazdırır