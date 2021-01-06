import os
import sys
import pygame
from random import randint, choice
from SETTINGS import FPS, WIDTH, HEIGHT, CHANGE, CONTINUEMOVE, GHOSTS, GHOSTSGAME, INTRO, FULLNAME, screen, all_sprites, \
    all_ghosts, all_points, all_maps, all_rects, ghost_sprites, pacman_kill, pacman_sprite, clock, map_on_screen, \
    map_on_screen_num
from Ghost import Ghost
from GhostInGame import GhostPlay

pygame.init()
pygame.display.set_caption('Pacman')
pygame.mouse.set_visible(False)


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
