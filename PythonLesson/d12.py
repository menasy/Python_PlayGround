import pandas as pd
import numpy as np

print("-	-	-	-	Merge()	-	-	-	-")
#merge() işlevini kullandığımızda,fonsiyon parametrelerini tanımlamamız gerekmektedir:
#left & right: Hangi dataframe left, hangisi right olarak tanımlanacak.
#how: Birleştirme nasıl yapılacak.inner join, outer join, left join ve right join
#Belirtilmediği takdirde bu yöntem varsayılan olarak inner olacaktır.
#on : Hangi sütuna göre birleşme yapılacak, eğer belirtilmemişse otamatik olarak index kullanılır.
#left_on & right_on: Eğer sütun isimleri aynı değilse , birleşyitmeyi sağlıyacak sütunlar belirtilmelidir
#suffixes: Eğer aynı isimde sütunlar varsa sütunları tekrar isimlendirebiliriz. Eğer atlanırsa,otamatik_y olarak atanır.
#sort: Birleşmeye konu olan sütuna göre DataFrame sıralar.
df_0 = pd.DataFrame(
	[['Ali','Fizik',50],
	['Veli','Fizik',45],
	['Ayşe','Matematik',50]],
	columns =['isim','aldığı_ders','final_sınav_notu'])
print("Df_o:\n",df_0)

df_1 = pd.DataFrame(
	[['Ali',60],
	['Fatma',65],
	['Ayşe',70]],
	columns=['isim','vize_sınav_notu'])
print("\nDf_1:\n",df_1)

# isimlere göre birleştiriyorsak ve how parametresini tanımlamıyorsak
#otamatik olarak inner yöntemini uygular
print("\nMerge Defult:\n",pd.merge(df_0,df_1,on = 'isim'))
# how belirtmediğimiz için default olarak innear yani kesşimleri aldı.

print("\nMerge outer:\n",pd.merge(df_0,df_1,on ='isim',how = 'outer'))
# outer ile kume birleştirme işlemi yaptık olan değerleri yazdı olmayanlara nan attı

print("\nMerge left:\n", pd.merge(df_0,df_1,on ='isim',how= 'left'))
# leftteki yani df_0 daki isimleri aldı ve diğer df de olan stunları da alarak birleştirdi
# Başta aldığ ders ve fianal notu varlen birleştirme sonunda vize_sınav notu da eklenmiş oldu

print("\nMerge right:\n", pd.merge(df_0,df_1,on ='isim',how= 'right'))
# righttaki yani df_1 deki isimleri aldı ve iki df nin kolonlarını birleştirdi

print("\nMerge Default on:\n", pd.merge(df_0,df_1, how= 'outer'))


print("-	-	-	-	Merge()/df2	-	-	-	-")

df_01 = pd.DataFrame(
	[['Ali','Fizik',50],
	['Veli','Fizik',45],
	['Ayşe','Matematik',50]],
	columns=['isim','aldığı_ders','final_sınav_notu'])

df_02 = pd.DataFrame(
	[['Ali','Fizik',50],
	['Veli','Fizik',45],
	['Ayşe','Kimya',50]],
	columns=['isimler','dersler','final_sınav_notu'])

print("\ndf_01:\n",df_01)
print("\ndf_02:\n",df_02)

print("\nMerge suflix:\n",pd.merge(df_01,df_02,how='inner',left_on ='isim',right_on='isimler',suffixes=[' df_01',' df_02']))
# stun isimleri ortak olmadığı için direkt on kullanamıyoruz bu yuzden left-on ve right_on kullanıyoruz.
#suffixles ise ortak olan stun ismi varsa birleştirme de karışmasın diye farklı isimle belirtir
#eğer suffixles yazılmazsa default olarak ilk df deki stuna x ikinci ye y atanır.

print("\nMerge suflix/outter:\n",pd.merge(df_01,df_02,left_on ='aldığı_ders',right_on='dersler',how='outer',suffixes=[' df_01',' df_02']))
#outer yaptığımızda çakışan veri olmayam yerlerde nan attı
#ayşe için df_01 değerlerini yazdı ve df_02 değerlerine nan attı
#ayşe için df_01 deki değerlere nan attı ve df_02 deki değerleri yazdı
#isimleri ikişer defa yazmasının sebebi bir tanesi df_01 için oburu df_02 için

print("\nMerge suflix/çoklu stun:\n",pd.merge(df_01,df_02,left_on=['isim','aldığı_ders']
	,right_on=['isimler','dersler'],how="inner"))


print("-	-	-	-	-	Join	-	-	-	-	")
#join(), iki DataFrame'i indekste birleştirmek için kullanılır ancak sütunlarda kullanılmaz;
# merge() ise öncelikle sütunları üzerinden birleştirmek için kullanılır
#merch birleştirdiği verileri alt alta ve karışık veriyor
#join de ise left df yi solda right df yi sağda verir

df_a = pd.DataFrame(
	[['Ali','Fizik',50],
	['Veli','Fizik',45],
	['Ayşe','Matematik',50]],
	columns=['isim','aldığı_ders','final_sınav_notu'])

df_b = pd.DataFrame(
	[['Ali','Fizik',50],
	['Veli','Fizik',45],
	['Ayşe','Matematik',50],
	['Fatma','Kimya',90]],
	columns=['isim','ders','vize_sınav_notu'])

print("\ndf_a:\n",df_a)
print("\ndf_b:\n",df_b)

print("\nJoin lsuffix\n",df_a.join(df_b,lsuffix=' > df_a|'))
#merhc te stunlar aynıyken de birleştirme yaptığımızda suffix yazmasak bile
#aynı olan stunlara default olarak x ve ye değerleri atıyordu.Fakat
#Join de eğer stun isimleri aynıysa suffix olmadan kod çalışmaz.
#how belirtilmezse default olarak inner işlenir

print("\nJoin outter:\n",df_a.join(df_b, lsuffix= " > df_a",how="outer"))


print("\nJoin left:\n",df_a.join(df_b, lsuffix= " > df_a",how="left"))

print("\nJoin right:\n",df_a.join(df_b, lsuffix= " > df_a",how="right"))
#right veya left yaptığımızda kendisini yazdırır. ve eğer diğer df de ondaki veri yoksa nan atar

print("-	-	-	-	-	Concat	-	-	-	-	")


df_c = pd.DataFrame(
	[['Ali','Fizik',50],
	['Veli','Fizik',45],
	['Ayşe','Matematik',50]],
	columns=['isim','aldığı_ders','final_sınav_notu'])

df_d = pd.DataFrame(
	[['Fatma','Fizik',50],
	['Zeynep','Tarih',45],
	['Necip','Kimya',50]],
	columns=['isim','aldığı_ders','final_sınav_notu'])

print("\ndf_c:\n",df_c)
print("\ndf_d:\n",df_d)

print("\nConcat Aynı Stunlar:\n",pd.concat([df_c,df_d],axis=0))
# Concatta eğer stun isimleri ortaksa alt alta tum verileri yazar fakat

# eğer stun isimleri farklıı ise de verileri yazar ve farklı olan stunları
#yana yazar ve olmayan değerler için nan değeri atar
print("\nConcat Farklı Stunlar:\n",pd.concat([df_a,df_b],axis=0))

#axis değeri 1 olunca da yatay yazar ve olmayan değerler için nan atar
print("\nConcat Aynı Stunlar Yatay:\n",pd.concat([df_c,df_d],axis=1))
print("\nConcat Farklı Stunlar Yatay:\n",pd.concat([df_a,df_b],axis=1))

print("join default:\n",df1.join(df2,lsuffix='df1',rsuffix='df2'))
