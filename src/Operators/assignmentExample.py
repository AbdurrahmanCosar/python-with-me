a, b, c = 3, 7, 13

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile a,b,c toplamının farkı nedir?
x = int(input("x : "))
y = int(input("y : "))

result = (x * y) - (a, b, c)
print(result)

# 2 - c'in b'ye kalansız bölümünü hesaplayın
print(c // b)

# 3 - a,b,c toplamının mod 3'ü nedir?
result(a + b + c ) % 3
print(result)

# 4 - b'nin a. kuvvetini hesaplayınız.
print(b ** a)

# 5 - a, *b, c = numbers işlemine göre c'nin küğü kaçtır
numbers = 1,5,7,10,3
a, *b, c = numbers
print(c ** 3)

# 6 - a, *b, c = numbers işlemine göre b nin değerlerinin toplamı kaçtır
a, *b, c = numbers
print(b[0] + b[1] + b[2])