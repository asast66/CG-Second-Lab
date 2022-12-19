from math import pi

from camera.camera import Camera
from common.colors import Colors
from common.matrix import Matrix
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
                     edges_color=Colors.DARK_WHITE,
                     edges_width=2)
    camera = Camera(L=-9, R=9, B=-7, T=7, F=10, D=10)
    camera.translate([2, 0.5, 2])
    camera.rotate([-pi / 10, pi / 4, 0])
    scene = Scene(camera=camera,
                  models=[model1],
                  projection_type=ProjectionType.PERSPECTIVE)
    scene.show()

    # TODO:
    #  1. Добавить скейлинг при прокрутке мыши
    #  2. Добавить отрисовку осей координат в сцене
    #  3. (Добавить составные АП, но не факт что это нужно)
    #  4. Отрефакторить код классов Matrix и Vector, возможно удалить точки и вектор
    #  5. Перенести matrix.py в common.py


if __name__ == "__main__":
    main()
