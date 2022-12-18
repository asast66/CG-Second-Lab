from camera.camera import Camera
from model.model import Model3D


class Scene:

    def __init__(self, camera: Camera, model: Model3D):
        self.__camera = camera
        self.__model = model
        self.__window = self.__initialize_window()

    def __initialize_window(self):
        return []

    def __draw_model(self):
        pass

    def __draw_3d_axis(self):
        pass

    def __clear_screen(self):
        pass
