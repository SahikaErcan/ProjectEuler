
"""
2^15 = 32768 ve rakamları toplamı 3 + 2 + 7 + 6 + 8 = 26'dır.

2^1000 sayısının rakamları toplamı kaçtır ?
"""

# sayi = pow(2, 1000)
# toplam = 0
# while True:
#     kalan = sayi % 10
#     sayi //= 10
#     toplam += kalan

#     if sayi <= 0:
#         break
# print(toplam)



#  2.YOL

number = 2**1000
sum = 0

for i in str(number):
    sum += int(i)
print(sum)


