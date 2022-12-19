from enum import Enum
from math import pi
from typing import List, Tuple

import pygame
from pygame.event import Event
from pygame.surface import SurfaceType

from camera.camera import Camera
from common.colors import Colors
from model.model import Model3D


class ProjectionType(Enum):
    ORTHOGONAL = "orthogonal"
    PERSPECTIVE = "perspective"


class MouseState:

    def __init__(self, is_dragging: bool = False, is_ctrl_dragging: bool = False):
        self.__is_dragging = is_dragging
        self.__is_shift_dragging = is_ctrl_dragging
        self.__prev_mouse_pos = (0, 0)
        self.__delta_mouse_pos = (0, 0)

    def is_dragging(self) -> bool:
        return self.__is_dragging

    def is_shift_dragging(self) -> bool:
        return self.__is_shift_dragging

    def switch_dragging(self):
        self.__is_dragging = not self.__is_dragging

    def switch_shift_dragging(self):
        self.__is_shift_dragging = not self.__is_shift_dragging

    def get_mouse_delta(self, event: Event) -> Tuple[int, int]:
        if self.__prev_mouse_pos == self.__delta_mouse_pos:
            self.__prev_mouse_pos = event.pos
        else:
            self.__delta_mouse_pos = (event.pos[0] - self.__prev_mouse_pos[0], event.pos[1] - self.__prev_mouse_pos[1])
            self.__prev_mouse_pos = event.pos
        return self.__delta_mouse_pos

    def clear_pos(self):
        self.__is_dragging = False
        self.__is_shift_dragging = False
        self.__prev_mouse_pos = (0, 0)
        self.__delta_mouse_pos = (0, 0)


class Scene:

    def __init__(self, camera: Camera, models: List[Model3D], projection_type: ProjectionType):
        self.__camera = camera
        self.__models = models
        self.__projection_type = projection_type
        self.__window = self.__initialize_window()
        self.__clock = self.__initialize_clock()

        self.__rotation_k = pi / 360
        self.__translation_k = 0.025

    def __initialize_window(self):
        pygame.display.set_caption("CG Lab")
        pygame.display.set_icon(SurfaceType(size=(0, 0)))
        return pygame.display.set_mode((self.__camera.get_W(), self.__camera.get_H()))

    def __initialize_clock(self):
        return pygame.time.Clock()

    def __clear_screen(self):
        self.__window.fill(Colors.GRAY)

    def __draw_models(self):
        for model in self.__models:
            # Получение спроецированных на экран координат модели
            w_to_v = self.__camera.get_world_to_view_matrix()
            if self.__projection_type == ProjectionType.ORTHOGONAL:
                v_to_p = self.__camera.get_view_to_orthogonal_projected_matrix()
            else:
                v_to_p = self.__camera.get_view_to_perspective_projected_matrix()
            projection_matrix = v_to_p * w_to_v
            projected_vertices = model.apply_transform(projection_matrix)
            screen_vertices = []
            for vertex in projected_vertices:
                vertex = [vertex[0] / vertex[-1], vertex[1] / vertex[-1]]
                screen_vertices.append(self.__camera.get_projected_to_screen_vertex(vertex))
            adjacency_matrix = model.get_adjacency_matrix()
            for index in range(adjacency_matrix.get_line_num()):
                for jndex in range(adjacency_matrix.get_column_num()):
                    if index <= jndex and adjacency_matrix.get_matrix_data()[index][jndex] == 1:
                        pygame.draw.line(self.__window,
                                         model.get_edges_color(),
                                         (screen_vertices[index][0], screen_vertices[index][1]),
                                         (screen_vertices[jndex][0], screen_vertices[jndex][1]),
                                         model.get_edges_width())

    # Инициализация окна и запуск цикла отлавливания событий
    def show(self):
        mouse_state = MouseState()
        while True:
            self.__clock.tick(60)
            # Обработка событий
            pressed = pygame.key.get_pressed()
            shift_held = pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.exit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.exit()
                        exit()
                if event.type == pygame.MOUSEWHEEL:
                    print(f'{event = }, {type(event) = }')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Shift + левая кнопка мыши
                    if event.button == 1 and shift_held and not mouse_state.is_shift_dragging():
                        mouse_state.switch_shift_dragging()
                    # Левая кнопка мыши
                    elif event.button == 1 and not mouse_state.is_dragging():
                        mouse_state.switch_dragging()
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_state.clear_pos()
                if event.type == pygame.MOUSEMOTION and mouse_state.is_dragging():
                    mouse_delta = mouse_state.get_mouse_delta(event)
                    rot_vec = [-mouse_delta[1] * self.__rotation_k, -mouse_delta[0] * self.__rotation_k, 0]
                    self.__camera.rotate(rot_vec)
                if event.type == pygame.MOUSEMOTION and mouse_state.is_shift_dragging():
                    mouse_delta = mouse_state.get_mouse_delta(event)
                    t_vec = [mouse_delta[0] * self.__translation_k, -mouse_delta[1] * self.__translation_k, 0]
                    self.__camera.translate(t_vec)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.__camera.rotate([0, -self.__rotation_k, 0])

            # Очистка экрана
            self.__clear_screen()
            # Отрисовка моделей
            self.__draw_models()
            pygame.display.update()
