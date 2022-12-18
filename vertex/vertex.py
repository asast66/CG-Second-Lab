from typing import List


class Vertex2D:

    def __init__(self, vertex_data: List[float]):
        self.__x, self.__y = vertex_data

    def set_x(self, x: float) -> "Vertex2D":
        self.__x = x
        return self

    def get_x(self) -> float:
        return self.__x

    def set_y(self, y: float) -> "Vertex2D":
        self.__y = y
        return self

    def get_y(self) -> float:
        return self.__y


class Vertex3D:

    def __init__(self, vertex_data: List[float]):
        self.__x, self.__y, self.__z = vertex_data

    def set_x(self, x: float) -> "Vertex3D":
        self.__x = x
        return self

    def get_x(self) -> float:
        return self.__x

    def set_y(self, y: float) -> "Vertex3D":
        self.__y = y
        return self

    def get_y(self) -> float:
        return self.__y

    def set_z(self, z: float) -> "Vertex3D":
        self.__z = z
        return self

    def get_z(self) -> float:
        return self.__z
