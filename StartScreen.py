import pygame
from load_image import load_image
from settings_for_startscreen import HEIGHT, WIDTH, FULLNAME, INTRO, all_sprites, screen


class StartScreen:

    # Класс, отвечающий за вывод на экран стартового интерфейса

    def __init__(self):
        # Загрузка изображения названия игры и расположение на экране
        image = load_image('start_screen.png')
        sprite = pygame.sprite.Sprite()
        sprite.image = image
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = (WIDTH - 115) - image.get_width()
        sprite.rect.y = 0
        all_sprites.add(sprite)

    def print_text(self):
        # Вывод текста стартового окна
        for i in range(len(INTRO)):
            if INTRO[i][1] == 0:
                color = pygame.Color("white")
            else:
                color = pygame.Color("yellow")
            font = pygame.font.Font(FULLNAME, 30)
            text = font.render(INTRO[i][0], 1, (color))
            start_x = (WIDTH + 80) // 2 - text.get_width() // 2
            start_y = HEIGHT // 2 - text.get_height() // 2 - 50
            text_x = start_x
            text_y = start_y + i * 60
            screen.blit(text, (text_x, text_y))
