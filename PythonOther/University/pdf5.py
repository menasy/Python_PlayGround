import pandas as pd
import numpy as np

# dataframe oluşturma 1

dc = {'isim': ['eto','memo','furkan'],
		'soyisim': ['kose','yılmaz','genc'],
		'okulno': [31,73,47]}
df = pd.DataFrame(dc)

print(df)

df1 = pd.DataFrame(index = ['eto', 'memo','furki'],columns = ['boy','kilo'])
print("df1 : \n",df1)
df1["memlket"] = ["suriye","şırnak","izmit"]
print("new df1 : \n",df1)
print(df1.columns)
print(df1.index)

# boş dataframe

df2 = pd.DataFrame()
print("Boş dataframe : ",df2)

# list kullanarak dataframe
liste = [1,2,3,5]

df3 = pd.DataFrame(liste)
print("liste df : ", df3)

# dataframe yeni stun eklemek
# yeni stun eklerken data uzunluğu aynı olmalıdır yanı satır sayısını geçmemeli
print("df : \n",df)
df ["memleket"] = ['suriye','şırnak','izmit']
df ["yas"] = [22,23,21]
print("new df : \n",df)

print("\n--------------------------------------------------\n")

#Dataframe datatipleri
print("dataframe boyutu : \n",df.shape)
print("info : \n")
df.info()
print("new df : \n",df)
print("\nBoyut : ",df.shape)
print("\nDescribe : \n",df.describe()) # integar veriler uzerinde bilgi sağlar
print("\n--------------------------------------------------\n")

# dataframe silmek
print("df3 : \n",df3)
del	df3
#print("after del df3 : \n",df3) silindiği için hata veriyor

#sütun silmek drop(axis=1)

print("df1 : \n",df1)
df1.drop(['kilo'],axis = 1,inplace = True) # axis = 1 stunlarda işlem yapacağımızı ifade eder
print("After df1 : \n",df1) 				# axis = 0 satırlarda işlem yapacağını ifade eder
# inplace = true dediğimizde de işlemi kaydediyoruz eğer onu yazmazsak çıktı değişmez
# Sıra silinmesi axis=0
df1.drop(['furki'],axis=0, inplace=True)
print("After 2 df1 : \n",df1)

# index ile silme
print("indis : \n",df1.index)
df1.drop(['eto'],axis=0,inplace = True)
print("After 3 df1 : \n",df1)

print("\n--------------------------------------------------\n")

df7 = pd.DataFrame([['Ali',18,'istanbul'],['Veli',25,'istanbul'],['Ayşe',20,'izmir'],['Fatma',23,'ankara']],
 columns=['isimler','yaşlar','doğum_yerleri'])
# bu bir seridir
print(df7['isimler'])
# bu ise DataFrame dir
print(df7[['isimler']])
print("\n loc : \n")
print(df7.loc[:,['isimler']])
print("\n İloc : \n")
print(df7.iloc[:,[2]]) # hangi indisi yazacaksan o değeri gireceksin
# değerler koşeli parantez içinde ise DataFrame dir değilse seridir

#						Filtreleme
print("\n-------------------------Filtreleme-------------------------\n")

# istanbul doğımlu kişiler

print("İstanbul doğumlu kişiler : \n",df7[df7['doğum_yerleri'] == 'istanbul'])

# yaşları 20 veya 20 den küçük kişiler
print("yaş : \n",df7[df7['yaşlar'] <= 20])

#en yayşlı kişi
print("en yayşlı kişi : \n",df7[df7['yaşlar'] == df7['yaşlar'].max()])
#en yayşlı kişinin ismi (list olarak)
print("en yayşlı kişinin ismi : \n",df7[df7['yaşlar'] == df7['yaşlar'].max()]['isimler'])
#en yayşlı kişinin ismi
print("en yayşlı kişinin ismi values : \n",df7[df7['yaşlar'] == df7['yaşlar'].max()]['isimler'].values[0])
# burdaki values değeri tek eleman olduğu için 0 değerini girdik birden çok değer olsaydı indisini girerdik

# 20 ve 20 üstü yaşında olup ve istanbullu olmayanlar
print("filtre : \n",df7[(df7['yaşlar'] >= 20) & (df7['doğum_yerleri'] != 'istanbul')])

#25 ve altı yaşda olup ismi A harfi ile başlayanlar
print("isim a : \n",df7[(df7['yaşlar'] <= 25) & (df7['isimler'].str.startswith('A'))])



print("kolon ortalaması : \n",df['okulno'].mean())
