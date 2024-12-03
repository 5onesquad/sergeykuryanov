import numpy as np


# Функция для подсчета суммы и количества положительных элементов над главной диагональю
def positive_elements_above_diagonal(A):
    n = A.shape[0]  # Размерность квадратной матрицы
    positive_sum, positive_count = 0, 0  # Переменные для суммы и подсчета

    # Проходим только по элементам выше главной диагонали
    for i in range(n):
        for j in range(i + 1, n):
            if A[i, j] > 0:  # Если элемент положительный
                positive_sum += A[i, j]  # Прибавляем к сумме
                positive_count += 1  # Увеличиваем счетчик на 1

    return positive_sum, positive_count  # Возвращаем сумму и количество


# Тестируем на заданной матрице A
if __name__ == "__main__":
    A = np.array([[1, -2, 3, 4], [5, 6, -7, 8], [-9, 10, 11, -12], [13, -14, 15, 16]])
    positive_sum, positive_count = positive_elements_above_diagonal(A)
    print(f"Сумма: {positive_sum}, Количество: {positive_count}")

