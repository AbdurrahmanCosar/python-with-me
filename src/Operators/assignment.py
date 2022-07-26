# a = 5
# b = 10
# c = 20

a, b, c = 5, 10, 20

#a, b = b, a

a += 5       # a = a + 5
a -= 5       # a = a - 5
a *= 5       # a = a * 5
a /= 5       # a = a / 5
a %= 5       # a = a % 5
a **= 5      # a = a ** 5
a //= 5      # a = a // 5

values = (1, 2, 3, 4, 5)

#a, b, c = values
# a, b, *c = values # a = 1, b = 2, kalan değerler c'ye aktarılır
a, *b, c = values # a = 1, c = 5, kalan değerler 5'ye aktarılır

print(a, b, c)