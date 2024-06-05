import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.special import kolmogorov

# Заданные данные
data = [
    0.726, 0.756, 0.274, 0.703, 0.012, 0.278, 0.225, 0.495, 0.343, 0.829,
    0.952, 0.890, 0.132, 0.829, 0.025, 0.781, 0.319, 0.413, 0.533, 0.241,
    0.661, 0.365, 0.234, 0.475, 0.756, 0.467, 0.838, 0.443, 0.028, 0.514
]

data = np.array(data)

# Функция для вычисления эмпирической функции распределения
def ecdf(data):
    x = np.sort(data)  # сортируем
    y = np.arange(1, len(data) + 1) / len(data)  # значение эмпирической функции распределения на каждой из точек данных
    return x, y

x, y = ecdf(data)

# Построение графика
plt.figure(figsize=(10, 6))
plt.step(x, y, where='post', label='Empirical CDF')

# Теоретическая функция распределения для равномерного распределения
plt.plot(x, stats.uniform.cdf(x), label='Theoretical CDF (Uniform)', linestyle='--')

plt.xlabel('Value')
plt.ylabel('ECDF')
plt.title('Empirical CDF vs Theoretical CDF')
plt.legend()
plt.grid(True)
plt.show()

# Реализация критерия Колмогорова
def kolmogorov_test(data):
    n = len(data)
    x, y = ecdf(data)

    # Максимальное положительное отклонение между ECDF и теоретической CDF
    d_plus = np.max(y - stats.uniform.cdf(x))

    # Максимальное отрицательное отклонение между ECDF и теоретической CDF
    d_minus = np.max(stats.uniform.cdf(x) - (y - 1 / n))
    # Максимальное отклонение
    d = max(d_plus, d_minus)
    return d

# Максимальное отклонение между эмпирической и теоретической функцией распределения
d_statistic = kolmogorov_test(data)

# Нормализация статистики
n = len(data)
lambda_stat = np.sqrt(n) * d_statistic

# Вычисление критического значения для уровня значимости α = 0.15
alpha = 0.15
critical_value = stats.kstwobign.ppf(1 - alpha)

# Вычисление p-value с использованием распределения Колмогорова
p_value_kolm = 1 - kolmogorov(lambda_stat)

# Вывод результатов на русском языке
print(f"Статистика Колмогорова (Ненормализованная): {d_statistic}")
print(f"Статистика Колмогорова (Нормализованная): {lambda_stat}")
print(f"Критическое значение (для уровня значимости α = 0.15): {critical_value / np.sqrt(n)}")
print(f"P-значение (Колмогоров): {p_value_kolm}")

# если вычисленная статистика D превышает критическое значение, мы отвергаем нулевую гипотезу о равномерном распределении
if d_statistic > critical_value / np.sqrt(n):
    print("Отвергаем нулевую гипотезу о равномерности распределения (d_statistic > critical_value)")
else:
    print("Нет оснований отвергнуть нулевую гипотезу о равномерности распределения (d_statistic <= critical_value)")

def kolmogorov_cdf(x):
    if x < 0:
        return 0.0
    elif x == 0:
        return 1.0
    else:
        sum = 0.0
        k = 1
        while True:
            term = (-1) ** (k - 1) * np.exp(-2 * (k * x) ** 2)
            sum += term
            if abs(term) < 1e-10:  # точность
                break
            k += 1
        return 1 - 2 * sum

x = 0.54954
kolmogorov_value = kolmogorov_cdf(x)
print("Real Level: ", kolmogorov_value)
