from SETTINGS import GAMEBOARD
from random import randrange


class Ghost():
    """"Создаем конструктор класса Ghost"""

    def __init__(self, row, col, color, changeFeetCount):
        self.row = row
        self.col = col
        self.attacked = False
        self.color = color
        self.dir = randrange(4)
        self.dead = False
        self.changeFeetCount = changeFeetCount
        self.changeFeetDelay = 5
        self.target = [-1, -1]
        self.ghostSpeed = 0.25
        self.lastLoc = [-1, -1]
        self.attackedTimer = 240
        self.attackedCount = 0
        self.deathTimer = 120
        self.deathCount = 0

    """Метод для обновления положения Призрака в пространстве"""

    def move(self):
        self.lastLoc = [self.row, self.col]
        if self.dir == 0:
            self.row -= self.ghostSpeed
        elif self.dir == 1:
            self.col += self.ghostSpeed
        elif self.dir == 2:
            self.row += self.ghostSpeed
        elif self.dir == 3:
            self.col -= self.ghostSpeed

        # На случай если они пойдут через средний туннель
        self.col = self.col % len(GAMEBOARD[0])
        if self.col < 0:
            self.col = len(GAMEBOARD[0]) - 0.5

    def isValidTwo(self, cRow, cCol, dist, visited):
        if cRow < 3 or cRow >= len(GAMEBOARD) - 5 or cCol < 0 or cCol >= len(GAMEBOARD[0]) or GAMEBOARD[cRow][
            cCol] == 3:
            return False
        elif visited[cRow][cCol] <= dist:
            return False
        return True

    """"Установление атаки"""

    def setAttacked(self, isAttacked):
        self.attacked = isAttacked

    """"Атакован"""

    def isAttacked(self):
        return self.attacked

    """"Если съеден пакманом, то умер"""

    def setDead(self, isDead):
        self.dead = isDead

    """"Проверка на смерть"""

    def isDead(self):
        return self.dead
