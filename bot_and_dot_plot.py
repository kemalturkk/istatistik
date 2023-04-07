import matplotlib.pyplot as plt

# Veriler
tip1 = [350, 350, 350, 358, 370, 370, 370, 371, 371, 372, 372, 384, 391, 391, 392]
tip2 = [350, 354, 359, 363, 365, 368, 369, 371, 373, 374, 376, 380, 383, 388, 392]
tip3 = [350, 361, 362, 364, 364, 365, 366, 371, 377, 377, 377, 379, 380, 380, 392]

# Kutu-çizim grafiği
plt.boxplot([tip1, tip2, tip3], labels=["Tip 1", "Tip 2", "Tip 3"])
plt.title("Karşılaştırmalı Kutu-Çizim Grafiği")
plt.xlabel("Halat Tipleri")
plt.ylabel("Yorulma Limiti (MPa)")
plt.show()

# Nokta-çizim grafiği
fig, ax = plt.subplots()
ax.plot(tip1, [1]*len(tip1), "ro", label="Tip 1")
ax.plot(tip2, [2]*len(tip2), "go", label="Tip 2")
ax.plot(tip3, [3]*len(tip3), "bo", label="Tip 3")
ax.set_yticks([1, 2, 3])
ax.set_yticklabels(["Tip 1", "Tip 2", "Tip 3"])
ax.set_xlabel("Yorulma Limiti (MPa)")
ax.set_title("Karşılaştırmalı Nokta-Çizim Grafiği")
ax.legend()
plt.show()
