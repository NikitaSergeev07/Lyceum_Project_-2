import pygame
from SETTINGS import HEIGHT, WIDTH, GHOSTSGAME, ghost_sprites, pacman_sprite, map_on_screen
from random import randint, choice
from main import load_image


class GhostPlay(pygame.sprite.Sprite):
    """
    Класс призраков в игровом процессе
    """

    def __init__(self, num):
        super().__init__(ghost_sprites)
        image = load_image(GHOSTSGAME[num % 4][0])
        size_h = image.get_height()
        self.num = num % 4
        # скорость призрака
        self.v = 3
        self.way = 1
        self.p = 1
        self.image = image
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        if num % 2 == 0:
            self.rect.x = WIDTH // 2 + 235
            self.rect.y = HEIGHT // 2 - size_h // 2 - 20
        else:
            self.rect.x = WIDTH // 2 - 272
            self.rect.y = HEIGHT // 2 - size_h // 2 - 20

    def move(self):
        """
        Движение призрака по карте
        :return:
        """
        global stop_game
        if self.way == 1:
            self.image = load_image(GHOSTSGAME[self.num][0])
            self.rect.y -= self.v
            if pygame.sprite.collide_mask(self, map_on_screen):
                self.rect.y += 2 * self.v
                self.way = choice([2, 4])

        elif self.way == 2:
            self.image = load_image(GHOSTSGAME[self.num][3])
            self.rect.x += self.v
            if pygame.sprite.collide_mask(self, map_on_screen):
                self.rect.x -= 2 * self.v
                self.way = choice([1, 3])

        elif self.way == 3:
            self.image = load_image(GHOSTSGAME[self.num][1])
            self.rect.y += self.v
            if pygame.sprite.collide_mask(self, map_on_screen):
                self.rect.y -= 2 * self.v
                self.way = choice([2, 4])

        elif self.way == 4:
            self.image = load_image(GHOSTSGAME[self.num][2])
            self.rect.x -= self.v
            if pygame.sprite.collide_mask(self, map_on_screen):
                self.rect.x += 2 * self.v
                self.way = choice([1, 3])

        if self.way > 4:
            self.way = 1

        for pacman in pacman_sprite:
            if pygame.sprite.collide_mask(self, pacman):
                stop_game = True

    def change(self):
        """
        Изменение направления движения призрака
        :return:
        """
        last = self.way
        while self.way == 4 - last:
            self.way = randint(1, 4)