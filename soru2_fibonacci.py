# 1.YOL:

# x=1
# y=2
# topla = 2 
# while True:
#     z = x + y
#     x,y = y,z
#     if z % 2 == 0:
#        topla+=z
#     if z > 4000000 :
#         break
# print(topla)


# 2.YOL:
    
fibonacci = list()
fibonacci.append(1)
fibonacci.append(2)

index = 2 
topla = 0
while True:
  
    if fibonacci[index-2] + fibonacci[index-1] < 4000000:
        fibonacci.append(fibonacci[index-2] + fibonacci[index-1])
        index += 1
    else:
        break

for cift in fibonacci:
    if cift % 2 == 0:
        topla += cift
    
print(topla)