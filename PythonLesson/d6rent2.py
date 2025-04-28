import pandas as pd
import numpy as np
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter('ignore')

df = pd.read_csv("House_Rent_Dataset.csv")
print("Df :\n",df)
print(df.describe())
number_of_posted_ad_by_cities = df.groupby('City').count()[['Rent']]
number_of_posted_ad_by_cities.columns = ['number_of_posted_ad']
print(number_of_posted_ad_by_cities)

#				Çubuk Grafik

# fig, ax = plt.subplots(figsize=(12,8))
# ax.bar(number_of_posted_ad_by_cities.index, number_of_posted_ad_by_cities["number_of_posted_ad"])
# ax.set_xlabel('Cities')
# ax.set_ylabel("Number of Rental house Ad")
# ax.set_xticklabels(number_of_posted_ad_by_cities.index, rotation=30,color='r')
# # yukarıdaki satırda x ekseni için ozelleştirme yapılıyor.
# # rotation değeri altta yazan yazıları hangi açıyla yazacağını belitir
# plt.show()

# 'Rent' sütunundaki tarih formatındaki verileri sayısal değerlere dönüştür
df['Rent'] = pd.to_numeric(df['Rent'])

# 'Rent' sütunundaki tarih formatındaki verileri sayısal değerlere dönüştür
df['Rent'] = pd.to_numeric(df['Rent'], errors='coerce')
# 'City' gruplarına göre ortalama kiralama ücretini hesapla
average_rent_by_cities = df.groupby('City')['Rent'].mean().reset_index()
average_rent_by_cities.columns = ['City', 'average_rent']

print("Avarage_rent_cities:\n",average_rent_by_cities)

fig, ax = plt.subplots(figsize=(12,8))
ax.bar(number_of_posted_ad_by_cities.index, number_of_posted_ad_by_cities["number_of_posted_ad"],label = "number_of_posted_ad_by_cities")
ax.bar(average_rent_by_cities.index, average_rent_by_cities["average_rent"],bottom=number_of_posted_ad_by_cities["number_of_posted_ad"],label='average_rent')
ax.set_xlabel('Cities')
ax.set_ylabel("Number of Rental house Ad & Average Rent (000 ruppi)")
ax.set_xticklabels(number_of_posted_ad_by_cities.index, rotation=90,color='r')
ax.legend()
plt.show()

#				Histogram ve dağılım Grafiği
fig,ax= plt.subplots(figsize = (12,8))
# label ile isim atadık ve bins = 11 ile kaç parçaya dağılcağını soyledik
ax.hist(df[df["City"] == "Delhi"]["Size"],label ="memo",bins = 11,)
ax.hist(df[df["City"] == "Kolkata"]["Size"],label = "eto",bins = 11)
ax.set_xlabel("Şehir")
ax.set_ylabel("Size")
ax.legend() # lejantı getiriyor kucuk kutu
plt.show()

fig, ax = plt.subplots(figsize=(12,8))
ax.bar('Delhi',df[df['City']=='Delhi'][['Rent']].mean(),yerr =df[df['City']=='Delhi'][['Rent']].std() )
ax.bar('Kolkata',df[df['City']=='Kolkata'][['Rent']].mean(),yerr =df[df['City']=='Kolkata'][['Rent']].std())
ax.set_xlabel("Cities")
ax.set_ylabel("Rent (000 ruppi)")
plt.show()
