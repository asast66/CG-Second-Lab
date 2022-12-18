from camera.camera import Camera
from common.colors import Colors
from matrix.matrix import Matrix
from matrix.vector import Vector
from model.model import Model3D
from scene.scene import Scene, ProjectionType


def main():
    vertices = [
        [2, 0, 2],
        [2, 0, -2],
        [-2, 0, -2],
        [-2, 0, 2],
        [2, 2, 2],
        [2, 2, -2],
        [-2, 2, -2],
        [-2, 2, 2]
    ]
    adjacency_matrix = Matrix([
        [0, 1, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0],
    ])
    model1 = Model3D(vertices=vertices,
                     adjacency_matrix=adjacency_matrix,
                     edges_color=Colors.DARK_WHITE)
    camera = Camera(L=-9, R=9, B=-7, T=7, F=7, D=5)
    camera.translate(Vector([0, 0, 0]))
    camera.rotate(Vector([-0.3, 0.3, 0.3]))
    scene = Scene(camera=camera,
                  models=[model1],
                  projection_type=ProjectionType.ORTHOGONAL)
    scene.show()


if __name__ == "__main__":
    main()
