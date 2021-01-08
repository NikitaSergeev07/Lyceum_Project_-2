import pygame
from SETTINGS import all_points, WIDTH, HEIGHT, map_on_screen_num
from load_image import load_image


class Points(pygame.sprite.Sprite):
    """
    Загрузка и расстановка баллов на карте
    """

    def __init__(self):
        super().__init__(all_points)
        if map_on_screen_num == 3:
            image = load_image('points_level3.png')
        else:
            image = load_image('points.png')
        size_w = image.get_width()
        size_h = image.get_height()
        self.image = image
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - size_w // 2
        self.rect.y = HEIGHT // 2 - size_h // 2
