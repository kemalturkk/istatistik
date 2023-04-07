import matplotlib.pyplot as plt
import numpy as np

tip1 = [182, 193, 184, 201, 212, 209, 213, 199, 207, 234,
        202, 219, 225, 228, 209, 187, 203, 228, 205, 236,
        225, 194, 214, 209, 218, 219, 213, 198, 229, 198,
        202, 219, 227, 201, 219, 188, 203, 188, 205, 238,
        223, 209, 194, 216, 195, 208, 189, 204, 197, 208]

tip2 = [192, 225, 251, 203, 173, 207, 176, 216, 259, 219,
        151, 201, 191, 259, 205, 198, 223, 215, 185, 193,
        212, 241, 219, 203, 153, 227, 214, 155, 218, 194,
        213, 201, 182, 231, 206, 192, 206, 258, 208, 186,
        221, 213, 257, 204, 184, 161, 209, 219, 157, 197]
tip1 = np.sort(tip1)
tip2 = np.sort(tip2)

fig, ax = plt.subplots()

plt.rc('axes', axisbelow=True)
plt.grid(True)

plt.title('Tip I vs Tip II Plastik Boru Verileri')
plt.ylabel('Değerler')

ax.tick_params(axis='y', labelsize=8)
ax.tick_params(axis='x', labelsize=8)

leaf1 = ax.stem(tip1, linefmt='grey', markerfmt='.', use_line_collection=True, label='Tip I')
plt.setp(leaf1, 'linewidth', 1.0, 'color', 'red')

leaf2 = ax.stem(tip2, linefmt='grey', markerfmt='.', use_line_collection=True, label='Tip II')
plt.setp(leaf2, 'linewidth', 1.0, 'color', 'blue')

plt.legend(loc='upper right')

plt.show()
