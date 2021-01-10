import pygame
import math
from random import randrange
import random
import copy
import os
from settings_for_startscreen import screen, all_sprites, all_ghosts, mouse_on_screen
from StartScreen import StartScreen
from load_image import load_image


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


def show_start_screen(self):
    # Отрисовка всех элементов стартового интерфейса

    global mouse_on_screen
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    StartScreen.print_text(start)
    for ghost in all_ghosts:
        ghost.move()
        if ghost.show_name == 1:
            screen.blit(ghost.text, (ghost.start_x, ghost.start_y))
    all_ghosts.update()
    all_ghosts.draw(screen)


running = True
onLaunchScreen = True
show_start_screen(True)
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            game.recordHighScore()
        elif event.type == pygame.KEYDOWN:
            game.paused = False
            game.started = True
            if event.key == pygame.K_w:
                if not onLaunchScreen:
                    game.pacman.newDir = 0
            elif event.key == pygame.K_d:
                if not onLaunchScreen:
                    game.pacman.newDir = 1
            elif event.key == pygame.K_s:
                if not onLaunchScreen:
                    game.pacman.newDir = 2
            elif event.key == pygame.K_a:
                if not onLaunchScreen:
                    game.pacman.newDir = 3
            elif event.key == pygame.K_SPACE:
                if onLaunchScreen:
                    onLaunchScreen = False
                    game.paused = True
                    game.started = False
                    game.render()
                    pygame.mixer.music.load(MusicPath + "pacman_beginning.wav")
                    pygame.mixer.music.play()
                    musicPlaying = 1
            elif event.key == pygame.K_q:
                game.paused = True
                game.recordHighScore()
            elif event.key == pygame.K_ESCAPE:
                running = False
                game.recordHighScore()
            elif event.key == pygame.K_q:
                game.paused = True

    if not onLaunchScreen:
        game.update()
