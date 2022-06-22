
"""
Palindromik bir sayı her iki şekilde de aynı şekilde okunur.
İki basamaklı iki sayının çarpımından yapılan en büyük palindrom 9009 = 91 × 99'dur.
3 basamaklı iki sayının çarpımından oluşan en büyük palindromu bulun.
"""

# 1.YOL

liste = []
for i in range(100,1000):
    for j in range(100,1000):
        carpım = i*j
        if str(carpım)==str(carpım)[::-1]:
            liste.append(carpım)
print(max(liste))        
    

# 2.YOL

# def palindromik(sayi):
#     str_sayi = str(sayi)
#     str_ters_sayi = str_sayi[::-1]
#     if str_sayi == str_ters_sayi:
#         return True
#     else:
#         return False
    
# buyuk_palindrom = 0
# a,b=0,0
# for i in range(100,1000):
#      for j in range(100,1000):
#          if palindromik(i*j) and i*j > buyuk_palindrom:
#              a,b = i,j
#              buyuk_palindrom = i*j
            
# print(f"{a} x {b} = {buyuk_palindrom}")        
    
        