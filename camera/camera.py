from math import sin, cos
from typing import Union

from matrix.matrix import Matrix
from matrix.vector import Vector


class Camera:

    def __init__(self,
                 L: Union[int, float] = 0, R: Union[int, float] = 10,
                 B: Union[int, float] = 0, T: Union[int, float] = 6,
                 camera_vector: Vector = Vector([0, 1, 0]),
                 W: int = 800, H: int = 600,
                 F: Union[int, float] = 1,
                 D: Union[int, float] = 20):
        self.__L, self.__R, self.__B, self.__T = L, R, B, T
        self.__camera_vector = camera_vector
        self.__W, self.__H = W, H
        self.__F, self.__D = F, D

    def get_W(self) -> int:
        return self.__W

    def get_H(self) -> int:
        return self.__H

    @staticmethod
    def get_X_rotation_matrix(angle) -> Matrix:
        return Matrix([
            [1, 0, 0, 0],
            [0, cos(angle), -sin(angle), 0],
            [0, sin(angle), cos(angle), 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def get_Y_rotation_matrix(angle) -> Matrix:
        return Matrix([
            [cos(angle), 0, sin(angle), 0],
            [0, 1, 0, 0],
            [-sin(angle), 0, cos(angle), 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def get_Z_rotation_matrix(angle) -> Matrix:
        return Matrix([
            [cos(angle), -sin(angle), 0, 0],
            [sin(angle), cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def get_scaling_matrix(scale_vector: Vector) -> Matrix:
        return Matrix([
            [scale_vector.get_x(), 0, 0, 0],
            [0, scale_vector.get_y(), 0, 0],
            [0, 0, scale_vector.get_z(), 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def get_shift_matrix(shift_vector: Vector) -> Matrix:
        return Matrix([
            [1, 0, 0, shift_vector.get_x()],
            [0, 1, 0, shift_vector.get_y()],
            [0, 0, 1, shift_vector.get_z()],
            [0, 0, 0, 1]
        ])

    def get_world_to_view_transition_matrix(self) -> Matrix:
        # Просто преобразование геометрии, чтобы она смотрела в камеру => набор аффинных преобразований
        # Изначально просто единичная матрица, потом будем накапливать афинные преобразования
        return Matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    def get_view_to_normalized_transition_matrix(self) -> Matrix:
        return Matrix([
            [2 / (self.__R - self.__L), 0,                         (self.__L + self.__R)/(self.__R - self.__L) * 1 / self.__F,   -(self.__L + self.__R) / (self.__R - self.__L)],  # nopep8
            [0,                         2 / (self.__T - self.__B), (self.__B + self.__T) / (self.__T - self.__B) * 1 / self.__F, -(self.__B + self.__T) / (self.__T - self.__B)],  # nopep8
            [0,                         0,                         (-2 * self.__F + self.__D) / self.__D * 1 / self.__F,         -1],  # nopep8
            [0,                         0,                         -1 / self.__F,                                                 1]  # nopep8
        ])

    def get_normalized_to_screen_transition_matrix(self) -> Matrix:
        return Matrix([
            [1, 0,  (self.__R - self.__L) / 2],
            [0, -1, (self.__T - self.__B) / 2],
            [0, 0,  1]
        ])

    def resize_camera_screen(self):
        pass

    def translate(self):
        pass

    def rotate(self):
        pass

    def scale(self):
        pass
