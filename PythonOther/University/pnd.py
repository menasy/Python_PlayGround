import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter('ignore')

indian_rent = pd.read_csv("House_Rent_Dataset.csv")

print("Genel indian rent : \n",indian_rent)
print("columns indian rent : \n",indian_rent.columns)
# stunları turkçeye çevirdik
indian_rent.columns = ['ilan_tarihi','oda_sayısı','kira','boyut','bulunduğu_kat','zemin_tipi','lokasyon_türü',
 'şehir','mobilyalı_mobilyasız','kiracı_tercihi','banyo_sayısı','erişim_yolu']

print("Yeni columns indian rent : \n",indian_rent.columns)

# head() metodu ile ilk satırları çağırabiliriz, eğer bir rakam koymazsak ilk beş satır gelir
print("head : \n",indian_rent.head(10))

#tail() metodu ile son satırları çağırabiliriz, eğer bir rakam koymazsak son beş satır gelir
print(indian_rent.tail(10))

# İndekslemeyi kullanarak da satırları çağırabiliriz.
print(indian_rent[5:10])
print("loc : \n",indian_rent.loc[5:10,:])
print("iloc : \n",indian_rent.iloc[5:10,:])

# Dataframe değildir
print("No Dataframe : \n",indian_rent[0:5]['kira'])
#Dataframe dir
print("DataFrame : \n",indian_rent[0:5][['kira']])

# son 4 sıradaki kira ve şehir bilgileri
print("son 4 sıradaki kira ve şehir bilgileri : \n",indian_rent[-5:-1][['kira','şehir']])

# SADECE rentin 10000' eşit olanlarını görmek istiyoruz

print("kira 10000 : \n",indian_rent[indian_rent['kira'] == 10000])

# rentin 10000'eşit olduğu ve bhk'nın 3 eşit olduğu veriyi görmek istiyoruz
print("Kira oda sayısı : \n",indian_rent[(indian_rent['kira'] == 10000) & (indian_rent['oda_sayısı'] == 3)])

# rentin 10000'eşit olduğu ve bhk'nın 3 eşit ve buyuk olduğu veriyi görmek istiyoruz. loc indeksleme ile de yapab
print("Kira oda sayısı : \n",indian_rent.loc[(indian_rent['kira'] == 10000) & (indian_rent['oda_sayısı'] == 3)])

#en yüksek kiraya sahip ev

print("max kira : \n",indian_rent[indian_rent['kira'] == indian_rent['kira'].max()])

#hayrabadda en yüksek kiraya sahip ev

hd = indian_rent[indian_rent['şehir'] == 'Hyderabad']
print("hayrabad: \n",indian_rent[indian_rent['şehir'] =='Hyderabad'][indian_rent[indian_rent['şehir'] == 'Hyderabad']['kira'] == indian_rent[indian_rent['şehir'] == 'Hyderabad']['kira'].max()])
print("kısaltmalı : \n",hd[hd['kira'] == hd['kira'].max()])
print("en  yuksek kira : \n",indian_rent[indian_rent['şehir'] == 'Hyderabad']['kira'].max())

#bu yöntem Hyderabad şehrindeki sadece en ortalama kirayı gösterir
print("ortalma hayrabad : \n",indian_rent[indian_rent['şehir'] == 'Hyderabad'][['kira','oda_sayısı','boyut']].mean())

# grupby() fonksiyonu


print("groupby : \n",indian_rent.groupby('şehir').mean("şehir"))
print("Ortalama son 5: \n", indian_rent[indian_rent['şehir'] == 'Hyderabad']['kira'].tail(5).mean())
print("gruoupby : \n", indian_rent.groupby('şehir').mean("a"))

# deihide banyo ==2  boyut en buyuk
dlh = indian_rent[indian_rent['şehir'] == 'Delhi']
o = dlh[dlh['oda_sayısı'] == 2]

print("eto \n",o[o['boyut'] == o['boyut'].max()])
print("GRP : \n", indian_rent[indian_rent['kira'] <= 4500].groupby(['şehir','banyo_sayısı','oda_sayısı','kira']).max())
#şehirleri mobilyalı mobilyasız
# kira banyo oda

#Mumbai den kirasi en fazla 10000 olsun  erişim_yolu == Contact Owner mobilyalı_mobilyasız == Unfurnished

mm = indian_rent[indian_rent['şehir'] == 'Mumbai'][indian_rent['kira'] <= 10000]
c = mm[mm['erişim_yolu'] == "Contact Owner"]
sex = c[c["mobilyalı_mobilyasız"] == "Unfurnished"]
print(sex)

#şehir == Mumbai oda_sayısı = 3 kira <= 20000 boyut > 600 bayno_sayısı >= 2 kiracı_tercihi = Bachelors

mb = indian_rent[indian_rent['şehir'] == 'Mumbai'][indian_rent['kira'] <= 20000][indian_rent['oda_sayısı'] == 3][indian_rent['boyut'] >= 600][indian_rent['kiracı_tercihi'] == 'Bachelors'][indian_rent["banyo_sayısı"] >= 2 ]
print(mb)
eto = {"isim" : ["memo","eto","frko"],
		"soyisim": ["yılmaz","kose","genc"]}
print("typ:",eto)
