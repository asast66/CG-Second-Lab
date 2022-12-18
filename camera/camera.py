from typing import Union

from matrix.matrix import Matrix


class Camera:

    def __init__(self, L: Union[int, float] = 0, R: Union[int, float] = 10,
                 B: Union[int, float] = 0, T: Union[int, float] = 6,
                 W: int = 800, H: int = 600):
        self.__L = L
        self.__R = R
        self.__B = B
        self.__T = T

        self.__W = W
        self.__H = H

    def get_W(self) -> int:
        return self.__W

    def get_H(self) -> int:
        return self.__H

    def get_world_to_view_transition_matrix(self) -> Matrix:
        return Matrix([

        ])

    def get_view_to_normalized_transition_matrix(self) -> Matrix:
        return Matrix([

        ])

    def get_normalized_to_screen_transition_matrix(self) -> Matrix:
        return Matrix([

        ])

    def resize_camera_screen(self):
        pass

    # def draw_edges(self):
    #     pass

    # def draw_3d_axis(self):
    #     pass
