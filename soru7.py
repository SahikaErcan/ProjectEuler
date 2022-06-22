"""
İlk altı asal sayıyı listeleyerek: 2, 3, 5, 7, 11 ve 13, 6. asal sayının 13 olduğunu görebiliriz.

10001. asal sayı kaçtır?
"""
# import math

# sayac = 0

# def asal_mı(sayi):
#     if sayi == 2:
#         return True
#     else:
#         for i in range(2,int(math.sqrt(sayi)+1)):
#             if sayi % i == 0:
#                 return False
#                 break
#         return True
    

# i = 2
# while True:
#     if asal_mı(i):
#         sayac += 1
#     if sayac == 10001:
#         print(i)
#         break
#     i += 1

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2. YOL ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ # # 

import time

start_time = time.time() # başlama zamanı


# **************************** ASAL MI KONTROLÜ *******************************
def is_prime(n): 
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    
    limit = int(n ** 0.5) + 1 # sayının karekökünün 1 fazlasını alıyoruz. işlemi hızlandırıyoruz.
    
    for i in range(3, limit, 2): # çift sayılar asal olmayacağı için onları atlıyoruz. (3,5,7,9,11,13,15....)
        if n % i == 0:
            return False
    return True

# *****************************************************************************
# **************************** ASALLARI SAYALIM *******************************
def next_prime(sayac_limit):
    yield 2
    sayac = 1
    sayi = 3
    while True:
        if is_prime(sayi): # sayı asal mı
            yield sayi # asal sa sayıyı döndür. 
            sayac += 1 # asal bulduğumuz için asalları sayıyoruz. Sayaç 1 artar.
            if sayac == sayac_limit: # sayac = 10001 olduğunda yani 10001. asal sayıyı bulduğumuzda
                return  # döngüden çık
        sayi += 2  # sayiyi 2 arttırıyoruz ki tek sayılara ulaşalım. 2 dışında çift asal sayı yoktur.

# *****************************************************************************

sayac_limit = 10001

for item in next_prime(sayac_limit):
    pass

print(item)

print("--- %s seconds ---" % (time.time() - start_time)) # ne kadar sürede bulduğunu kontrol ediyoruz.

    