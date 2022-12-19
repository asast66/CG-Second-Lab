from math import sin, cos
from typing import Union, List

from common.matrix import Matrix
from matrix.vector import Vector


class Camera:

    def __init__(self,
                 L: Union[int, float] = -10, R: Union[int, float] = 10,
                 B: Union[int, float] = -10, T: Union[int, float] = 10,
                 camera_vector: Vector = Vector([0, 1, 0]),
                 W: int = 800, H: int = 600,
                 F: Union[int, float] = 10,
                 D: Union[int, float] = 20):
        self.__L, self.__R, self.__B, self.__T = L, R, B, T
        self.__camera_vector = camera_vector
        self.__W, self.__H = W, H
        self.__F, self.__D = F, D

        self.__view_matrix = Matrix([])

    def get_W(self) -> int:
        return self.__W

    def get_H(self) -> int:
        return self.__H

    def get_X_rotation_matrix(self, angle: float) -> Matrix:
        return Matrix([
            [1, 0, 0, 0],
            [0, cos(angle), -sin(angle), 0],
            [0, sin(angle), cos(angle), 0],
            [0, 0, 0, 1]
        ])

    def get_Y_rotation_matrix(self, angle: float) -> Matrix:
        return Matrix([
            [cos(angle), 0, sin(angle), 0],
            [0, 1, 0, 0],
            [-sin(angle), 0, cos(angle), 0],
            [0, 0, 0, 1]
        ])

    def get_Z_rotation_matrix(self, angle: float) -> Matrix:
        return Matrix([
            [cos(angle), -sin(angle), 0, 0],
            [sin(angle), cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    def get_scaling_matrix(self, scale_vector: Vector) -> Matrix:
        return Matrix([
            [scale_vector.get_x(), 0, 0, 0],
            [0, scale_vector.get_y(), 0, 0],
            [0, 0, scale_vector.get_z(), 0],
            [0, 0, 0, 1]
        ]) * self.__view_matrix

    def get_translate_matrix(self, translate_vector: List[float]) -> Matrix:
        return Matrix([
            [1, 0, 0, translate_vector[0]],
            [0, 1, 0, translate_vector[1]],
            [0, 0, 1, translate_vector[2]],
            [0, 0, 0, 1]
        ])

    def get_world_to_view_matrix(self) -> Matrix:
        # Просто преобразование геометрии, чтобы она смотрела в камеру => набор аффинных преобразований
        # Изначально просто единичная матрица, потом будем накапливать афинные преобразования
        return self.__view_matrix

    def get_view_to_normalized_matrix(self) -> Matrix:
        return Matrix([
            [2 / (self.__R - self.__L), 0,                         (self.__L + self.__R)/(self.__R - self.__L) * 1 / self.__F,   -(self.__L + self.__R) / (self.__R - self.__L)],  # nopep8
            [0,                         2 / (self.__T - self.__B), (self.__B + self.__T) / (self.__T - self.__B) * 1 / self.__F, -(self.__B + self.__T) / (self.__T - self.__B)],  # nopep8
            [0,                         0,                         (-2 * self.__F + self.__D) / self.__D * 1 / self.__F,         -1],  # nopep8
            [0,                         0,                         -1 / self.__F,                                                 1]  # nopep8
        ]) * self.__view_matrix

    def get_normalized_to_screen_matrix(self) -> Matrix:
        return Matrix([
            [1, 0,  (self.__R - self.__L) / 2],
            [0, -1, (self.__T - self.__B) / 2],
            [0, 0,  1]
        ])

    def get_view_to_orthogonal_projected_matrix(self) -> Matrix:
        return Matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ])

    def get_view_to_perspective_projected_matrix(self) -> Matrix:
        return Matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, -1 / self.__F, 1],
        ])

    def get_projected_to_screen_vertex(self, vertex: List[float]) -> List[float]:
        return [(vertex[0] - self.__L) / (self.__R - self.__L) * self.__W,
                (self.__T - vertex[1]) / (self.__T - self.__B) * self.__H]

    def translate(self, translate_vector: List[float]):
        self.__view_matrix = self.get_translate_matrix(translate_vector) * self.__view_matrix

    def rotate(self, rotate_vector: List[float]):
        rotation_matrix = (self.get_Z_rotation_matrix(-rotate_vector[2]) *
                           self.get_Y_rotation_matrix(-rotate_vector[1]) *
                           self.get_X_rotation_matrix(-rotate_vector[0]))
        self.__view_matrix = rotation_matrix * self.__view_matrix

    def scale(self, scale_vector: Vector):
        self.__view_matrix = self.get_scaling_matrix(scale_vector) * self.__view_matrix

    # def resize_camera_screen(self):
    #     pass
