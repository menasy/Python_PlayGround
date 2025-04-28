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

start = '2010-12-15'
end = '2020-12-15'
tickers = ['GOOGL','AAPL','KO','IBM']
interval = "1d"

portfolio_stocks = yf.download(tickers,start, end, interval)
portfolio_stocks = portfolio_stocks['Adj Close']
print("portfolio_stocks : \n",portfolio_stocks)

#dogu ile grafik oluşturma
fig,ax = plt.subplots(figsize = (12,8))
for i in portfolio_stocks.columns:
	ax.plot(portfolio_stocks[i])
	ax.set_xlabel("TİME")
	ax.set_ylabel("PRİCE")
plt.show()

# figur oluşturmayı dongu içinde yaptığım için her bir hisse için
#ayrı bir figur oluşturup grafiği ayrı ayrı veriyor
# for i in portfolio_stocks.columns:
# 	fig,ax = plt.subplots(figsize = (12,8))
# 	ax.plot(portfolio_stocks[i])
# 	ax.set_xlabel("TİME")
# 	ax.set_ylabel("PRİCE")
# plt.show()

# plt.figure(figsize = (8,4))
# heatmap = sns.heatmap(df[['oda_sayısı','kira','boyut']].corr(),vmin = -1, vmax=1, annot=True, cmap='BrBG')
# heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':18}, pad=12);
# plt.show()



# plt.figure(figsize = (20, 8))
# counts = df["şehir"].value_counts()
# explode = (0, 0, 0, 0, 0, 0.1)
# colors = ['#FF1E00', '#A66CFF', '#EAE509', '#D61C4E', '#3CCF4E', '#3AB4F2']
# counts.plot(kind = 'pie', colors = colors, explode = explode,
# autopct = '%1.1f%%')
# plt.axis('equal')
# plt.legend(labels = counts.index, loc = "best")
# plt.show()
# Aykırı değerleri ve dağılımları gösteren bazı grafik türleri şunlardır:

# Boxplot (Kutu Grafiği):
# Boxplot, veri setinin merkezi eğilimini, çeyreklikleri, aykırı değerleri ve genel dağılımı gösterir.
# Boxplot, veri setindeki aykırı değerleri belirlemek ve
# temel istatistiksel özellikleri anlamak için sıkça kullanılır.

# Scatter Plot (Saçılma Grafiği):
# Scatter plot, iki değişken arasındaki ilişkiyi gösterir
# Aykırı değerler genellikle diğer noktalardan belirgin bir şekilde farklıdır,
# bu nedenle scatter plot kullanılarak aykırı değerler tespit edilebilir.

# Histogram:
# Histogram, veri setinin frekans dağılımını gösterir
# Bu dağılım içindeki aykırı değerleri görsel olarak belirlemek ve anlamak için kullanılabilir.

# Kernel Density Plot:
# Kernel density plot, veri setinin olasılık yoğunluğunu gösterir.
#  Bu grafik türü, histogramın pürüzsüz bir versiyonuolarak düşünülebilir.
# Aykırı değerleri daha yumuşak bir şekilde gösterir.

# QQ Plot (Quantile-Quantile Plot):
# QQ plot, bir teorik dağılım ile gözlemlenen veri setinin dağılımını karşılaştırır.
# Aykırı değerler, teorik dağılımdan sapmalar olarak görülebilir.
