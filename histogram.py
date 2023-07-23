from matplotlib import pyplot as plt
import numpy as np
# Creating dataset
a = np.array([62, 55, 68, 47, 50, 41, 62, 39, 54, 70, 56, 70, 56, 47, 
71, 55, 60, 42])
# Creating histogram
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(a, bins = [30,40,42,50,60,70,80],color = "pink", hatch='o', edgecolor='k',fill=True)
plt.show() 


print("--------------------------")


veriler = [514, 476, 497, 511, 484, 513, 471, 470, 441, 466, 443, 481, 502, 528, 459, 548, 521, 517, 463, 478, 473, 514, 542, 519, 522, 523, 546, 487, 486, 473, 527, 470, 440, 564, 499, 523, 484, 463, 461, 437, 555, 525, 461, 539, 466, 470, 486, 490, 543, 519]

frekanslar, sinif_sinirlari = np.histogram(veriler, bins=8)

n = len(veriler)  
yuzde_frekanslar = 100 * frekanslar / n 

plt.bar(sinif_sinirlari[:-1], yuzde_frekanslar, width=np.diff(sinif_sinirlari), align='edge', edgecolor='black')
plt.title("Verilerin Yüzde Frekans Histogramı")
plt.xlabel("Sınıf Sınırları")
plt.ylabel("Yüzde Frekans (%)")
plt.show()

print("---------------------------")


                                    #frekanslar belirliyken histogram veren kod 

#import matplotlib.pyplot as plt
# Veri seti frekansları
#frekanslar = [0.08, 0.68, 0.68, 0.24, 0.08, 0.013,0]

# Veri setindeki elemanların sınırları
#sınırlar = [0,25, 50, 75, 100, 200, 500]

# Histogram çizimi
#plt.hist(sınırlar, bins=sınırlar, weights=frekanslar, color='pink')

# Eksen etiketlerini ekleme
#plt.xlabel('Aralıklar')
#plt.ylabel('Frekans')

# Grafiği gösterme
#plt.show() #
