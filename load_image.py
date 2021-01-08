import os
import pygame

def load_image(name):
    """
    Загрузка картинки из файла в программу
    :param name: имя файла с картинкой
    :return: изображение, готовое для работы
    """
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        return image
    except pygame.error as message:
        print('Не можем загрузить изображение:', name)
        raise SystemExit(message)