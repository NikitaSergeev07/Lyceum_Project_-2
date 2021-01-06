import pygame
from main import load_image
from SETTINGS import all_maps, WIDTH, HEIGHT

class Map(pygame.sprite.Sprite):
    """
    Класс карты игры
    """

    def __init__(self, name):
        super().__init__(all_maps)
        image = load_image(name)
        size_w = image.get_width()
        size_h = image.get_height()
        self.image = image
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - size_w // 2
        self.rect.y = HEIGHT // 2 - size_h // 2