from camera.camera import Camera
from matrix.matrix import Matrix
from model.model import Model3D
from scene.scene import Scene
from vertex.vertex import HomogeneousVertex


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
    homogeneous_vertices = [HomogeneousVertex(vertex) for vertex in vertices]
    adjacency_matrix = Matrix([
        [0, 1, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 1, 0],
    ])
    model = Model3D(vertices=homogeneous_vertices,
                    adjacency_matrix=adjacency_matrix)
    camera = Camera()
    scene = Scene(camera=camera,
                  model=model)
    scene.show()


if __name__ == "__main__":
    main()
