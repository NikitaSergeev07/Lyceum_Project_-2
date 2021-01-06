import pygame
import os
from Map import Map
from main import load_image
from StartScreen import StartScreen
from Points import Points

FPS = 30
WIDTH = 1200
HEIGHT = 750

# Таймеры
CHANGE = 30
CONTINUEMOVE = 31

GHOSTS = [('Inky.png', 'INKY', (26, 175, 230)),
          ('Blinky.png', 'Blinky', (231, 0, 10)),
          ('Pinky.png', 'Pinky', (242, 159, 183)),
          ('Clyde.png', 'Clyde', (231, 141, 0))]
GHOSTSGAME = [('blinky_up.png', 'blinky_down.png',
               'blinky_left.png', 'blinky_right.png'),
              ('pinky_up.png', 'pinky_down.png',
               'pinky_left.png', 'pinky_right.png'),
              ('clyde_up.png', 'clyde_down.png',
               'clyde_left.png', 'clyde_right.png'),
              ('inky_up.png', 'inky_down.png',
               'inky_left.png', 'inky_right.png')]
INTRO = [["Начать игру", 0],
         ["Управление", 0],
         ["Об игре", 0],
         ["Таблица рекордов", 0],
         ["Выход", 0]]

# Шрифт надписей в игре
FULLNAME = os.path.join('data', 'Firenight-Regular.otf')

# Экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(pygame.Color("black"))

# Группы спрайтов для стартового экрана
all_sprites = pygame.sprite.Group()
all_ghosts = pygame.sprite.Group()

# Группы спрайтов интерфейса карты
all_maps = pygame.sprite.Group()
all_points = pygame.sprite.Group()
all_rects = pygame.sprite.Group()

# Группы спрайтов-персонажей
ghost_sprites = pygame.sprite.Group()
pacman_kill = pygame.sprite.Group()
pacman_sprite = pygame.sprite.Group()

# Карта и часы
map_on_screen = Map("map.png")
clock = pygame.time.Clock()
map_on_screen_num = 1

# Начальные значения для главного меню
f1, f2, f3, f4, f5 = False, False, False, False, False
f6 = False
color_back = 0
ghost_on_screen = 0

# Основные флаги
running = True
mouse_on_screen = None

# Саундтрек игры
song = os.path.join('data', 'music.mp3')
music_on = True

# Загрузка изображений
image_life = load_image('pacman_lives.png')
game_over_image = load_image("game_over.png")
winn_level = load_image('winn_level.png')

# Начало игры
start = StartScreen()

# Для игры
score = 0
lives = 3
stop_game = False
start_game = False
stop = False
iteration_kill = 0
kill_num = 0
iterations = 0
points = Points()
