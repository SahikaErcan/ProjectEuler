"""
Bir Pisagor üçlüsü, a < b < c olmak üzere üç doğal sayı kümesidir, bunun için,  a^2 + b^2 = c^2

Örneğin, 3^2 + 4^2 = 9 + 16 = 25 = 5^2 .

a + b + c = 1000 olan tam olarak bir Pisagor üçlüsü vardır . abc çarpımını bulun .
"""

# Toplamları 1000 edeceği için bu sayıların hiç biri 1000 olamaz.Bu nedenle for 1 den 1000 e kadar şeklinde
   
for a in range(1, 1000): 
    for b in range(1, 1000 - a):
        c = 1000 - a - b
        if c*c == a*a + b*b and a + b + c == 1000 and a < b < c:
            print(f"{a}^2 + {b}^2 = {c}^2")
            print(f"{a} x {b} x {c} = ",a*b*c)



# *************************** 2.YOL *******************************************

# done değişkeni burada çarpımı (print) 2 kez yazmasını engelliyor. Peki neden 2 kez yazıyor?
# a^2 + b^2 = c^2 yapısında  3^2 + 4^2 = 5^2 şeklinde olabileceği gibi  4^2 +3^2 = 5^2 şeklinde de aynı sonu verebiliyor.
# bir nevi işlem tekrarı gibi düşünülebilir. İçteki for sayıyı bulduğunda çıkıyor. Ancak dıştaki for a ve b nin yer 
# değiştirilmiş halde bulunmasına devam ediyor. Dıştaki döngüden de aynı  değerleri tekrar bulmadan çıkması için 
# içdeki for dan done = True olduğunda yani istenilen bulunduğunda çıkılıyor. Dıştaki for dada tekrar aynı değeri
# bulmasın diye done = True yu if kaşulu ile sorgulayıp zaten içerde True olan değişken sayesinde brek atılıyor ve 2 
# döngüden de böylece çıkılmış olunuyor.


# done = False

# for a in range(1,1000):
#     for b in range(1,1000-a):
#         c = 1000 - a - b
#         if c**2 == a**2 + b**2:
#             print(f"{a}^2 + {b}^2 = {c}^2")
#             print(f"{a} x {b} x {c} = ",a*b*c)
#             done = True   
#             break
#     if done == True:
#         break

