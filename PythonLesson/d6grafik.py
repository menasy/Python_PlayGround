import pandas as pd
import numpy as np
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

start = '2010-12-15'
end = '2020-12-15'
tickers = ['GOOGL','AAPL','KO','IBM']
interval = "1d"

portfolio_stocks = yf.download(tickers,start, end, interval)

portfolio_stocks = portfolio_stocks['Adj Close']

print("portfolio_stocks : \n",portfolio_stocks)

print("-	-	-	-	GRAFİK ÇİZİMİ	-	-	-	-")
# # Tek bir hissenin grafiğinin çizilmesi
# plt.figure(num = 1, figsize = (12,8))
# #figurleri belirtiyoruz burda ve num değeri  de oluşturduğumuz figure atanan değeri ifade ediyor.
# #Yani grafik oluştuğunda oluşan dosyanın ismi figure 1
# plt.plot(portfolio_stocks.AAPL)
# # plt.plot(portfolio_stocks.AAPL,'rx') rx komutunu ekleyince x ten oluşan grafik oluşturuyor
# # Burda grafiği oluşturduk plt.plot ile çixgi grafk oluşturmamıza yarıyor
# plt.title('Zaman Serisi Grafiği')
# plt.xlabel('Günler')
# plt.ylabel('Fiyat')
# plt.show()

# # Grafiklerin düzenlenmesi
# plt.figure(num = 2, figsize= (12,8), facecolor= 'orange')
# #facecolor arka plan rengi
# plt.plot(portfolio_stocks.loc['2014','AAPL'], '^g')
# # loc ile AAPL hissesinin 2014 yılı verilerini aldık. ve'^'uçgen şeklindeki ve g yeşil renkte grafikle gosterdik
# plt.title('2014 Yılı APPLE Hisse Fiyatları',color='C0')
# plt.xlabel('Zaman',color='C4')
# plt.ylabel('Fiyat',color='C2')
# plt.show()

#								Subplot
# yukarıdaki grafiklerde sadece bir figur oluşturulurken  burda ise
#subplots ile hem figur hem de alt çizimleri oluşturur
#figur oluşturulan ana nesne yani grafikdir. alt çizim ise tasarımlar ve girilen verilerdir
# *****fig,ax = plt.subplots(figsize = (12,8))
# #fig e figur nesnesini ax ise alt çizimleri barındırır
# ax.plot(portfolio_stocks.loc['2020':,'AAPL'],marker = "o",linestyle = "--",color="r")
# ax.set_xlabel("Zaman")
# ax.set_ylabel("Fiyat")
# ax.set_title("APPLE 220 Yılı Hisse Fiyatı")
# plt.show()

# # Eğer iki farklı datayı aynı çizim kodu ile çizersek ikisi için ayrı ayrı karakter belirleyemeyiz

# fig,ax = plt.subplots(figsize=(12,8))
# ax.plot(portfolio_stocks.loc['2019':,['AAPL','GOOGL']],marker = "^",linestyle = "--")
# ax.set_xlabel("Time")
# ax.set_ylabel("Price")
# ax.set_title("İkili Grafik")
# plt.show()

# # Eğer iki farklı datayı ayrı ayrı çizim kodu ile çizersek
# # ikisi için ayrı ayrı karakter belirleyebiliriz

# fig,ax = plt.subplots(figsize = (12,8))
# ax.plot(portfolio_stocks.loc['2019':,'GOOGL'],marker = "*", linestyle="-.")
# ax.plot(portfolio_stocks.loc['2020':,'AAPL'],marker = "s",linestyle = ":")
# ax.set_xlabel("Time")
# ax.set_ylabel("Price")
# ax.set_title("AAPL & GOOGL Menasy tasarımı")
# plt.show()

# # 					Çoklu grafik çizimi(2 satır ve 2 sütun)
# fig,ax = plt.subplots(2,3,figsize = (12,8))
# #2,2 dediğimde oluşan figurde 2 satır ve 2 stun olacak şekilde 4 tane grafik oluşturuyor.
# #ax da tıpkı dizi mantığında olduğu gibi indis değerleri girerek bunlara erişiyoruz
# #ax[0,0] ilk grafiği yani 0. satır 0. stunu ax[0,1] = 0. satır 1.stun
# # grafikleri aynı yukarıda yaptığımızgibi marker color falan ile ozelleştirebiliriz
# ax[0,0].plot(portfolio_stocks.loc['2020':,'AAPL'])
# ax[0,1].plot(portfolio_stocks.loc['2019':,'GOOGL'])
# ax[1,0].plot(portfolio_stocks.loc['2020':,'KO'])
# ax[1,1].plot(portfolio_stocks.loc['2019':,'IBM'])
# ax[0,0].set_title("AAPL HİSSESİ")
# ax[0,1].set_title("GOOGL Hissesi")
# ax[1,0].set_title("KO Hissesi")
# ax[1,1].set_title("IBM Hissesi")
# ax[0,0].set_xlabel("Time")
# ax[0,1].set_ylabel("Price")
# ax[1,0].set_xlabel("Zaman")
# ax[1,1].set_ylabel("Fiyat")

# plt.show()

