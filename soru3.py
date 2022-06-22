# 1.YOL

def asal_mı(sayi):
    if sayi>1:
        for i in range(2,int(sayi*0.5) +1):
            if (sayi % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False # 1 asal değildir

### asal_carpan = list()
sayi = 600851475143
en_buyuk_asal = 1
for i in range(2,int(sayi/2)+1):
    if (sayi % i) == 0 and asal_mı(i):
        sayi/= i
        print(sayi)
        en_buyuk_asal = i
print(en_buyuk_asal)
###         asal_carpan.append(i)
### print(max(asal_carpan))



# *********************************************

# 2.YOL

# def sayi(sayi):
#   bolen = 2
#   while sayi != 1:
#     if sayi / bolen == 1:
#       print(bolen)
#       break
#     elif sayi % bolen == 0:
#       sayi /= bolen
#     else:
#       bolen += 1
# sayi(600851475143)





# ********************************************

# 3.YOL

# sayi = 600851475143
# i = 2
# while i*i < sayi:  
#     while sayi % i == 0:
#         sayi /= i        
#     i += 1
# print(int(sayi))
        