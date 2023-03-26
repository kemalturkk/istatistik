#b şıkkı
import pandas as pd
import numpy as np

data= [514, 476, 497, 511, 484, 513, 471, 470, 441, 466, 443, 481, 502, 528, 459, 548, 521, 517, 
463, 478, 473, 514, 542, 519, 522, 523, 546, 487, 486, 473, 527, 470, 440, 564, 499, 523, 
484, 463, 461, 437, 555, 525, 461, 539, 466, 470, 486, 490, 543, 519]
s = pd.Series(data)
out = pd.cut(s, bins=[436,453,469,485,501,517,533,549,565])
print(out.value_counts().sort_index())

print("------------------")
print("e şıkkı")
import matplotlib.pyplot as plt

veriler = [514, 476, 497, 511, 484, 513, 471, 470, 441, 466, 443, 481, 502, 528, 459, 548, 521, 517, 463, 478, 473, 514, 542, 519, 522, 523, 546, 487, 486, 473, 527, 470, 440, 564, 499, 523, 484, 463, 461, 437, 555, 525, 461, 539, 466, 470, 486, 490, 543, 519]

frekanslar, sinif_sinirlari = np.histogram(veriler, bins=8)

n = len(veriler)  
yuzde_frekanslar = 100 * frekanslar / n 

plt.bar(sinif_sinirlari[:-1], yuzde_frekanslar, width=np.diff(sinif_sinirlari), align='edge', edgecolor='black')
plt.title("Verilerin Yüzde Frekans Histogramı")
plt.xlabel("Sınıf Sınırları")
plt.ylabel("Yüzde Frekans (%)")
plt.show()

print("-------------------------")
print ("g şıkkı")
import pandas as pd
import stemgraphic

data = ([514, 476, 497, 511, 484, 513, 471, 470, 441, 466, 443, 481, 502, 528, 459, 548, 521, 517,463, 478, 473, 514, 542, 519, 522, 523, 546, 487, 486, 473, 527, 470, 440, 564, 499, 523,484, 463, 461, 437, 555, 525, 461, 539, 466, 470, 486, 490, 543, 519])

y=pd.Series(data)
fig, ax = stemgraphic.stem_graphic(y)
fig.show()

print("-------------")
print("i şıkkı")
import pandas as pd
import stemgraphic

data = ([514, 476, 497, 511, 484, 600, 620, 513, 471, 470, 441, 466, 443, 481, 502, 528, 459, 548, 521, 517,463, 478, 473, 514, 542, 519, 522, 523, 546, 487, 486, 473, 527, 470, 440, 564, 499, 523,484, 463, 461, 437, 555, 525, 461, 539, 466, 470, 486, 490, 543, 519])

y=pd.Series(data)
fig, ax = stemgraphic.stem_graphic(y)
fig.show()



