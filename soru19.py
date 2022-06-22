# 1 Ocak(1.ay) 1901 den 31 Aralık(12.ay) 2000 e kadar kaç sefer bir ayın ilk günü pazar olur?

from datetime import datetime

pazar_sayisi = 0

for yil in range(1901,2001): 
    for ay in range(1,13):
        # gün parametresine 1 dedik çünkü ayın 1. günü
        if datetime(yil, ay, 1).weekday() == 6:
        # weekday 0 dan 6 ya kadar değer üretir. Bu nedenle haftanın 6.günü pazara denk geliyor.
            pazar_sayisi += 1
            
print(pazar_sayisi)

""" Sırayla dıştaki döngü 1901 iken içteki döngüde olan 12 ayı tek tek dolaşıp;
 1.ayın 1 i pazar mı?
 2.ayın 1 i pazar mı?
 3.ayın 1 i pazar mı?
 ''
 ''
 ''
 12.ayın 1 i pazar mı?
 
   Yıl 1902
   Yıl 1903
   '
   '
   '
   Yıl 2000 ının sonuna kadar

 şeklinde devam eder.
 
 """
 
# 2.YOL:  PANDAS ÇÖZÜMÜ 

import pandas as pd

# pandas.period_range() , varsayılan frekans olarak gün (takvim) ile sabit
# bir PeriyodIndex frekansı döndürmek için kullanılır.
"""
Sabit bir sıklıkta PeriodIndex döndürün.Gün (takvim) varsayılan sıklıktır.
     parametreler
start : str veya nokta benzeri, varsayılan Yok
Dönem oluşturma için sol sınır.

end :  str veya nokta benzeri, varsayılan Yok
Dönemler oluşturmak için doğru sınır.

freq : str veya DateOffset, isteğe bağlı
Frekans takma adı. Varsayılan olarak frekansı alınır başlangıcında veya
sonunda bu dönem nesneleri ise. Aksi takdirde, varsayılan "D"günlük sıklık içindir.

name : str, varsayılan Yok
Ortaya çıkan PeriodIndex'in adı.
"""
days = pd.DataFrame(pd.period_range(start='1901-01-01', end='2000-12-31', freq='D'), dtype = str)
days['Day of Month'] = days[0].apply(lambda x:x.split('-')[-1]) # - ye göre parçala ve günü al
#Yalnızca ayın ilklerini seçmek
days = days[days['Day of Month'] == '01']
days['day name'] = pd.Series(days[0], dtype = 'datetime64').dt.day_name()
print(len(days[days['day name'] == 'Sunday']))