import pandas as pd
import numpy as np
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter('ignore')

df = pd.read_csv("House_Rent_Dataset.csv")
#sütun bilgilerinin türkçeleştirilmesi
df.columns = [ 'ilan_tarihi','oda_sayısı','kira','boyut','zemin_tipi',
'muhit_tipi','semt','şehir','mobilyalı_mobilyasız','kiracı_tercihi',
'banyo_sayısı','sahibinden_emlakçıdan']

print("Df :\n",df)

number_of_posted_ad_by_cities = df.groupby('şehir').count()[['kira']]
number_of_posted_ad_by_cities.columns = ['toplam_ilan_sayısı']
print(number_of_posted_ad_by_cities)

#				Döngü ile grafik kullanımı
fig,ax = plt.subplots(figsize = (12,8))
ax.bar(number_of_posted_ad_by_cities.index, number_of_posted_ad_by_cities["toplam_ilan_sayısı"])
ax.set_xlabel("Şehir")
ax.set_ylabel("toplam_ilan_sayısı")
ax.set_xticklabels(number_of_posted_ad_by_cities.index, rotation = 30, color ="r")
for i,j in zip (number_of_posted_ad_by_cities.index,number_of_posted_ad_by_cities["toplam_ilan_sayısı"]):
	ax.text(i,(j*0.8),str(j),color ="w")

plt.show()

#delhi ve kolkatada ev boyutlarının dağılımlarının karşılaştırılması

fig,ax = plt.subplots(figsize = (12,8))
ax.hist(df[df["şehir"] == "Delhi"]["boyut"],label = "Delhi",bins = 11)
ax.hist(df[df["şehir"] == "Kolkata"]["boyut"],label="Kolkata", bins = 11)
ax.set_title("delhi/Kolkata histogram")
ax.set_xlabel("Şehirler")
ax.set_ylabel("Boyut")
ax.legend()
plt.show()

# boxplot aykırı değerlerin görsel olarak gösterilmesi konusunda oldukça etkindir,
#delhi ve kolkata kira dağılımları

fig,ax = plt.subplots(figsize = (12,8))
ax.boxplot([df[df['şehir']=='Delhi']['kira'],df[df['şehir']=='Kolkata']['kira']])
ax.set_xlabel("Şehirler")
ax.set_ylabel(["Delhi","Kolkata"])
ax.set_title("Kira Boxplot Grafiği")

plt.show()

#kira ve boyut arasındaki ilişkinin görsel olarak gösterilmesi
fig, ax = plt.subplots(figsize=(12,8))
ax.scatter(df['boyut'], df['kira'])
ax.set_xlabel("boyut")
ax.set_ylabel("Rent (000 ruppi)")
plt.show()


