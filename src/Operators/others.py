# Identity Operator: is

x = y = [1, 2, 3]
z = [1, 2, 3]

print(x==y) # True
print(x==z) # True
print( x is y) # True
print( x is z) # False

a = [1, 2, 3]
b = [2 ,4]

del a[2]
b[1] = 1
b.reverse()

print(a==b)
print(a is b)
print(a is not b)

# Membership Operator: in

q = ["apple", "banana", "pear"]
print("banana" in q) # liste içerisinde var mı?

name = "Abduley"
print("u" in name) # True 
print("u" not in name) # True 