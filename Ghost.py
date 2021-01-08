import pygame
from load_image import load_image
from SETTINGS import HEIGHT, WIDTH, all_ghosts, GHOSTS, FULLNAME


class Ghost(pygame.sprite.Sprite):
    """
    Класс призраков в стартовом меню
    """

    def __init__(self, group, ghost_name):
        super().__init__(group)
        file_name = ghost_name[0]
        text = ghost_name[1]
        self.group = group
        image = load_image(file_name)
        # Скорость призрака
        self.v = 5
        self.moving = True
        self.show_name = False
        self.is_moving = True
        self.made_stop = False
        self.size = image.get_width()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = - 600
        self.rect.y = HEIGHT // 2 - 180

        # Вывод имен призраков
        font = pygame.font.Font(FULLNAME, 30)
        self.text = font.render(text, 1, (ghost_name[2]))
        self.start_x = WIDTH // 2 - self.text.get_width() // 2
        self.start_y = HEIGHT // 2 - 180

    def move(self):
        """
        Движение призрака по экрану
        :return: Перемещение призрака, его остановка в центре экрана,
        установка таймера для изображения имени призрака
        """
        if self.is_moving and self.moving:
            self.rect.x += self.v
        if not self.made_stop:
            if self.rect.x >= WIDTH // 2 + self.text.get_width() // 2 + 10:
                self.show_name = True
                self.is_moving = False
                self.made_stop = True

        if self.rect.x >= WIDTH + self.size:
            self.is_moving = False
            self.stop(1)

    def stop(self, pos=0):
        """
        Остановка привидений
        :param pos: отвечает за удаление спрайта призрака
        после выхода за пределы экрана
        :return: Остановка прдыдущего призрака и создание нового
        """
        global ghost_on_screen
        if pos == 1 and self.moving:
            self.moving = False
            self.kill()
            ghost_on_screen += 1
            if ghost_on_screen == 4:
                ghost_on_screen = 0
            Ghost(all_ghosts, GHOSTS[ghost_on_screen])
            Ghost.moving = True
            Ghost.is_moving = True
            Ghost.made_stop = False

    def continue_moving(self):
        """
        Продолжение движения
        :return:
        """
        if self.moving:
            self.show_name = False
            self.is_moving = True
