import pygame
from pygame.surface import SurfaceType

from camera.camera import Camera
from model.model import Model3D


class Scene:

    def __init__(self, camera: Camera, model: Model3D):
        self.__camera = camera
        self.__model = model
        self.__window = self.__initialize_window()

    def __initialize_window(self):
        pygame.display.set_caption("CG Lab")
        pygame.display.set_icon(SurfaceType(size=(0, 0)))
        return pygame.display.set_mode((self.__camera.get_W(), self.__camera.get_H()))

    def __draw_model(self):
        pass

    def __draw_3d_axis(self):
        pass

    def __clear_screen(self):
        pass

    # Начало отрисовки окна и запуск цикла отлавливания событий
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
            # Очистка экрана
            self.__window.fill((255, 255, 255))
            # Отрисовка приколов
            # ...
            pygame.display.update()
