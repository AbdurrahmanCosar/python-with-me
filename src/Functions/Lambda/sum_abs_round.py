# -- SUM --
numbers = [5,16,45,123]

result = sum(numbers) # numbers listesindeki bütün elemanları toplar
result = sum(numbers, 10) # numbers listesindeki bütün elemanları toplar ve üzerine +10 ekler


products = [
    {"title": "ayakkabı", "price": 2000},
    {"title": "mont", "price": 5000},
    {"title": "kulaklık", "price": 2600}
]

total_price = sum([product['price'] for product in products]) 
product_count = len([product for product in products if product['price']>0])
result = total_price / product_count

# -- ROUND --

result = round(10.2) # en yakın sayıya yuvarlar (10)
result = round(10.5) # (10)
result = round(10.6) # (11)

result = round(1.484848484848) # 1'e yuvarlar
result = round(1.484848484848, 2) # 1'e yuvarlar ve sayının noktadan sonraki 2 basamağı alır
result = round(1.494848484848, 2) # Burada noktadan sonraki ilk 3 basamakta 494 var ve bu 49'a daha yakın olduğu için 1.49 olarak alır



# -- ABS --

num = -30

result = abs(num) # ABS sayıları pozitif değerlere çevirir

num = -30.51
result = abs(num)


print(result)