
"""
Pozitif tamsayılar kümesi için aşağıdaki yinelemeli dizi tanımlanır:

n → n /2 ( n çifttir)
n → 3 n + 1 ( n tektir)

Yukarıdaki kuralı kullanarak ve 13 ile başlayarak aşağıdaki diziyi oluşturuyoruz:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Bu dizinin (13'ten başlayıp 1'de biten) 10 terim içerdiği görülebilir. Henüz kanıtlanmamış 
olmasına rağmen (Collatz Problemi), tüm başlangıç ​​sayılarının 1'de bittiği düşünülmektedir.

Bir milyonun altındaki hangi başlangıç ​​sayısı en uzun zinciri oluşturur?

NOT: Zincir bir kez başladığında terimlerin bir milyonun üzerine çıkmasına izin verilir.
"""
import time

past_numbers = dict()  # Boş bir sözlük listesi oluşturuyoruz. # Geçmiş sayıları tutabilmek için # sayı, kaç adım ürettiği

def collatz(number,past_numbers): 
    given = number  # mevcut degeri belirliyoruz. Hangi sayıyı denediğimizi unutmamak için
    steps = 1        # adım -- sayac
    while number != 1: # sayı 1 olmadığı sürece işlelere devam et
        if number in past_numbers: # geçmiş sayılar listesinin içerisinde yeni sayı var mı? Yani daha önce bu sayıyı denedik mi?
            steps += past_numbers[number] - 1 # eğer varsa adımı sayının indexinin 1 eksiği kadar ilerlet.
# Örneğin sayımız 13 ise 13-1 arttıracak. Sayı başlangıçta adım 1 diye aldık eğer 1 çıkarmazsak o sayıyı 2 kez almış olacağız.
            break # böylece gereksiz işlem yapmaktan geri kalmış olacağız.
        if number % 2 == 0:
            number //= 2
            steps += 1
        else:
            number = 3 * number + 1
            steps += 1
    past_numbers[given] = steps # geçmiş sayılar listesine tuttuğumuz sayıyı (given) ekliyoruz. # sayac : sayı sözlüğü oluşuyor. # 13 sayısının 10 adımdan oluştuğunu ekliyor.
   # print(past_numbers) # 13 sayısı için uyguladığımızda Çıktı: 
    return steps
""" print(past_numbers) # 13 sayısı için uyguladığımızda Çıktı: 
    {1: 1}
    {1: 1, 2: 2}
    {1: 1, 2: 2, 3: 8}
    {1: 1, 2: 2, 3: 8, 4: 3}
    {1: 1, 2: 2, 3: 8, 4: 3, 5: 6}
    {1: 1, 2: 2, 3: 8, 4: 3, 5: 6, 6: 9}
    {1: 1, 2: 2, 3: 8, 4: 3, 5: 6, 6: 9, 7: 17}
    {1: 1, 2: 2, 3: 8, 4: 3, 5: 6, 6: 9, 7: 17, 8: 4}
    {1: 1, 2: 2, 3: 8, 4: 3, 5: 6, 6: 9, 7: 17, 8: 4, 9: 20}
    {1: 1, 2: 2, 3: 8, 4: 3, 5: 6, 6: 9, 7: 17, 8: 4, 9: 20, 10: 7}
    {1: 1, 2: 2, 3: 8, 4: 3, 5: 6, 6: 9, 7: 17, 8: 4, 9: 20, 10: 7, 11: 15}
    {1: 1, 2: 2, 3: 8, 4: 3, 5: 6, 6: 9, 7: 17, 8: 4, 9: 20, 10: 7, 11: 15, 12: 10}
"""
    

wanted = 1 # bizdden istenen sayı
max_ = 1  # max adım sayısı
baslangıc = time.time()
for i in range(1,1000000):
    move_count = collatz(i, past_numbers) # adım sayısı
    if move_count > max_:
        max_ = move_count
        wanted = i # max adım sayısını veren sayıyı wanted a atıyoruz.
bitis = time.time()
print(wanted)
print("Çözülme süresi : " , bitis - baslangıc)
#  *****************************  2. YOL  *************************************

# def adim_sayisi(deger):

#     sayac = 1
    
#     while deger > 1:
#         if deger % 2 == 0:
#             deger /= 2
#         else:
#             deger = deger*3 + 1
#         sayac += 1
#     return sayac   

# # Burada ki " key=lambda x: x[0] " her bir öğeyi dizideki 0. indeksinde ki değerle karşılaştırır.
# print(max([(adim_sayisi(i), i) for i in range(0,1000000)], key=lambda x: x[0])) 


# ******************************************************************************
        
# print(adim_sayisi(13))

# sayi_listesi = []

# en_buyuk = 0

# for i in range(1,1000000):
#     terim = adim_sayisi(i)
    
#     if terim > en_buyuk:
#         en_buyuk = terim
#         sayi_listesi.append(i)
# print(max(sayi_listesi))
        