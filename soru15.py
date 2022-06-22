"""
2×2 ızgaranın sol üst köşesinden başlayarak ve yalnızca
sağa ve aşağı hareket edebilen, sağ alt köşeye giden tam
6 yol vardır.
20 × 20 ızgarada böyle kaç rota var?
"""

# *****************************************************
# 1.YOL

"""  4 x 3 lük ızgarada;
sağ 1 olsun
aşağı 0 olsun
  1001101
  1100101
  .
  .
  gibi başlangıç ve bitiş yolları çizebiliriz.
Bu durumu formülize edecek olursak.
7 değer : 7!
1 in takrar sayısı : 4!
0 ın tekrar sayısı : 3!

# Toplam yol sayısı / Devam edenler
                7! / 4! x 3!
""" 

def fact(x):
    factorial = 1
    for i in range(1,x+1):
        factorial*=i
    return factorial

# soruda bizen 20 x 20 ızgaranın çıktısını istiyor
# 20 sağ 20 aşağı gitmemiz lazım. Toplam: 40! eder.

steps = fact(40) / (fact(20)*fact(20))
print(int(steps))



# *****************************************************
# 2.YOL

# import itertools 
# # içerisinde permütasyon ve kombinasyon işlemlerini barındıran bir kütüphane 

# liste = []

# for i in range(1,6):
#     liste.append(0) # aşağı
#     liste.append(1) # sağ
    
# permutations = itertools.permutations(liste,10)
# # ancak bunun içerisinde tekrar edenlerde var
# # bunun için 2. bir liste oluşturyoeuz.

# yollar = []

# for permutation in list(permutations):
#     if permutation in yollar:
#         continue
#     else:
#         yollar.append(permutation)
    
# print(len(yollar))

# 40! i hesaplamakda zorlandı
# Yüksek bir değer ve hafıza için uygun bir yol değil
# yine de küçük değerler için denenebilir.