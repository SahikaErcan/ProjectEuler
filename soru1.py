# 3 veya 5 e tam bölünen 1000 den küçük sayıların toplamı

"""def euler1(i):
    if i % 3 == 0 or i % 5 == 0:
        return True
    else:
        return False
    
sum = 0
for i in range(1,1000):
    if euler1(i):
        sum += i
print(sum)"""

# **************** ÇÖZÜM-2 *****************************


print(sum([i for i in range(1,1000) if i%3 == 0 or i%5 == 0]))