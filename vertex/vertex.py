class Vertex2D:

    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

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

    def __init__(self, x: float, y: float, z: float):
        self.__x = x
        self.__y = y
        self.__z = z

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
