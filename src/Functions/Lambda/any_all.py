# -- ALL --
"""
All fonksiyonu kendisine verilen değerler arasında tek tek gezer
ve tüm değerlerin True olduğu durumlarda bize True değerini döndürür
"""
# Eg.

result = all([True, True, False]) # False dönecektir çünkü bütün değerler True değil!


# -- ANY --
"""
Any fonksiyonu kendisine verilen değerlerin arasında herhangi biri
True olduğunda bize True döndürür.
"""
# Eg.

result = any([True, False, False]) # True dönecektir çünkü herhangi bir değerin True olması yeterli!


#? Fark - Different

# And => True and True => True => All()
# Or => True or False => True => Any()


# Example

numbers = [0,1,2,4,6,7,9,17,15,42,52,13,42]

result = all([number % 2 == 0 for number in numbers])
print(result) # Bütün sayılar çift ise True dönecektir