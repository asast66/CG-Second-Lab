from typing import List

from matrix.matrix import Matrix
from vertex.vertex import HomogeneousVertex


class Model3D:

    def __init__(self, vertices: List[HomogeneousVertex], adjacency_matrix: Matrix):
        self.__vertices = vertices
        self.__adjacency_matrix = adjacency_matrix
        self.__accumulated_affine_transform_matrix = Matrix([])

    def set_vertices(self, vertices: Matrix):
        self.__vertices = vertices

    def get_vertices(self) -> List[HomogeneousVertex]:
        return self.__vertices

    def set_adjacency_matrix(self, adjacency_matrix: Matrix):
        self.__adjacency_matrix = adjacency_matrix

    def get_adjacency_matrix(self) -> Matrix:
        return self.__adjacency_matrix

    def apply_transform(self, affine_matrix: Matrix) -> List[HomogeneousVertex]:
        self.__accumulated_affine_transform_matrix = affine_matrix * self.__accumulated_affine_transform_matrix
        new_vertices = []
        for vertex in self.__vertices:
            new_vertices.append(self.__accumulated_affine_transform_matrix * vertex)
        return new_vertices
