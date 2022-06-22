kareler_toplamı = 0
for i in range(1,101):
    kareler_toplamı += i**2    
    toplamin_karesi = (i* (i+1)/2)**2
print(toplamin_karesi - kareler_toplamı)

