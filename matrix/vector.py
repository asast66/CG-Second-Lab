from math import sqrt
from typing import List, Union


class Vector:

    def __init__(self, vector_data: List[Union[float, int]]):
        self.__x, self.__y, self.__z = vector_data

    def set_x(self, x: float) -> "Vector":
        self.__x = x
        return self

    def get_x(self) -> float:
        return self.__x

    def set_y(self, y: float) -> "Vector":
        self.__y = y
        return self

    def get_y(self) -> float:
        return self.__y

    def set_z(self, z: float) -> "Vector":
        self.__z = z
        return self

    def get_z(self) -> float:
        return self.__z

    # Вычисление длины вектора
    def __abs__(self) -> float:
        return sqrt(self.__x ** 2 + self.__y ** 2 + self.__z ** 2)

    # Векторное произведение
    def __mul__(self, other: Union["Vector", float]) -> "Vector":
        if isinstance(other, Vector):
            return Vector([self.get_y() * other.get_z() - self.get_z() * other.get_y(),
                           self.get_z() * other.get_x() - self.get_x() * other.get_z(),
                           self.get_x() * other.get_y() - self.get_y() * other.get_x()])
        elif isinstance(other, float):
            return Vector([self.__x * other, self.__y * other, self.__z * other])
        else:
            raise ValueError

    def __repr__(self):
        return f"|{self.__x} {self.__y} {self.__z}|"
