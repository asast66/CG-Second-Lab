from camera.camera import Camera
from matrix.matrix import Matrix
from matrix.vector import Vector
from model.model import Model3D
from scene.scene import Scene


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
                     adjacency_matrix=adjacency_matrix)
    camera = Camera()
    camera.translate(Vector([0, -1, 0]))
    camera.rotate(Vector([0, 0.1, 0]))
    scene = Scene(camera=camera,
                  models=[model1])
    scene.show()


if __name__ == "__main__":
    main()
