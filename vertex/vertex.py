from typing import List, Union


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


class HomogeneousVertex:
    def __init__(self, vertex_data: Union[List[float], Vertex2D, Vertex3D]):
        if isinstance(vertex_data, list):
            self.__x, self.__y, self.__z = vertex_data[0], vertex_data[1], vertex_data[2]
        elif isinstance(vertex_data, Vertex2D):
            self.__x, self.__y, self.__z = vertex_data.get_x(), vertex_data.get_y(), 0
        elif isinstance(vertex_data, Vertex3D):
            self.__x, self.__y, self.__z = vertex_data.get_x(), vertex_data.get_y(), vertex_data.get_z()
        self.__h = 1

    def set_x(self, x: float):
        self.__x = x

    def get_x(self) -> float:
        # return self.__x / self.__h
        return self.__x

    def set_y(self, y: float):
        self.__y = y

    def get_y(self) -> float:
        # return self.__y / self.__h
        return self.__y

    def set_z(self, z: float):
        self.__z = z

    def get_z(self) -> float:
        # return self.__z / self.__h
        return self.__z

    def set_h(self, h: Union[int, float]):
        self.__h = h

    def get_h(self) -> Union[int, float]:
        return self.__h

    def __repr__(self):
        return f"|{self.__x} {self.__y} {self.__z} {self.__h}|"

    def __str__(self):
        return f"|{self.__x} {self.__y} {self.__z} {self.__h}|"
