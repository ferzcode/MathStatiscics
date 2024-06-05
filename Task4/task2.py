import numpy as np
from scipy.stats import chi2

# Данные
data = [
    0.726, 0.756, 0.274, 0.703, 0.012, 0.278, 0.225, 0.495, 0.343, 0.829,
    0.952, 0.890, 0.132, 0.829, 0.025, 0.781, 0.319, 0.413, 0.533, 0.241,
    0.661, 0.365, 0.234, 0.475, 0.756, 0.467, 0.838, 0.443, 0.028, 0.514
]

n = len(data)

# Определяем границы интервалов
bins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
probability = 0.2

# Вычисляем частоты для каждого интервала
hist, bin_edges = np.histogram(data, bins=bins)

# Выводим частоты
print("Frequencies", hist)

chi2_value = 0
for i in range(5):
    chi2_value += ((hist[i] - n * probability) ** 2) / (n * probability)
print("Chi2: ", chi2_value)

epsilon = 0.15

confidence_level = 1 - epsilon
degrees_of_freedom = n - 1

quantile = chi2.ppf(confidence_level, degrees_of_freedom)

print("Quantile of Chi2: ", quantile)