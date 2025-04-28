# -*- coding: utf-8 -*-

import datetime
from datetime import datetime
from datetime import timedelta
from datetime import datetime
import numpy as np

# ikisi de aynı işlevde
print("şimdiki zaman :",datetime.now())
print("Gün :",datetime.today())

tarih = [datetime(2001,6,23), datetime(2001,1,17)]
print("tanımlanan tarih : ",tarih)
print("Type : ",type(tarih))

dt =datetime(200,2,2) # veri tipi datetime oluyor
print("dt : ",dt)
print("Type : ",type(dt))

# dt değişkenimin içine tek bir tarih attığım için indis belirtmeden yazdırabiliyorum
print("dt year : ",dt.year)
print("dt month : ",dt.month)
print("dt day : ",dt.day)
print("-----------------------------------")
# tarih değişkenimin içine 2 tane tarih değeri girdiğim için çift pointerli dizi oluşur.
# bu yuzden indislerle erişmem lazım tarih[0] dediğimde ilk tarih verime date[1] ile bir sonrakine erişirim
print("tarih year : ",tarih[0].year)
print("tarih month : ",tarih[0].month)
print("tarih day : ",tarih[1].day)
print("-----------------------------------")
# strftime() fonksiyonu tarih verisini istediğimiz formata çevirir flag lerle ama string olur
# tarih = [datetime(2001,6,23), datetime(2001,1,17)]

strdate = tarih[0].strftime("%d-%m-%Y-%B")
print("sitringe cevrilimiş date : ",strdate)
print("strdate type : ",type(strdate))
#strdate.month dediğmde hata alırım çunku strdate artık bir string değer
print("-----------------------------------")
d1 = datetime(2000,2,2)
d2 = datetime(2001,6,23)

dtarihs = [d1,d2] # listeye tarih değeri atama
print("liste tarih : ",dtarihs)
print("En kucuk (0 a en yakın) tarih : ",min(dtarihs))
print("En buyuk (0 a en uzak) tarih : ",max(dtarihs))

fark = d2-d1
print("tarih farkları : ", fark.days)
# tarihe gun eklemek için:
ekle = timedelta(days = 3)
print("Eklenmiş tarih : ",d1+ekle)
print("Şimdiki tarihe ekleme : ",datetime.now() + ekle)
print("-----------------------------------")


strtarih = "12/30/2017 15:19:13"
print("Type : ",type(strtarih))
strtodate = datetime.strptime(strtarih,"%m/%d/%Y %H:%M:%S")
print("Type srtodate : ",type(strtodate))
print("strtodate : ", strtodate) # hem veri tipi date hem de çıktı ıso formatında yani string
print("-----------------------------------\n")
# 								dictionary
dict1={'hisse_senetleri':['AAPL','IBM','GOOGL','KO','FB','PG'],
'kapanış_fiyatları':[160,115,220,65,115,25],
 'sahip_olunan_miktar':[10,15,21,0,5,11],
 'sahip_olunan_hisselerin_değeri':[]}
print(type(dict1))

for i in range(len(dict1['hisse_senetleri'])):
	dict1['sahip_olunan_hisselerin_değeri'].append(dict1['kapanış_fiyatları'][i] * dict1['sahip_olunan_miktar'][i])
print("sahip olunan hisse değeri : ", dict1['sahip_olunan_hisselerin_değeri'])
i = 0

#					sum() toplama fonksiyonu
print("\n--------------------------------------------------\n")
dict1['hissenin_portfoydeki_payı'] = []
hissetoplam = np.sum(dict1['sahip_olunan_hisselerin_değeri'])

for i in range(len(dict1['hisse_senetleri'])):
	dict1['hissenin_portfoydeki_payı'].append((dict1['sahip_olunan_hisselerin_değeri'][i] / hissetoplam)*100)
print("Hisselerin portfoye oranı : ",dict1['hissenin_portfoydeki_payı'])
i = 0
#						round() yuvarlama fonksiyonu
print("\n--------------------------------------------------\n")

# for i in range(len(dict1['hisse_senetleri'])):
# 	dict1['hissenin_portfoydeki_payı'][i] = round(dict1['hissenin_portfoydeki_payı'][i],2)

for i in range(len(dict1['kapanış_fiyatları'])):
	for j in ['kapanış_fiyatları','sahip_olunan_miktar','hissenin_portfoydeki_payı']:
		dict1[j][i] = round((dict1[j][i]),2)

print("Yuvarlanmış dict : ",dict1)
# benim oluşturduğum dongude ben işlemi sadece portfoydaki pay için yaptım fakat
# diğer dongude eğer diğerlerinde de kusuratlı uzun bir sayı varsa onu da yuvarlar
# j m de her seferinde en baştan başlayarak birini tutar ve round() uygulanır

print("\n--------------------------------------------------\n")

#							#zip
# zip bir nevi indislme yapar birleştirir:
# list1 = [1, 2, 3, 4], list2 = ['a', 'b', 'c', 'd'] gibi iki listeyi
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')] bu şekilde birleştirip indeksler

print("i = ",i)
print("j = ", j)
for i,j in zip(dict1['hisse_senetleri'],dict1['hissenin_portfoydeki_payı']):
	if j > 15:
		print('Hisse senedi {} satış listesinde olmalı.'.format(i))
	elif (j < 15) & (j > 5):
		print('Hisse senedi {} elde tutulan listesinde olmalı.'.format(i))
	else:
		print('Hisse senedi {} satış listesinde olmalı.'.format(i))
	