# # çoklu grafik çizimi(2 satır ve 2 sütun) grafik aralarına boşluk ekleyerek
# fig = plt.figure(figsize=(12, 8), constrained_layout=True)
# # Burda fig i yapılandırıyoruz 12,8 lik ve aralarında otomatik boşluk olsun diyoruz
# spec = fig.add_gridspec(2, 2, hspace=0.025, wspace=0)
# #Burda boşuk ayarlamaları yaplıyor ve alt çizim oluşturularak ax0 a atanıyor
# ax0 = fig.add_subplot(spec[0, :])
# # Burda yapılandırılan fig de ilk satırın tamamına bir grafik atama işlemi yapılıyor
# # Normalde 2x2 den 4 tane grafik olacakken bunu yaptığımızda ilk satırda 1 ve alt satır da 2 tane grafik olacal
# ax0.plot(portfolio_stocks.loc['2020':,'AAPL'],marker="o",linestyle="--",color="r")
# ax0.set_title("aapl Stocks Price")
# ax0.set_xlabel("Time")
# ax0.set_ylabel("Price")

# #Burda ise 1. satırın 0. stununa bir grafik atıyoruz ve bunu ax10 a eşitliyoruz
# ax10 = fig.add_subplot(spec[1, 0])
# ax10.plot(portfolio_stocks.loc['2019':,'GOOGL'],marker="v",linestyle="--",color="g")
# ax10.set_title("googl Stocks Price")
# ax10.set_xlabel("Time")
# ax10.set_ylabel("Price")

# #Burda da 1. satırın 1. stununa bir grafik (alt-çizi)atıyoruz
# ax11 = fig.add_subplot(spec[1, 1])
# ax11.plot(portfolio_stocks.loc['2019':,'IBM'],color="0")
# ax11.set_title("ibm Stocks Price")
# ax11.set_xlabel("Time")
# ax11.set_ylabel("Price")
# plt.show()

# # tek satırlık ve 2 stunluk bir alt cizim oluşturduk
# #ax[0] a istediğimiz kadar grafik atabiliyoruz istersek 4 hissenin grafiğini de yazabiliriz
# # Ama bu kodda ilk stuna iki ve 2. stuna iki grafik atadık
# fig,ax = plt.subplots(1, 2,figsize=(12,8))
# ax[0].plot(portfolio_stocks.loc['2019':,'AAPL'],marker="o",linestyle="--",color="r")
# ax[0].plot(portfolio_stocks.loc['2020':,'GOOGL'],marker="v",linestyle="--",color="g")
# ax[1].plot(portfolio_stocks.loc['2020':,'KO'],marker="*",linestyle="--",color="r")
# ax[1].plot(portfolio_stocks.loc['2019':,'IBM'],color="0")
# ax[0].set_title("aapl & google Stocks Price")
# ax[1].set_title("ko & ibm Stocks Price")
# ax[0].set_xlabel("Time")
# ax[1].set_ylabel("Price")
# plt.show()


# # Grafiklerde x eksenini veya y eksenini ortak kullanabiliriz
# # Bunu sharex ile kullanırız x ekseninde bulunan tarihi ortak kullanmış olurlar
# fig, ax = plt.subplots(2, 1, sharex=True,figsize=(12,8))
# ax[0].plot(portfolio_stocks.loc['2019':,'AAPL'],marker="o",linestyle="--",color="r")
# ax[0].plot(portfolio_stocks.loc['2020':,'GOOGL'],marker="v",linestyle="--",color="g");
# ax[1].plot(portfolio_stocks.loc['2020':,'KO'],marker="*",linestyle="--",color="r")
# ax[1].plot(portfolio_stocks.loc['2019':,'IBM'],color="0")
# ax[0].set_title("aapl & google Stocks Price")
# ax[1].set_title("ko & ibm Stocks Price")
# ax[0].set_xlabel("Time")
# ax[1].set_ylabel("Price")
# fig.tight_layout()
# plt.show()


#					grafik fitreleme
# pct.change() kullanırsak yuzdelik değişimini verir kullanmazsak direkt fiyatı verir
# ret = portfolio_stocks[['AAPL']].pct_change()
# max_ret = ret[ret['AAPL'] == ret['AAPL'].max()]
# min_ret = ret[ret['AAPL'] == ret['AAPL'].min()]

# print("Max_ret :\n",max_ret)
# print("Min_ret :\n",min_ret)

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(portfolio_stocks.index, portfolio_stocks['AAPL'],'blue' )
ax.set_xlabel('Time')
ax.set_ylabel('Price ($)',color='b')
ax.tick_params('y', colors='blue')
# tick_params ile y eksenin ozelliklerini belirliyoruz.
ax2 = ax.twinx()
# burda ise ax grafiğini ax2 ye kopyalıyor
# alt satırdaki kodda pct_change() diyerek de kırmzı grafiği oluşturuyoruz.
ax2.plot(portfolio_stocks.index,portfolio_stocks['AAPL'].pct_change(),'red')
ax2.set_xlabel('Time')
ax2.set_ylabel('Daily Return (%)',color='r')
ax2.tick_params('y', colors='red')
fig.tight_layout()
ax2.annotate("The highest drop -0.128647 ",xy=(pd.Timestamp('2020-03-16'), -0.128647),arrowprops={})
ax2.annotate("The highest increase 0.119808 ",xy=(pd.Timestamp('2020-03-13'), 0.119808),arrowprops={})
# annonte ile grafiğin en tepe değerine ve en duşuk değerinin bulunduğu kısma
# yazı yazdırır ve yazının bulunduğu kısmı bir okla gostermek istersek de arrowprops = {} kullanırız
plt.show()
