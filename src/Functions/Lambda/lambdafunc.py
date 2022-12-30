def multiply(a):
    return a ** 2

print(multiply(4))

# lambda <parameters>: <expression>
# (lambda <parameters>: <expression>)(<arguments>)

result = (lambda a: a**2)(5) # Tek satırda bir fonksiyon tanımlıyoruz
print(result)

# Çarpma

multiply = lambda a: a**2
r = multiply(5)
print(r)

# Toplama

toplama = lambda a,b,c: a+b+c
result = toplama(1,5,2)
print(result)

# Ters Çevir

tersCevir = lambda s: s[::-1]
result = tersCevir("Abduley")
print(result)

#########

def myFunc(x):
    return lambda a: a * x

multiply2 = myFunc(2) # göndereceğimiz sayıyı 2 ile çarpar
multiply3 = myFunc(3) # göndereceğimiz sayıyı 3 ile çarpar

result = multiply2(5) # 5'i 2 ile çarpar
print(result)

