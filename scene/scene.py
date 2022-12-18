from enum import Enum
from typing import List

import pygame
from pygame.surface import SurfaceType

from camera.camera import Camera
from common.colors import Colors
from matrix.vector import Vector
from model.model import Model3D


class ProjectionType(Enum):
    ORTHOGONAL = "orthogonal"
    PERSPECTIVE = "perspective"


class MouseState:

    def __init__(self, is_dragging: bool = False, is_ctrl_dragging: bool = False):
        self.__is_dragging = is_dragging
        self.__is_ctrl_dragging = is_ctrl_dragging

    def is_dragging(self) -> bool:
        return self.__is_dragging

    def is_ctrl_dragging(self) -> bool:
        return self.__is_ctrl_dragging

    def switch_dragging(self):
        self.__is_dragging = not self.__is_dragging

    def switch_ctrl_dragging(self):
        self.__is_ctrl_dragging = not self.__is_ctrl_dragging


class Scene:

    def __init__(self, camera: Camera, models: List[Model3D], projection_type: ProjectionType):
        self.__camera = camera
        self.__models = models
        self.__projection_type = projection_type
        self.__window = self.__initialize_window()
        self.__clock = self.__initialize_clock()

        self.__rotation_k = 0.1

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
            print(f'{screen_vertices = }')
            adjacency_matrix = model.get_adjacency_matrix()
            for index in range(adjacency_matrix.get_line_num()):
                for jndex in range(adjacency_matrix.get_column_num()):
                    if index <= jndex and adjacency_matrix.get_matrix_data()[index][jndex] == 1:
                        pygame.draw.line(self.__window, model.get_edges_color(),
                                         (screen_vertices[index][0], screen_vertices[index][1]),
                                         (screen_vertices[jndex][0], screen_vertices[jndex][1]))

    # Инициализация окна и запуск цикла отлавливания событий
    def show(self):
        prev_pos = [0, 0]
        delta_pos = [0, 0]
        mouse_state = MouseState()
        while True:
            self.__clock.tick(10)
            # Обработка событий
            pressed = pygame.key.get_pressed()
            ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.exit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.exit()
                        exit()
                if event.type == pygame.MOUSEWHEEL:
                    print(f'{event = }')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Ctrl + левая кнопка мыши
                    if event.button == 1 and ctrl_held and not mouse_state.is_ctrl_dragging():
                        mouse_state.switch_ctrl_dragging()
                    # Левая кнопка мыши
                    elif event.button == 1 and not mouse_state.is_dragging():
                        mouse_state.switch_dragging()
                if event.type == pygame.MOUSEBUTTONUP and mouse_state.is_dragging():
                    mouse_state.switch_dragging()
                    prev_pos = [0, 0]
                    delta_pos = [0, 0]
                if event.type == pygame.MOUSEBUTTONUP and mouse_state.is_ctrl_dragging():
                    mouse_state.switch_ctrl_dragging()
                if event.type == pygame.MOUSEMOTION and mouse_state.is_dragging():
                    if prev_pos == delta_pos:
                        prev_pos = [event.pos[0], event.pos[1]]
                    else:
                        delta_pos[0] = event.pos[0] - prev_pos[0]
                        self.__camera.rotate(Vector([delta_pos[0] * self.__rotation_k, 0, 0]))
                        delta_pos[1] = event.pos[1] - prev_pos[1]
                        self.__camera.rotate(Vector([0, delta_pos[1] * self.__rotation_k, 0]))
                        print(f'{delta_pos = }')
                        # self.__camera.rotate(Vector([delta_pos[0], delta_pos[1], 0]))
                        prev_pos = [event.pos[0], event.pos[1]]
                if event.type == pygame.MOUSEMOTION and mouse_state.is_ctrl_dragging():
                    print(f'ctrl + 1, {event = }')
            # Очистка экрана
            self.__clear_screen()
            # Отрисовка моделей
            self.__draw_models()
            pygame.display.update()
