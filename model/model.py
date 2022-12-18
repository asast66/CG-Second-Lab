from typing import List, Tuple

from matrix.matrix import Matrix
from vertex.vertex import HomogeneousVertex


class Model3D:

    def __init__(self, vertices: List[List[float]], adjacency_matrix: Matrix, edges_color: Tuple[int, int, int]):
        self.__vertices = vertices
        self.__adjacency_matrix = adjacency_matrix
        self.__edges_color = edges_color
        self.__accumulated_affine_transform_matrix = Matrix([])

    def set_vertices(self, vertices: Matrix):
        self.__vertices = vertices

    def get_vertices(self) -> List[List[float]]:
        return self.__vertices

    def set_adjacency_matrix(self, adjacency_matrix: Matrix):
        self.__adjacency_matrix = adjacency_matrix

    def get_adjacency_matrix(self) -> Matrix:
        return self.__adjacency_matrix

    def get_edges_color(self) -> Tuple[int, int, int]:
        return self.__edges_color

    def apply_transform(self, transformation_matrix: Matrix) -> List[List[float]]:
        new_vertices = []
        for vertex in self.__vertices:
            h_vertex = HomogeneousVertex(vertex)
            transformed_h_vertex = transformation_matrix * h_vertex
            new_vertices.append(transformed_h_vertex.revert())
        return new_vertices
