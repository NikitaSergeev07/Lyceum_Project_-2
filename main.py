import pygame
import math
from random import randrange
import random
import copy
import os
from settings_for_startscreen import screen, all_sprites, all_ghosts, mouse_on_screen


# Функция остановки времени
def pause(time):
    cur = 0
    while not cur == time:
        cur += 1


# Функция для проверки возможности передвижения и для отсллеживания сталкиваний
def canMove(row, col):
    if col == -1 or col == len(gameBoard[0]):
        return True
    if gameBoard[int(row)][int(col)] != 3:
        return True
    return False


# Возрождение после смерти
def reset():
    global game
    game.ghosts = [Ghost(14.0, 13.5, "red", 0), Ghost(17.0, 11.5, "blue", 1), Ghost(17.0, 13.5, "pink", 2),
                   Ghost(17.0, 15.5, "orange", 3)]
    for ghost in game.ghosts:
        ghost.setTarget()
    game.pacman = Pacman(26.0, 13.5)
    game.lives -= 1
    game.paused = True
    game.render()

def load_image(name):
    """
    Загрузка картинки из файла в программу
    имя файла с картинкой
    изображение, готовое для работы
    """
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        return image
    except pygame.error as message:
        print('Не можем загрузить изображение:', name)
        raise SystemExit(message)



