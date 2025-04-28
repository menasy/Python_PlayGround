import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter('ignore')
import yfinance as yf
import seaborn as sns

tips = sns.load_dataset("tips")
print("Tips:\n",tips.head())

# İki değişken arasındaki ilişkini çizelmesi
fig,ax = plt.subplots(figsize = (10,8))
sns.scatterplot(x = "total_bill",y = "tip",data = tips)
# x = "total_bil" kısmı x ekseninde tip datasetinin total_bil stunun olacağını ifade ediyor
# y="tip" de ye ekseninde tip stunun bulunacağını ifade ediyor.
# data = tips de kullanılacak DataFrame ı işaret ediyor
ax.set_xlabel("Tip")
ax.set_ylabel("Total_Bill")
plt.show()
