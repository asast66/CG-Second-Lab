from matrix.matrix import Matrix


class Model3D:

    def __init__(self):
        self.__vertices = []
        self.__adjacency_matrix = Matrix([])
        self.__accumulated_affine_transform = Matrix([])
