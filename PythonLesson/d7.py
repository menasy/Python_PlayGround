import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime

google = yf.download('GOOGL',start='2017-1-1',end='2019-12-31')
print(google)
print (google.info())

#						Asfreq()
print("-------\nASFREQ:\n-------")
print(google.asfreq('D').info())

print("Asfreq2 :\n",google.asfreq('D').head(32))
# // incexler tarihken 1 2 3 4 şeklinde sıralı gunler varsa ve orneğin 2. gunun verileri
# yoksa 2.tarihi de listeler ve verilere nan atar.

google_kapanış = google[['Close']]
print("Google kapanış : \n",google_kapanış)

print("\n-	-	-	-	Resample weak/last-first	-	-	-\n")
print("First Weak:\n",google_kapanış.resample('W').first())
# Tarih olarak gene sonu gosteriyor ama aldığı veri o haftanın ilk gunudur.
print("First Weak:\n",google_kapanış.resample('W').last())
# tarih sonu gosteriyor yani first ile aynı fakat her haftanın son gununun verisini veriyor

print("\n-	-	-	-	Resample Month/last-first	-	-	-\n")
print("First:\n",google_kapanış.resample('M').first())
# first yaptığımızda o ayın ilk verisini verir tarih kısmı son değerigosterse de veri ilk olandır.
print("Last : \n",google_kapanış.resample('M').last())
# last yaptığımızda ise her ayın son verisini veriyor.


print("\n-	-	-	-	Resample Year(Annual)/mean()	-	-	-\n")
print("Mean :\n",google_kapanış.resample('Y').mean())
# verilerin yıllık ortalamasını verir bunu 'A' annual ya da 'Y' year kullanarak alabilirsin
print("\ngogle kapanıs:\n",google_kapanış)
