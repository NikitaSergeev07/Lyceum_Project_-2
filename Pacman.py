import pygame
import math
import random
import os
from SETTINGS import BOARDPATH, ELEMENTPATH, TEXTPATH, DATAPATH, MUSICPATH, MUSICPLAYING, DEFAULTCOLOR


class Pacman:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mouthOpen = False
        self.pacSpeed = 0.25
        self.mouthChangeDelay = 5
        self.mouthChangeCount = 0
        self.dir = 0
        self.newDir = 0
