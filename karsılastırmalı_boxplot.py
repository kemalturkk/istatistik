import matplotlib.pyplot as plt

Örneklem1 = [234,198,209,197,208,188,212,202,187,204,228,193,194,216,195,238,205,227,192,219]
Örneklem2 = [198,205,221,251,218,199,204,215,213,155,213,219,231,225,213,198,259,223,227,206]

veri = [Örneklem2, Örneklem1]

fig, ax = plt.subplots()

ax.boxplot(veri, vert=False)

ax.set_yticklabels(['Örneklem 2', 'Örneklem 1'])

plt.show()
