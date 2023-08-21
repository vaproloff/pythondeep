import unittest


class MatrixError(Exception):
    pass


class MatrixConsistencyError(MatrixError):
    def __init__(self, matrix: list[list]):
        self.matrix = matrix

    def __str__(self):
        return 'All incoming matrix rows should be the same length!'


class MatrixAdditionError(MatrixError):
    def __init__(self, self_rows: int, self_cols: int, other_rows: int, other_cols: int):
        self.self_rows = self_rows
        self.self_cols = self_cols
        self.other_rows = other_rows
        self.other_cols = other_cols

    def __str__(self):
        return f'Matrix cannot be added: Rows and columns of both matrix should be equal!\n' \
               f'Rows of matrixes are: {self.self_rows}, {self.other_rows}.\n' \
               f'Columns of matrixes are: {self.self_cols}, {self.other_cols}.'


class MatrixMultiplyError(MatrixError):
    def __init__(self, self_cols: int, other_rows: int):
        self.self_cols = self_cols
        self.other_rows = other_rows

    def __str__(self):
        return f'Matrix cannot be multiplied: ' \
               f'columns quantity of the first matrix ({self.self_cols}) ' \
               f'should be equal to rows quantity of the second matrix ({self.other_rows})!'


class Matrix:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __new__(cls, matrix: list[list[int]]):
        if type(matrix) is not list:
            raise TypeError(f'Incoming matrix should be list. Current type: {type(matrix)}')

        if len({len(row) for row in matrix}) != 1:
            raise MatrixConsistencyError(matrix)

        return super().__new__(cls)

    def concat_rows(self):
        return [item for row in self.matrix for item in row]

    def __is_lengths_equal(self, other):
        return self.rows == other.rows and self.cols == other.cols

    def __eq__(self, other):
        if self.__is_lengths_equal(other):
            return sorted(self.concat_rows()) == sorted(other.concat_rows())
        return False

    def __lt__(self, other):
        if self.rows * self.cols < other.rows * other.cols:
            return True
        elif self.rows * self.cols > other.rows * other.cols:
            return False
        else:
            return sum(self.concat_rows()) < sum(other.concat_rows())

    def __le__(self, other):
        if self.rows * self.cols < other.rows * other.cols:
            return True
        elif self.rows * self.cols > other.rows * other.cols:
            return False
        else:
            return sum(self.concat_rows()) <= sum(other.concat_rows())

    def __add__(self, other):
        if self.__is_lengths_equal(other):
            sum_matrix = []
            for row_i in range(self.rows):
                sum_row = []
                for item_i in range(self.cols):
                    sum_row.append(self.matrix[row_i][item_i] + other.matrix[row_i][item_i])
                sum_matrix.append(sum_row)
            return Matrix(sum_matrix)
        else:
            raise MatrixAdditionError(self.rows, self.cols, other.rows, other.cols)

    def __mul__(self, other):
        if self.cols == other.rows:
            mul_matrix = []
            for row in self.matrix:
                mul_row = []
                for col_i in range(other.cols):
                    mul_row.append(sum(row[i] * other.matrix[i][col_i] for i in range(self.cols)))
                mul_matrix.append(mul_row)
            return Matrix(mul_matrix)
        else:
            raise MatrixMultiplyError(self.cols, other.rows)

    def __str__(self):
        max_length = max(map(lambda x: max(map(lambda y: len(str(y)), x)), self.matrix))
        output = ''
        for i in range(len(self.matrix)):
            output += '| '
            for j in range(len(self.matrix[i])):
                output += f'{self.matrix[i][j]:>{max_length}} '
            output += '|\n'
        return output

    def __repr__(self):
        return f'Matrix({self.matrix})'


class TestMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix_1 = Matrix([[1, 22, 33, 44], [55, 66, 77, 88]])
        self.matrix_2 = Matrix([[44, 33, 1], [66, 55, 88]])
        self.matrix_3 = Matrix([[40, 25], [60, 3], [100, 1], [55, 55]])
        self.matrix_4 = Matrix([[5, 6, 7], [8, 9, 10]])
        self.matrix_5 = Matrix([[9, 5, 8], [7, 10, 6]])

    def test_addition(self):
        self.assertEqual(self.matrix_2 + self.matrix_4, Matrix([[49, 39, 8], [74, 64, 98]]))

    def test_multiplying(self):
        self.assertEqual(self.matrix_1 * self.matrix_3, Matrix([[7080, 2544], [18700, 6490]]))

    def test_equality(self):
        self.assertEqual(self.matrix_4, self.matrix_5)

    def test_not_equality(self):
        self.assertNotEqual(self.matrix_1, self.matrix_5)

    def test_comparison_1(self):
        self.assertTrue(self.matrix_1 > self.matrix_5)

    def test_comparison_2(self):
        self.assertTrue(self.matrix_2 > self.matrix_4)

    def test_comparison_3(self):
        self.assertTrue(self.matrix_1 > self.matrix_3)

    def test_addition_error(self):
        self.assertRaises(MatrixAdditionError, Matrix.__add__, self.matrix_1, self.matrix_2)

    def test_multiply_error(self):
        self.assertRaises(MatrixMultiplyError, Matrix.__mul__, self.matrix_1, self.matrix_2)

    def test_creating_error(self):
        self.assertRaises(MatrixConsistencyError, Matrix.__new__, Matrix, [[1, 22, 444], [55, 666, 77, 88]])

    def test_create_invalid_type(self):
        self.assertRaises(TypeError, Matrix.__new__, Matrix, '[444, 33, 1], [666, 55, 88]')


if __name__ == '__main__':
    unittest.main(verbosity=2)
