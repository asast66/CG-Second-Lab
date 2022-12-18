from typing import List

import pygame
from pygame.surface import SurfaceType

from camera.camera import Camera
from model.model import Model3D


class Scene:

    def __init__(self, camera: Camera, models: List[Model3D]):
        self.__camera = camera
        self.__models = models
        self.__window = self.__initialize_window()

    def __initialize_window(self):
        pygame.display.set_caption("CG Lab")
        pygame.display.set_icon(SurfaceType(size=(0, 0)))
        return pygame.display.set_mode((self.__camera.get_W(), self.__camera.get_H()))

    def __clear_screen(self):
        self.__window.fill((255, 255, 255))

    def __draw_models(self):
        for model in self.__models:
            # self.__draw_model(model)
            # Получение спроецированных на экран координат модели
            w_to_v = self.__camera.get_world_to_view_matrix()
            v_to_p = self.__camera.get_view_to_projected_matrix()
            projection_matrix = v_to_p * w_to_v
            projected_vertices = model.apply_transform(projection_matrix)
            screen_vertices = []
            for vertex in projected_vertices:
                vertex = [vertex[0] / vertex[-1], vertex[1] / vertex[-1]]
                screen_vertices.append(self.__camera.get_projected_to_screen_vertex(vertex))
                # pygame.draw.circle(self.__window, (0, 0, 0), (screen_vertex[0], screen_vertex[1]), 3)
            adjacency_matrix = model.get_adjacency_matrix()
            for index in range(adjacency_matrix.get_line_num()):
                for jndex in range(adjacency_matrix.get_column_num()):
                    if index <= jndex and adjacency_matrix.get_matrix_data()[index][jndex] == 1:
                        pygame.draw.line(self.__window, (0, 0, 0),
                                         (screen_vertices[index][0], screen_vertices[index][1]),
                                         (screen_vertices[jndex][0], screen_vertices[jndex][1]))

    # Инициализация окна и запуск цикла отлавливания событий
    def show(self):
        while True:
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.exit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.exit()
                        exit()
                if event.type == pygame.MOUSEMOTION:
                    print(f'{event = }')
            # Очистка экрана
            self.__clear_screen()
            # Отрисовка моделей
            self.__draw_models()
            pygame.display.update()
