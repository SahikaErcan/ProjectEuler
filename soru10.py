""" 10'un altındaki asal sayıların toplamı 2 + 3 + 5 + 7 = 17'dir.

İki milyonun altındaki tüm asal sayıların toplamını bulun. """

def asal_mi(sayi): 
    if sayi == 2: 
        return True
    if sayi % 2 == 0 or sayi < 2:
        return False
  # sayının karekökünün 1 fazlasını alıyoruz. işlemi hızlandırıyoruz.
    for i in range(3, int(sayi ** 0.5) + 1, 2): # çift sayılar asal olmayacağı için onları atlıyoruz. (3,5,7,9,11,13,15....)
        if sayi % i == 0:
            return False
    return True
topla = 0
for i in range(2,2000000):
    if asal_mi(i):
        topla += i   
print(topla)

