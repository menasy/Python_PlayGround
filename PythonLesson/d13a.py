import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import shapiro


#					Dağılım

# 1-50 aralığında bir dizi veri oluşturma.
x = np.linspace(1,50,200)

#distrubution fonksiyon tanımlama.
def normal_dist(x , mean , sd):
	prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
	return prob_density

#ortalama ve standard deviations
mean = np.mean(x)
sd = np.std(x)

print("\nX dizisinin standart sapması:\n",sd)
print("\nX dizisinin ortalamsı:\n",mean)

#fonfksiyonu çalıştırısak.
pdf = normal_dist(x,mean,sd)

#dağılımı çizebiliriz
plt.plot(x,pdf , color = 'red')
plt.xlabel('Data points')
plt.ylabel('Probability Density')
plt.show()
# çan eğrisi şeklinde olduğu için veriler normal dağılmış diyebiliriz

#				Normal Dağılımın Özellikleri
# 1) Ortalama, mod ve medyanın hepsi eşittir.
# 2) Eğrinin altındaki toplam alan 1'e eşittir.(Toplam probability 1 dir)
# 3) Eğri ortalama etrafında simetriktir.
# 4) Verilerin %68'i ortalamanın bir standart sapması dahilindedir.
# 5) Verilerin %95'i ortalamanın iki standart sapması dahilindedir.
# 6) Verilerin %99,7'si ortalamanın üç standart sapması dahilindedir.

stat, p_value= shapiro(x)
print("p :\n",p_value) # guven değeri
print("stat :\n",stat) # test istatistiği
