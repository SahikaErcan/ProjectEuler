"""
2520, 1'den 10'a kadar olan sayıların her birine kalansız bölünebilen en küçük sayıdır.

1'den 20'ye kadar olan sayıların tamamına tam bölünebilen en küçük pozitif sayı kaçtır ?


->  Bu soru bir ebob ekok sorusudur. Python da ebob 'un hazır bir fonksiyonu vardır.
Bu fonksiyon 'gcd' dir. 
-> Eğer elimizde 2 sayı varsa o sayıların ebob ve ekoklerının çarpımı sayıların kendi
çarpımlarına eşittir.
     EBOB x EKOK = a x b
Bu yapıdan yola çıkarak ekok a erişim sağlayabiliyoruz.
     EKOK = (a x b) / EBOB
"""


import math
import functools

def gcd(x,y): 
    return math.gcd(x, y)  # gelen sayıların EBOB unu döndürür.

def lcm(x,y):    # EKOK
    return (x * y) // gcd(x,y) # // bölümün tam kısmını almamızı sağlar

liste = range(1,21)

result = functools.reduce(lcm, liste)
print(result)





