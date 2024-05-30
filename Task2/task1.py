import scipy.stats as stats

# Данные выборок
sample1 = [1.669, 1.439, -0.775, -1.662, 2.089, -0.997, 1.840, 1.177, -0.085, 1.778,
           -0.193, 2.243, 0.487, 0.725, 0.108, 1.537, 0.107, -0.868, -0.953, -0.122]
sample2 = [2.884, 1.105, 0.731, 0.965, 2.244, 1.306, 0.643, 2.333, 0.241, 0.555,
           1.246, 1.928, 0.985, 1.728, 1.308, 1.804, 0.777, -0.105, 0.007, 1.138,
           2.081, -1.246, 2.274, 1.986, 2.024, 1.181, 0.714, 0.240, 0.194, 3.066]


# Размер выборок
n1 = len(sample1)
n2 = len(sample2)

# Уровень значимости
epsilon = 0.15

# Выборочные дисперсии
s1 = sum((x - sum(sample1)/n1) ** 2 for x in sample1) / (n1 - 1)
s2 = sum((x - sum(sample2)/n2) ** 2 for x in sample2) / (n2 - 1)

print("averageX: ", sum(sample1)/n1)
print("averageY: ", sum(sample2)/n2)
print("s1: ", s1)
print("s2: ", s2)
print("F: ", s1/s2)

# F-статистика
F = s1 / s2 if s1 > s2 else s2 / s1

# Степени свободы
v1 = n1 - 1
v2 = n2 - 1

# Критические значени
F_lower = stats.f.ppf(epsilon / 2, 19, 29)
F_upper = stats.f.ppf(1 - epsilon / 2, 19, 29)


print(f"F-статистика: {F}")
print(f"Критические значения: F_lower = {F_lower}, F_upper = {F_upper}")

# Проверка гипотезы
if F <= F_lower or F >= F_upper:
    print("Отвергаем нулевую гипотезу (дисперсии различны).")
else:
    print("Не отвергаем нулевую гипотезу (дисперсии равны).")
