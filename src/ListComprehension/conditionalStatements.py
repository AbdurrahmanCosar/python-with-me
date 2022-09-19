"""
*Normal*

for item in list:
    if (condition):
        expression


*Comprehension ile*

[ expression for item in list if condition]
"""


nums = [1,4,6,123,51,32,576,54]
re = []


for num in nums:
    if num % 2 == 0:
        re.append(num)


# Comprehension
re = [ num for num in nums if num % 2 == 0 ]
re = [ num if num % 2 == 0 else "tek sayı" for num in nums ]


print(re)