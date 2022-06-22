# -*- coding: utf-8 -*-
"""
Aşağıdaki üçgenin yukarıdan aşağıya maksimum toplamını bulun:
"""

ucgen = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

satirlar = ucgen.split("\n")
dizi = []
for satir in satirlar:
    sayilar = satir.split(" ")
    dizi.append(sayilar)

for i in range(0,len(dizi)):
    for j in range(0,i+1):
        if dizi[i][j]=="00": # i ve j . index 00 karakterli ise 0 karakterine dönüştür.
            dizi[i][j]="0"
        elif len(dizi[i][j])!=1:
            if dizi[i][j].startswith("0"): # i ve j. index in 1. karakteri 0 ise 0 karakterine göre parçala.
                dizi[i][j]=dizi[i][j].strip("0") # 0 ı yok et.
        dizi[i][j]=int(dizi[i][j]) # int e çeviriyoruz.

for i in range(len(dizi)-1,-1,-1):
    for j in range(0,i):
        dizi[i-1][j] += max(dizi[i][j], dizi[i][j+1])
        # burada satırda ne yaptığımızı anlayalım
        #dizi[4-1][0] += max(dizi[4][0], dizi[4][0+1])
        #dizi[3][0] += max(dizi[4][0], dizi[4][1]) mantık bu şekilde

print(dizi[0])
