nums = []

# Bunu Kullanmak Yerine
for i in range(10):
    nums.append(i)

# Bunu kullanabiliriz

# [ expression for item in list ]
nums = [i for i in range(10)]

print(nums)



#---------------

name = "Abduley"

r = [ n.upper() for n in name]
print(r)