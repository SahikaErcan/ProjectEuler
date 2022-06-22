
"""
1'den 5'e kadar olan sayılar bir, iki, üç, dört, beş kelimelerle
yazılırsa, toplamda 3 + 3 + 5 + 4 + 4 = 19 harf kullanılır.

1'den 1000'e (bin) kadar olan tüm sayılar kelimelerle yazılsaydı
kaç harf kullanılırdı?
"""

sayilar = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',
              8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve',
              13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',
              17:'seventeen', 18:'eigtheen', 19:'nineteen', 20:'twenty',
              30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy',
              80:'eigthy', 90:'ninety', 100:'hundred', 1000:'thousand'}

topla = 0

# 1 ile 19 arası

for i in range(1,20):
    kelime = sayilar[i]
    topla += len(kelime)
    
# 20 ile 99 arası

for i in range(20,100,10):
    for j in range(0,10):
        kelime = sayilar[i] + sayilar[j]
        topla += len(kelime)
        
# 100 ile 999 arası

for i in range(1,10):
    for j in range(0,20):
        if j == 0:
            kelime = sayilar[i] + sayilar[100] # iki yüz , üç yüz,... , dokuz yüz gibi
        else:
            kelime = sayilar[i] + sayilar[100] + "and" + sayilar[j] # üç yüz on beş : Three hundred and fifteen 
        topla += len(kelime)
    
    for k in range(20,100,10):
        for j in range(0,10):    
            kelime = sayilar[i] + sayilar[100] + "and" + sayilar[k] + sayilar[j] # iki yüz otuz altı : two hundred and thirty six
            topla += len(kelime)
        
        
kelime = sayilar[1] + sayilar[1000] # 1000 : one thousand
topla += len(kelime)
               
print(topla)



# 2. YOL

# from num2words import num2words

# karakter = ""

# for i in range(1,1001):
#     kelime = num2words(i, lang="en_GB")
#     kelime = kelime.replace(" ","")
#     karakter += kelime

# karakter = karakter.replace(" ","")
# karakter = karakter.replace("-","")

# print(len(karakter))










