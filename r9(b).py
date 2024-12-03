import numpy as np


# Функция для замены максимального и минимального элемента в каждой строке
def swap_max_min(B):
    n, m = B.shape  # Размерность матрицы
    for i in range(n):
        max_index = np.argmax(B[i])  # Индекс максимального элемента
        min_index = np.argmin(B[i])  # Индекс минимального элемента

        # Меняем максимальный элемент с первым и минимальный с последним
        B[i, 0], B[i, max_index] = B[i, max_index], B[i, 0]
        B[i, m - 1], B[i, min_index] = B[i, min_index], B[i, m - 1]

    return B  # Возвращаем преобразованную матрицу


# Тестируем на заданной матрице B
if __name__ == "__main__":
    B = np.array([[2, 1, 3, 4, 5], [9, 7, -3, 1, 6], [5, 4, 10, 2, 1]])
    print("Изначальная матрица:")
    print(B)
    modified_B = swap_max_min(B)
    print("Матрица после замены:")
    print(modified_B)
