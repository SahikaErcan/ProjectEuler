numbers = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

rows = numbers.split("\n") #parçalayıp her satırı listenin bir elemanı haline getirdik.

liste = list()

for i in range(0,20): # listede ki her bir satır elemanını da boşluğa göre parçalıyoruz.
    elements = rows[i].split(" ") # Böylece stringde ki her bir elemana erişiyoruz.
    liste.append(elements)

for  i in range(0,20): # satır
    for j in range(0,20): # sütun
        if liste[i][j]=="00": # i ve j . index 00 karakterli ise 0 karakterine dönüştür.
            liste[i][j]="0"
        elif len(liste[i][j])!=1:
            if liste[i][j].startswith("0"): # i ve j. index in 1. karakteri 0 ise 0 karakterine göre parçala.
                liste[i][j]=liste[i][j].strip("0") # 0 ı yok et.

def sol_sag():  
    en_buyuk = 0
    for i in range(0,20):  # satır
        for j in range(0,17): # sütun # döngü içinde satır için 4 karakter (sütun) ilerlettiğimiz için 4 karakter eksik döngü açıyoruz.
            carp = 1
            for k in range(0,4):  # 4 sayıyı çarpacağımız için bu döngüyü açıyoruz.
                carp *= int(liste[i][j+k])
                if carp > en_buyuk:
                    en_buyuk = carp
    return en_buyuk

def yukari_asagi():
    en_buyuk = 0
    for i in range(0,17): # döngü içinde sütun 4 karakter (satır) ilerlettiğimiz için 4 karakter eksik döngü açıyoruz.
        for j in range(0,20):
            carp = 1
            for k in range(0,4):
                carp *= int(liste[i+k][j])
                if carp > en_buyuk:
                    en_buyuk = carp
    return en_buyuk

def sag_capraz():
    en_buyuk = 0
    for i in range(0,17):
        for j in range(0,17):
            carp = 1
            for k in range(0,4):
                carp *= int(liste[i+k][j+k])
                if carp > en_buyuk:
                    en_buyuk = carp
    return en_buyuk

def sol_capraz():
    en_buyuk = 0
    for i in range(0,17):
        for j in range(0,17):
            carp = 1
            for k in range(0,4):
                carp *= int(liste[i+k][19-j-k])
                if carp > en_buyuk:
                    en_buyuk = carp
    return en_buyuk

results = []

results.append(yukari_asagi())
results.append(sol_sag())
results.append(sol_capraz())
results.append(sag_capraz())

print(max(results))

# ****************** 2.YOL ****************************************************


# import numpy as np

# grid_str = (
#     """
# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""
# )[1:]

# grid = np.array([[int(n) for n in row.split(" ")] for row in grid_str.split("\n")])


# def max_prod_horiz(grid):
#     result = 0
#     for row in grid:
#         for j in range(len(grid[0]) - 4 + 1):
#             ans = np.product(row[j : j + 4])
#             if ans > result:
#                 result = ans

#     return result


# def max_prod_diag1(grid):
#     result = 0
#     for i in range(1 - len(grid), len(grid)):
#         diag = np.diag(grid, k=i)
#         if len(diag) < 4:
#             continue
#         for j in range(len(diag) - 4 + 1):
#             ans = np.product(diag[j : j + 4])
#             if ans > result:
#                 result = ans

#     return result


# def max_prod_diag2(grid):
#     grid = np.flip(grid, (0,))
#     return max_prod_diag1(grid)


# def max_product(grid):
#     return max([max_prod_horiz(grid), max_prod_diag1(grid), max_prod_diag2(grid)])


# print(max_product(grid))


# ****************** 3.YOL ****************************************************



