from typing import List, Union

from vertex.vertex import HomogeneousVertex


class MatrixError(Exception):

    def __init__(self, text: str):
        self.__text = text


class Matrix:

    def __init__(self, matrix_data: List[List[float]]):
        if len(matrix_data) != 0:
            self.__line_num = len(matrix_data)
            self.__column_num = len(matrix_data[0])
            self.__matrix_data = matrix_data
        else:
            self.__line_num = 4
            self.__column_num = 4
            self.__matrix_data = [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ]

    def get_column_num(self) -> int:
        return self.__column_num

    def get_line_num(self) -> int:
        return self.__line_num

    def get_matrix_data(self) -> List[List[float]]:
        return self.__matrix_data

    def __get_matrices_sum(self, other_matrix: "Matrix", is_subtraction: bool = False) -> "Matrix":
        coefficient = -1 if is_subtraction else 1
        if self.get_line_num() == other_matrix.get_line_num() and \
                self.get_column_num() == other_matrix.get_column_num():
            right_matrix_data = other_matrix.get_matrix_data()
            result_matrix_data = []
            for index in range(self.get_line_num()):
                line_data = []
                for jndex in range(self.get_column_num()):
                    line_data.append(self.__matrix_data[index][jndex] +
                                     right_matrix_data[index][jndex] * coefficient)
                result_matrix_data.append(line_data)
            return Matrix(result_matrix_data)
        else:
            raise MatrixError("Matrices dimensions is not equal")

    # Сложение матриц
    def __add__(self, other: "Matrix") -> "Matrix":
        return self.__get_matrices_sum(other)

    # Вычитание матриц
    def __sub__(self, other: "Matrix") -> "Matrix":
        return self.__get_matrices_sum(other, is_subtraction=True)

    def transpose(self) -> "Matrix":
        result_matrix_data = []
        for index in range(self.get_column_num()):
            result_matrix_line = []
            for jndex in range(self.get_line_num()):
                result_matrix_line.append(self.__matrix_data[jndex][index])
            result_matrix_data.append(result_matrix_line)
        return Matrix(result_matrix_data)

    def __multiply_by_const(self, const: Union[float, int]) -> "Matrix":
        result_matrix_data = []
        for index in range(self.get_line_num()):
            result_matrix_line = []
            for jndex in range(self.get_column_num()):
                result_matrix_line.append(self.__matrix_data[index][jndex] * const)
            result_matrix_data.append(result_matrix_line)
        return Matrix(result_matrix_data)

    def __multiply_by_matrix(self, other_matrix: "Matrix") -> "Matrix":
        if self.get_column_num() == other_matrix.get_line_num():
            right_transpose_matrix_data = other_matrix.transpose().get_matrix_data()
            result_matrix_data = []
            for left_line in self.__matrix_data:
                result_matrix_line = []
                for right_line in right_transpose_matrix_data:
                    new_element = sum([left_line[index] * right_line[index] for index in range(self.get_column_num())])
                    result_matrix_line.append(new_element)
                result_matrix_data.append(result_matrix_line)
            return Matrix(result_matrix_data)
        else:
            raise MatrixError("Last dimension of left matrix is not the same size as "
                              "the second-to-last dimension of right matrix.")

    def __multiply_by_homogeneous_vertex(self, vertex: HomogeneousVertex) -> HomogeneousVertex:
        new_vertex = []
        for left_line in self.__matrix_data:
            new_vertex.append(left_line[0] * vertex.get_x() +
                              left_line[1] * vertex.get_y() +
                              left_line[2] * vertex.get_z() +
                              left_line[3] * vertex.get_h())
        return HomogeneousVertex(new_vertex)

    def __multiply_by_list(self, vertex: List[float]):
        new_vertex = []
        for left_line in self.__matrix_data:
            new_vertex.append(left_line[0] * vertex[0] +
                              left_line[1] * vertex[1] +
                              left_line[2] * vertex[2])
        return new_vertex

    # Умножение матрицы на матрицу, или умножение на числовую константу
    def __mul__(self, other: Union["Matrix", float, int, HomogeneousVertex, List[float]]) -> Union["Matrix", HomogeneousVertex, List[float]]:
        if isinstance(other, float) or isinstance(other, int):
            return self.__multiply_by_const(other)
        elif isinstance(other, Matrix):
            return self.__multiply_by_matrix(other)
        elif isinstance(other, HomogeneousVertex):
            return self.__multiply_by_homogeneous_vertex(other)
        elif isinstance(other, list):
            return self.__multiply_by_list(other)
        else:
            raise MatrixError

    # Деление матрицы на числовую константу
    def __truediv__(self, other: Union[float, int]) -> "Matrix":
        result_matrix_data = []
        try:
            for index in range(self.get_line_num()):
                result_matrix_line = []
                for jndex in range(self.get_column_num()):
                    result_matrix_line.append(self.__matrix_data[index][jndex] / other)
                result_matrix_data.append(result_matrix_line)
            return Matrix(result_matrix_data)
        except ZeroDivisionError as exc:
            raise exc

    # Оператор сравнения "!="
    def __ne__(self, other: int):
        if isinstance(other, int):
            return True

    def __str__(self):
        str_matrix = f"|"
        for line in self.__matrix_data:
            str_matrix += " ".join([str(elem) for elem in line]) + "|\n|"
        return str_matrix[:-2]
