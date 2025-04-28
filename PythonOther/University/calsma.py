import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter('ignore')

df_07 = pd.DataFrame([['Ali',18,'istanbul'],['Veli',25,'istanbul'],['Ayşe',20,'izmir'],['Fatma',23,'ankara']],
 columns=['isimler','yaşlar','doğum_yerleri'])


indian_rent = pd.read_csv("House_Rent_Dataset.csv")
indian_rent.columns = ['ilan_tarihi','oda_sayısı','kira','boyut','bulunduğu_kat','zemin_tipi','lokasyon_türü',
 'şehir','mobilyalı_mobilyasız','kiracı_tercihi','banyo_sayısı','erişim_yolu']

print("data : \n",indian_rent)
# yer = indian_rent[indian_rent['şehir'] == 'Delhi'][indian_rent['banyo_sayısı'] == 2][indian_rent['kira'] <= 20000]
yerp = indian_rent[(indian_rent['şehir'] == 'Delhi')&(indian_rent['banyo_sayısı'] == 2)&(indian_rent['kira'] <= 20000)]
mx = yerp[yerp["boyut"] == yerp["boyut"].max()]
print(mx)
# kirası en yuksek ve boyutu en duşuk

memo = indian_rent[indian_rent["boyut"] == indian_rent["boyut"].max()]
kra = memo[memo["kira"] == memo["kira"].min()]
print("memo : \n",kra)

# print("grp : \n", indian_rent[indian_rent["şehir"] == "Delhi"].groupby('kira').max("a"))
print("GRP : \n", indian_rent.groupby('şehir').mean("da"))

