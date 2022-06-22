"""Üçgen sayıları dizisi, doğal sayıların eklenmesiyle oluşturulur. 7 Bu yüzden inci üçgen numarası olacaktır 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. ilk on koşulları şöyle olacaktır:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

İlk yedi üçgen sayısının çarpanlarını sıralayalım:

 1 : 1
 3 : 1,3
 6 : 1,2,3,6
10 : 1,2,5,10
15 : 1,3,5,15
21 : 1,3,7,21
28 : 1,2, 4,7,14,28
28'in beşten fazla böleni olan ilk üçgen sayı olduğunu görebiliriz.

Beş yüzden fazla böleni olan ilk üçgen sayısının değeri kaçtır?"""
"""
1‘den n‘e kadar ardışık doğal sayıların toplamını veren sayılara Üçgen sayılar denir.
n sayma sayısı olmak üzere nx(n+1)/2 şeklinde yazılabilen sayılardır
"""

# import math

# def bolen_sayisi(sayi):
#     bolen = 1
    
#     for i in range(2,int(math.sqrt(sayi) + 1)): # karekökünü aldığımız için kontrol işlemini yarıya düşürüyoruz. (bolen*2)
#         if sayi % i == 0:
#             bolen += 1
#     if (math.sqrt(sayi)).is_integer():
#         return (bolen*2) - 1
#     return bolen*2 # örneğin 105 saysının bir böleni 3 iken 3 ile çarpılan ve bölen konumunda olan 35 de old. için 2 ile çaprtık.

# n = 1
# while True:
#     number = (n*(n+1))/2
#     if bolen_sayisi(number) >= 500:
#         print(int(number))
#         break
#     n += 1
     


# *************************************************************************************************
# import numba as nb
# import math

# @nb.njit
# def trinum2(n, dik):
#     if n in dik:
#         return dik[n]
#     else:
#         ans = n + trinum2(n-1, dik)
#         dik[n] = ans
#         return ans

# @nb.njit
# def divisors3(n):
#     divs = 0
#     for i in range(int(math.sqrt(n)),0,-1):
#         if n % i == 0:
#             divs += 2
#     return divs

# @nb.njit
# def search2(maks):
#     count = 1
#     no_of_divs = 0
#     trianglenumber = 1
#     while no_of_divs < maks:
#         no_of_divs = divisors3(trianglenumber)
#         if no_of_divs >= maks:
#             return trianglenumber, no_of_divs
#         count += 1
#         trianglenumber += count
#     return trianglenumber, no_of_divs

# print(search2(500))


# ******************************************************************************************
    
    
# from sympy import divisor_count

# n = 1
# m = 1
# nb_fac = 500
# while divisor_count(m) < nb_fac:
#     n += 1
#     m += n
# print(m)
    
# *******************************************************************************************

# The approach to solve this problem is to realize that every natural number can be expressed
# as the product of all the factors to their exponents (occurences) power:
# N = A^a * B^b * ... * I^i, for example:
# 28 = 2^2 * 7^1 = 28.
# Also, the number of factors a number has is equal to this formula:
# (a+1)(b+1)...(i+1). In the previous example it would be (2 + 1)(1 + 1) = 6
# In conclusion, we have to find the exponents (number of occurences) for each factor
# and then apply the given formula above to find the total number of factors

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Bu sorunu çözme yaklaşımı, her doğal sayının ifade edilebileceğini anlamaktır.
# tüm faktörlerin üslerinin (oluşmalarının) gücünün ürünü olarak:
# N = A^a * B^b * ... * I^i, örneğin:
# 28 = 2^2 * 7^1 = 28.
# Ayrıca, bir sayının çarpanlarının sayısı şu formüle eşittir:
# (a+1)(b+1)...(i+1). Önceki örnekte (2 + 1)(1 + 1) = 6 olurdu
# Sonuç olarak, her faktör için üsleri (oluşma sayısı) bulmalıyız.
# ve ardından toplam faktör sayısını bulmak için yukarıdaki formülü uygulayın

# import math


# def decompose(number):
#     """ Decompose a number by its prime factors and return 
#         a list of the exponents (number of occurences) for each factor 
        
#         Bir sayıyı asal çarpanlarına göre ayrıştırın ve döndürün
#         her faktör için üslerin bir listesi (oluşma sayısı)
#     """
#     exponents = []
#     i = 1

#     # Loop until we have factored the number completely
#     # Sayıyı tamamen çarpanlarına ayırana kadar döngü
#     while True:
#         exponent = 0
#         i += 1

#         # Break condition, the number has been factored completely
#         # Kopma durumu, sayı tamamen çarpanlara ayrıldı
#         if number == 1:
#             break

#         # No prime factors exist beyond the square root of the number
#         # Sayının karekökü dışında asal çarpan yoktur
#         if i > int(math.sqrt(number) + 1):
#             exponent += 1
#             exponents.append(exponent)
#             break

#         # Decompose the number as much as possible by each prime factor
#         # Sayıyı her bir asal faktöre göre mümkün olduğunca ayrıştırın
#         if number % i == 0:
#             while number % i == 0:
#                 exponent += 1
#                 number = int(number / i)

#         # Add the exponent of the prime factor
#         # Asal çarpanın üssünü ekleyin
#         if exponent:
#             exponents.append(exponent)

#     return exponents


# def calculate_factors(exponents):
#     """ Receive a list of numbers and returns the result based on the
#         total divisors formula: (a+1)(b+1)...(n+1)
        
#         Sayıların bir listesini alın ve sonuca göre sonucu döndürür.
#         toplam bölen formülü: (a+1)(b+1)...(n+1)
#     """
#     total_divisors = 1
#     for exponent in exponents:
#         total_divisors = total_divisors * (exponent + 1)

#     return total_divisors


# triangle_num = 1
# natural_num = 1

# # Stop looping once we find the triangular number over 500 factors
# # 500 faktörün üzerindeki üçgen sayıyı bulduğumuzda döngüyü durdur
# while True:
#     natural_num += 1
#     triangle_num += natural_num     # get next triangular number # sonraki üçgen sayıyı al
#     exponents = decompose(triangle_num)     # get the list of exponents for this number # bu sayının üslerinin listesini al
#     total_factors = calculate_factors(exponents)    # total factors for this triangular number 
#                                                     # bu üçgen sayı için toplam faktör

#     # Break condition, we found the problem number
#     # Kırılma koşulu, sorun numarasını bulduk
#     if total_factors > 500:
#         break

# print("500'den fazla faktörün ilk üçgen sayısı", triangle_num)

#  **********************************************************************************


from math import sqrt

div = 0
count = 0
tri = 0
while div <= 500:
    count += 1
    tri += count
    div = 0
    for i in range(1, int(sqrt(tri)) + 1):
        if tri % i == 0:
            div += 2
print(tri, div)
 
