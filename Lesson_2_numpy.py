# ex 1
# импортируем библиотеки
import numpy as np

# получаем массив а 5Х2
a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])
print("Массив а")
print(a)

# находим средние значения по каждому признаку
mean_a = np.mean(a, axis=0)
print("Массив mean_a")
print(mean_a)

# ex_2
# находим массив a_centered
a_centered = a - mean_a
print("Массив a_centered")
print(a_centered)

# ex_3
# находим скалярные произведения столбцов
a_centered_sp = np.dot(a_centered[:, 0], a_centered[:, 1])
print("Величина a_centered_sp")
print(a_centered_sp)

# делим полученную ведичину на  N-1
covar = a_centered_sp / (a_centered.shape[0]-1)
print("Ковариация признаков")
print(covar)

# ex_4
# проверка
print("Проверка")
print(np.cov(np.transpose(a))[0, 1])

