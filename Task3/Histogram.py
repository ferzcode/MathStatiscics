import numpy as np
import matplotlib.pyplot as plt
import math

# Данные выборки
data = np.array([
    0.726, 0.756, 0.274, 0.703, 0.012, 0.278, 0.225, 0.495, 0.343, 0.829,
    0.952, 0.890, 0.132, 0.829, 0.025, 0.781, 0.319, 0.413, 0.533, 0.241,
    0.661, 0.365, 0.234, 0.475, 0.756, 0.467, 0.838, 0.443, 0.028, 0.514
])

# Формула Стерджесса для определения количества интервалов
num_bins = math.ceil(math.log2(len(data)) + 1)

# Построение гистограммы
plt.hist(data, bins=num_bins, density=True, edgecolor='black')
plt.title('Гистограмма выборки')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.grid(False)
plt.show()