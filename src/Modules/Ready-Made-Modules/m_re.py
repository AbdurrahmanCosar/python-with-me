import re

result = dir(re)


# re module

str = "Learn Python with me"

result = re.findall("Python", str)
result = re.split(" ", str)
result = re.sub(" ", "-", str)

rsearch = re.search("Module", str)
result = rsearch.span()
result = rsearch.start()
result = rsearch.end()
result = rsearch.group()
result = rsearch.string

# regular expression

#! [] arasına yazılan bütün karakterler aranır

"""
[abc] =>    a       : 1 match
            ac      : 2 match
            Python  : no mathes

"""

result = re.findall("[abc]", str)  # abc karakterlerini str içinde arar
result = re.findall("[sat]", str)

"""
[a-e]   => [abcde]
[1-5]   => [12345]
[0-39]  => [01239]


[^0-9]  => rakam olmayan karakterler
[^abc]  => abc dışındaki karakterler


"""

result = re.findall("[a-z]", str) # a'dan z'ye olan bütün karakterleri arar
result = re.findall("[1-5]", str) # 1'den 5'e olan bütün karakterleri arar

result = re.findall("[^2-5]", str) # 2'den 5'e olmayan bütün karakterleri arar
result = re.findall("[a-p]", str) # a'dan p'ye olan karakterler dışında arar

"""

. - Herhangi bir tek karakteri belirtir

    .. =>   a       : No matches
            ab      : 1 match
            abc     : 1 match
            abcd    : 2 matches

"""

result = re.findall("...", str)
result = re.findall("Py..on", str)

"""
^ - Belirtilen karakter ile başlyor mu?

    ^a =>   a       : 1 match
            abc     : 1 match
            bac     : No match

"""

result = re.findall("^L", str)

"""
$ - Belirtilen karakter ile bitiyor mu?

    $a =>   a       : 1 match
            cba     : 1 match
            bac     : No match

"""

result = re.findall("e$", str)
result = re.findall("me$", str)

"""
* - Bir karakterin sıfır ya da daha fazla sayıda olmaını kontrol eder

    ma*n =>     mn        : 1 match
                man       : 1 match
                maaan     : 1 match
                main      : No match ( a'nın arkasına n gelmiyor)
"""

"""
{} - Karakter sayısını kontrol eder

    al{2} => a karakterinin arkasına l karakteri 2 kez tekrarlamalı
    al{2, 3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı
    [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar
"""

reslut =  re.findall("a{2}", str)
reslut =  re.findall("[0-9]{2}", str)

"""
| - altenatif seçeeklerden birinin gerçekeşmesi gerekir

    a | b => a ya da 

        cde =>  no match
        ade =>  1 match
        acdbea =>  3 match
"""

reslt = re.findall("a|b", str)

"""
() - Gruplmak için kullanılı

    (a|b|c)xz => a,b,c karakterlerinden sonra xz gelmelidir
"""