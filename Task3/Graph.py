import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF

# Данные выборки
data = [
    0.726, 0.756, 0.274, 0.703, 0.012, 0.278, 0.225, 0.495, 0.343, 0.829,
    0.952, 0.890, 0.132, 0.829, 0.025, 0.781, 0.319, 0.413, 0.533, 0.241,
    0.661, 0.365, 0.234, 0.475, 0.756, 0.467, 0.838, 0.443, 0.028, 0.514
]

# Построение эмпирической функции распределения
ecdf = ECDF(data)

plt.figure(figsize=(10, 5))
plt.step(ecdf.x, ecdf.y, where='post')
plt.title('Эмпирическая функция распределения')
plt.xlabel('Значения')
plt.ylabel('Эмпирическая функция распределения')
plt.grid(True)
plt.show()