# liste=[ [8, 2, 22, 97, 38, 15, 00, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8] ,
#         [9 ,49 ,99, 40, 17, 81, 18 ,57 ,60 ,87 ,17 ,40 ,98 ,43 ,69 ,48 ,4 ,56 ,62 ,00],
#         [81, 49, 31, 73, 55 ,79 ,14, 29, 93, 71 ,40 ,67 ,53 ,88 ,30, 3, 49, 13, 36, 65],
#         [52 ,70 ,95 ,23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
#         [22, 31, 16, 71, 51, 67, 63 ,89 ,41, 92, 36, 54 ,22 ,40 ,40 ,28 ,66 ,33 ,13, 80],
#         [24 ,47 ,32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17 ,12, 50],
#         [32, 98 ,81 ,28, 64, 23, 67, 10 ,26 ,38, 40 ,67, 59 ,54 ,70,66 ,18 ,38 ,64 ,70],
#         [67 ,26 ,20 ,68, 2 ,62 ,12, 20, 95, 63, 94, 39 ,63, 8, 40, 91, 66, 49, 94, 21],
#         [24, 55, 58, 5, 66 ,73 ,9 ,26 ,97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
#         [21, 36, 23, 9, 75, 00, 76, 44, 20 ,45 ,35 ,14 ,00 ,61 ,33 ,97 ,34 ,31, 33, 95],
#         [78, 17 ,53 ,28, 22, 75 ,31, 67, 15, 94 ,3, 80, 4, 62 ,16 ,14 ,9, 53, 56 ,92],
#         [16 ,39 ,5, 42, 96, 35, 31, 47 ,55 ,58 ,88 ,24, 00 ,17 ,54, 24, 36, 29, 85, 57],
#         [86 ,56 ,00 ,48 ,35 ,71, 89 ,7 ,5 ,44, 44 ,37 ,44 ,60 ,21, 58, 51 ,54 ,17 ,58],
#         [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4 ,89 ,55 ,40],
#         [4 ,52 ,8 ,83 ,97 ,35 ,99 ,16 ,7 ,97 ,57 ,32 ,16 ,26 ,26 ,79 ,33 ,27 ,98 ,66],
#         [88, 36, 68, 87 ,57 ,62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
#         [4 ,42 ,16 ,73 ,38 ,25, 39 ,11 ,24 ,94 ,72 ,18, 8 ,46 ,29 ,32 ,40 ,62 ,76, 36],
#         [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59 ,85, 74, 4, 36, 16],
#         [20 ,73 ,35 ,29 ,78 ,31 ,90 ,1 ,74 ,31 ,49 ,71 ,48 ,86 ,81 ,16 ,23 ,57 ,5 ,54],
#         [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]
# i=0
# j=0
# a=liste[0][0]*liste[0][1]*liste[0][2]*liste[0][3]
# b=0
# while i<17:
#         while j<17:
#                 b=liste[i][j]*liste[i][j+1]*liste[i][j+2]*liste[i][j+3]
#                 if b>=a:
#                         a=b
#                         j=j+1
#                         print(a,i,j)

#                 elif b<a:
#                         j=j+1
#         i=i+1
#         j=0
#         continue
# #soldan sağa en yükse 48477312 8 11

# i=0
# j=0
# #a=liste[0][0]*liste[1][0]*liste[2][0]*liste[3][0]
# b=0
# while j<17:
#         while i<17:
#                 b=liste[i][j]*liste[i+1][j]*liste[i+2][j]*liste[i+3][j]
#                 if b>=a:
#                         a=b
#                         i=i+1
#                         print(a,i,j)

#                 elif b<a:
#                         i=i+1
#         j=j+1
#         i=0
#         continue
# #yukarıdan aşağı en yüksek 51267216 7 15

# i=0
# j=0
# #a=liste[0][0]*liste[1][1]*liste[2][2]*liste[3][3]
# b=0
# while i>=0 and i<17:
#       while j>=0 and j<17:
#             b=liste[i][j]*liste[i+1][j+1]*liste[i+2][j+2]*liste[i+3][j+3]
#             if b>=a:
#                   print(b,i,j)
#                   a=b
#                   j=j+1
#             else:
#                   j=j+1
#       i=i+1
#       j=0
# #hedef sağ alt 16 9 40304286

# i=0
# j=19
# #a=liste[0][19]*liste[1][18]*liste[2][17]*liste[3][16]
# b=0
# while i>=0 and i<17:
#     while j<=19 and j>2:
#         b=liste[i][j]*liste[i+1][j-1]*liste[i+2][j-2]*liste[i+3][j-3]
#         if b>=a:
#             print(b,i,j)
#             a=b
#             j=j-1
#         else:
#             j=j-1
#     i=i+1
#     j=19
