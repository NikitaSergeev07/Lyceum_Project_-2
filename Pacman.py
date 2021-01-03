import pygame
import numpy
import math
from main import canMove
import random
import os
from SETTINGS import BOARDPATH, ELEMENTPATH, TEXTPATH, DATAPATH, MUSICPATH, MUSICPLAYING, DEFAULTCOLOR, SPRITERATIO, \
    square, SPRITEOFFSET, WIDTH, HEIGHT, SCREEN
from main import game


class Pacman():
    """"Создаем конструктор класса Pacman"""

    def __init__(self, row, col):
        # Описываем основые характеристики Пакмана
        self.row = row
        self.col = col
        self.mouthOpen = False
        self.pacSpeed = 0.25
        self.mouthChangeDelay = 5
        self.mouthChangeCount = 0
        self.dir = 0  # Положение по компасу: 0 - Север, 1 - Восток, 2 - Юг, 3 - Запад
        self.newDir = 0

    """Метод для обновления положения Пакмана в пространстве"""

    def update(self):
        # Вначале рассматриваем новое положение по компасу, если оно имеется
        if self.newDir == 0:
            if canMove(math.floor(self.row - self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row -= self.pacSpeed
                self.dir = self.newDir
                return
        elif self.newDir == 1:
            if canMove(self.row, math.ceil(self.col + self.pacSpeed)) and self.row % 1.0 == 0:
                self.col += self.pacSpeed
                self.dir = self.newDir
                return
        elif self.newDir == 2:
            if canMove(math.ceil(self.row + self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row += self.pacSpeed
                self.dir = self.newDir
                return
        elif self.newDir == 3:
            if canMove(self.row, math.floor(self.col - self.pacSpeed)) and self.row % 1.0 == 0:
                self.col -= self.pacSpeed
                self.dir = self.newDir
                return

        # Если его нет, рассматриваем старое положение по компасу
        if self.dir == 0:
            if canMove(math.floor(self.row - self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row -= self.pacSpeed
        elif self.dir == 1:
            if canMove(self.row, math.ceil(self.col + self.pacSpeed)) and self.row % 1.0 == 0:
                self.col += self.pacSpeed
        elif self.dir == 2:
            if canMove(math.ceil(self.row + self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row += self.pacSpeed
        elif self.dir == 3:
            if canMove(self.row, math.floor(self.col - self.pacSpeed)) and self.row % 1.0 == 0:
                self.col -= self.pacSpeed

        """"Метод, рисующий Пакмана, основываясь на его положении в текущий момент"""

    def draw(self):
        if not game.started:
            pacmanImage = pygame.image.load(ELEMENTPATH + "tile112.png")
            pacmanImage = pygame.transform.scale(pacmanImage, (int(square * SPRITERATIO), int(square * SPRITERATIO)))
            SCREEN.blit(pacmanImage,
                        (self.col * square + SPRITEOFFSET, self.row * square + SPRITEOFFSET, square, square))
            return

        if self.mouthChangeCount == self.mouthChangeDelay:
            self.mouthChangeCount = 0
            self.mouthOpen = not self.mouthOpen
        self.mouthChangeCount += 1
        # /
        if self.dir == 0:
            if self.mouthOpen:
                pacmanImage = pygame.image.load(ELEMENTPATH + "tile049.png")
            else:
                pacmanImage = pygame.image.load(ELEMENTPATH + "tile051.png")
        elif self.dir == 1:
            if self.mouthOpen:
                pacmanImage = pygame.image.load(ELEMENTPATH + "tile052.png")
            else:
                pacmanImage = pygame.image.load(ELEMENTPATH + "tile054.png")
        elif self.dir == 2:
            if self.mouthOpen:
                pacmanImage = pygame.image.load(ELEMENTPATH + "tile053.png")
            else:
                pacmanImage = pygame.image.load(ELEMENTPATH + "tile055.png")
        elif self.dir == 3:
            if self.mouthOpen:
                pacmanImage = pygame.image.load(ELEMENTPATH + "tile048.png")
            else:
                pacmanImage = pygame.image.load(ELEMENTPATH + "tile050.png")

        pacmanImage = pygame.transform.scale(pacmanImage, (int(square * SPRITERATIO), int(square * SPRITERATIO)))
        SCREEN.blit(pacmanImage,
                    (self.col * square + SPRITEOFFSET, self.row * square + SPRITEOFFSET, square, square))
