import pygame
import os

WIDTH = 690
HEIGHT = 500

GHOSTS = [('Inky.png', 'INKY', (26, 175, 230)),
          ('Blinky.png', 'Blinky', (231, 0, 10)),
          ('Pinky.png', 'Pinky', (242, 159, 183)),
          ('Clyde.png', 'Clyde', (231, 141, 0))]

INTRO = [["Привет, добро пожаловать в игру PACMAN", 0],
         ["Пакман - аркадная видеоигра, вышедшая в 1980 году.", 0],
         ["Задача игрока — управляя Пакманом, ", 0],
         ["съесть все точки в лабиринте,", 0],
         ["избегая встречи с привидениями.", 0],
         ["Управление", 0],
         ["W - Вверх, S - Вниз, A - Влево, D -Вправо", 0],
         ["Для начала игры нажми на SPACE", 0],
         ["Q - пауза, SPACE - продолжить, Esc - выход", 0]]

# Шрифт надписей в игре
FULLNAME = os.path.join('data', 'Firenight-Regular.otf')

# Экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(pygame.Color("black"))

# Группы спрайтов для стартового экрана
all_sprites = pygame.sprite.Group()
all_ghosts = pygame.sprite.Group()

mouse_on_screen = None
