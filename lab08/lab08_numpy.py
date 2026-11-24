import numpy as np

# Задание 1. Создание векторов и матриц
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("Задание 1:")
print("hours:", hours)
print("shape:", hours.shape, "ndim:", hours.ndim, "size:", hours.size, "dtype:", hours.dtype)
print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)
print("-" * 30)

# Задание 2. Индексы и срезы в векторе
print("Задание 2:")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2-5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("Массив в обратном порядке:", hours[::-1])
print("-" * 30)

# Задание 3. Строки и столбцы таблицы
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Задание 3:")
print("Форма:", temperatures.shape, "ndim:", temperatures.ndim, "size:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
print("Центральный фрагмент 2x2:\n", temperatures[0:2, 1:3])
print("-" * 30)

# Задание 4. Прямоугольные срезы
matrix = np.arange(1, 26).reshape(5, 5)
print("Задание 4:")
print("Первые три строки:\n", matrix[:3], "\nshape:", matrix[:3].shape)
print("Последние две строки:\n", matrix[-2:], "\nshape:", matrix[-2:].shape)
print("Первые два столбца:\n", matrix[:, :2], "\nshape:", matrix[:, :2].shape)
print("Фрагмент (строки 1-3, столбцы 2-4):\n", matrix[1:4, 2:5], "\nshape:", matrix[1:4, 2:5].shape)
print("Угловой блок 2x2 (правый нижний):\n", matrix[-2:, -2:], "\nshape:", matrix[-2:, -2:].shape)
print("-" * 30)

# Задание 5. Изменение массива с помощью срезов
print("Задание 5:")
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print("changed_hours:", changed_hours)
print("hours:", hours)
# .copy() необходима, чтобы создать независимую копию. Без нее changed_hours был бы ссылкой на ту же память, и изменяя его, мы бы стерли исходный массив hours.

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print("Измененная матрица:\n", changed_matrix)
print("Исходная матрица:\n", matrix)
print("-" * 30)

# Задание 6. Изменение формы
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T
print("Задание 6:")
print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)
# reshape(3, 4) работает, так как 3 * 4 = 12 (совпадает с числом элементов). reshape(5, 3) вызовет ошибку, так как 5 * 3 = 15, а элементов всего 12.
