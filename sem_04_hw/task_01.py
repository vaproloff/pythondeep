# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    # Проверка, что длина все внутренних списков одинаковая
    if not len({len(matrix[i]) for i in range(len(matrix))}) == 1:
        return matrix

    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def print_matrix(matrix: list[list[int]]):
    # Определяем максимальную ширину ячейки матрицы
    max_length = max(map(lambda x: max(map(lambda y: len(str(y)), x)), matrix))

    for i in range(len(matrix)):
        print('|', end=' ')
        for j in range(len(matrix[i])):
            print(f'{matrix[i][j]:>{max_length}}', end=' ')
        print('|')


matr = [[11, 22, 33, 44], [55, 66, 77, 88]]
print('Исходная матрица:')
print_matrix(matr)
print('Транспонированная матрица:')
print_matrix(transpose_matrix(matr))
