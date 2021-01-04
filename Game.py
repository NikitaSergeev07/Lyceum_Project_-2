from Ghost import Ghost
from SETTINGS import DATAPATH, GAMEBOARD
from Pacman import Pacman
from random import randrange
import random


class Game():
    """"Создаем конструктор класса Game"""

    def __init__(self, level, score):
        self.paused = True
        self.ghostUpdateDelay = 1
        self.ghostUpdateCount = 0
        self.pacmanUpdateDelay = 1
        self.pacmanUpdateCount = 0
        self.tictakChangeDelay = 10
        self.tictakChangeCount = 0
        self.ghostsAttacked = False
        self.highScore = self.getHighScore()
        self.score = score
        self.level = level
        self.lives = 3
        self.ghosts = [Ghost(14.0, 13.5, "red", 0), Ghost(17.0, 11.5, "blue", 1), Ghost(17.0, 13.5, "pink", 2),
                       Ghost(17.0, 15.5, "orange", 3)]
        self.pacman = Pacman(26.0, 13.5)  # Центр Второго последнего ряда
        self.total = self.getCount()
        self.ghostScore = 200
        self.levels = [[350, 250], [150, 450], [150, 450], [0, 600]]
        random.shuffle(self.levels)
        # Индексы уровней и прогресс уровней
        self.ghostStates = [[1, 0], [0, 0], [1, 0], [0, 0]]
        index = 0
        for state in self.ghostStates:
            state[0] = randrange(2)
            state[1] = randrange(self.levels[index][state[0]] + 1)
            index += 1
        self.collected = 0
        self.started = False
        self.gameOver = False
        self.gameOverCounter = 0
        self.points = []
        self.pointsTimer = 10
        # Время спавна ягоды, время пропадания ягоды, съеденная ягода
        self.berryState = [200, 400, False]
        self.berryLocation = [20.0, 13.5]
        self.berries = ["tile080.png", "tile081.png", "tile082.png", "tile083.png", "tile084.png", "tile085.png",
                        "tile086.png", "tile087.png"]
        self.berriesCollected = []
        self.levelTimer = 0
        self.berryScore = 100
        self.lockedInTimer = 100
        self.lockedIn = True
        self.extraLifeGiven = False
        self.musicPlaying = 0

    """"Метод для обновления рекорда"""

    def getHighScore(self):
        file = open(DATAPATH + "HighScore.txt", "r")
        highScore = int(file.read())
        file.close()
        return highScore

    """"Метод для получения счета"""

    def getCount(self):
        total = 0
        for i in range(3, len(GAMEBOARD) - 2):
            for j in range(len(GAMEBOARD[0])):
                if GAMEBOARD[i][j] == 2 or GAMEBOARD[i][j] == 5 or GAMEBOARD[i][j] == 6:
                    total += 1
        return total
