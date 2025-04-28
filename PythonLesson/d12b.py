import pandas as pd
import numpy as np

df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/homes.csv")

df.columns=['satış_fiyatı','liste_fiyatı','salon_büyüklüğü','oda_sayısı','yatak_odası_sayısı',
'banyo_sayısı','evin_yaşı','evin_toplam_büyüklüğü(dönüm)','ödenen_vergi']
print("Columns:\n",df.columns)

print("\ndf:\n",df)

yortv= df[['yatak_odası_sayısı','ödenen_vergi']].groupby('yatak_odası_sayısı').mean().reset_index()
yortv.columns=['yatak_odası_sayısı','ortalama_vergi']
print("\nyatak_odası_sayısına_ortalama_vergi:\n",yortv)

#Inner Join
# yatak odasına göre ortalama verginin merge ile eklenmesi
df_01 = pd.merge(df,yortv, on="yatak_odası_sayısı")
print("Merg Join:\n",df_01)

df1 = pd.DataFrame({
	'rating': [90, 85, 82, 88, 94, 90, 76, 75],
	'points': [25, 20, 14, 16, 27, 20, 12, 15],
	'team':['A','A','B','B','C','C','D','D']},
	index=list('abcdefgh'))

df2 = pd.DataFrame(
	{'assists': [5, 7, 7, 8, 5, 7],
	'rebounds': [11, 8, 10, 6, 6, 9],
	'team':['A','F','B','F','C','F']},
	index=list('acdgmn'))

print("\ndf1:\n",df1)
print("\ndf2:\n",df2)

print("\nJoin left:\n",df1.join(df2,lsuffix='df1',rsuffix='df2'))

print("\nJoin left İnner:\n",df1.join(df2,lsuffix='df1',rsuffix='df2',how='inner'))

print("\nJoin right İnner:\n",df1.join(df2,lsuffix='df1',rsuffix='df2',how='right'))
#yine aynı yere 2. alana yazdı ve ilk kısma da ortakları yazdı ve df2 de olup df1 de olmayanlara nan attı

print("\nMerge on inner:\n",pd.merge(df1,df2,on = "team"))

print("\nMerge on left:\n",pd.merge(df1,df2,how="left",on="team"))

print("\nMerge on right:\n",pd.merge(df1,df2,how="right",on="team"))

print("\nMerge on outer:\n",pd.merge(df1,df2,how="outer",on="team"))


print("-	-	-	-	PİVOT TABLE	-	-	-")

print("\nPivot Table Sum:\n",pd.pivot_table(df1,values='points',columns='team',aggfunc='sum'))
print("\nPivot Table Mean:\n",pd.pivot_table(df2,values='rebounds',columns='assists',aggfunc='mean'))
# values değerine aggfunc ile tanımlanacak fonksiyonun işleyeceği değerler girilir
#columns kısmına da bu verilerin diğer bir stundaki verileri verilir
#orneğin 2.table de asist değerleri aynı olan yani mesela 5 e karşılık gelen rebaunds değerlerinin ortalamsını verir bu kod
# ya da 1.table için team a olan değerlerin toplamasını alıyor.
