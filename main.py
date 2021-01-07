import os
import sys
import pygame
from random import randint, choice
from SETTINGS import FPS, WIDTH, HEIGHT, CHANGE, CONTINUEMOVE, GHOSTS, GHOSTSGAME, INTRO, FULLNAME, screen, all_sprites, \
    all_ghosts, all_points, all_maps, all_rects, ghost_sprites, pacman_kill, pacman_sprite, clock, map_on_screen, \
    map_on_screen_num, f1, f2, f3, f4, f5, f6, color_back, ghost_on_screen, running, mouse_on_screen, song, music_on, \
    image_life, game_over_image, winn_level, start, score, start_game, stop, stop_game, lives, iteration_kill, \
    iterations, kill_num, points
from Ghost import Ghost
from GhostInGame import GhostPlay

pygame.init()
pygame.display.set_caption('Pacman')
pygame.mouse.set_visible(False)


def load_image(name):
    """
    Загрузка картинки из файла в программу
    :param name: имя файла с картинкой
    :return: изображение, готовое для работы
    """
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        return image
    except pygame.error as message:
        print('Не можем загрузить изображение:', name)
        raise SystemExit(message)


def terminate():
    """
    Выход из игры
    :return:
    """
    pygame.quit()
    sys.exit()


def start_screen_on():
    """
    Стартовый интерфейс
    :return:
    """
    global mouse_on_screen, music_on
    while True:
        show_start_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            # Включение/выключение музыки
            if pygame.key.get_pressed()[pygame.K_e]:
                if music_on:
                    pygame.mixer.music.pause()
                    music_on = False
                else:
                    pygame.mixer.music.unpause()
                    music_on = True

            elif event.type == pygame.MOUSEMOTION:
                change_text_start(event.pos)
                if pygame.mouse.get_focused():
                    change_place(event.pos)
                    mouse_on_screen = event.pos
            elif event.type == CONTINUEMOVE:
                for ghost in all_ghosts:
                    ghost.continue_moving()
                pygame.time.set_timer(CONTINUEMOVE, 0)
            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    event.button == 1:
                # Кнопка "Начать игру"
                if f1:
                    return
                # Кнопка "Управление"
                elif f2:
                    controls_screen()
                    return
                # Кнопка "Об игре"
                elif f3:
                    about()
                # Кнопка "Таблица рекордов"
                elif f4:
                    record_menu()
                # Кнопка "Выход"
                elif f5:
                    terminate()
        pygame.display.flip()


def before_game(map=1):
    """
    Загрузка карты и расстановка ее элементов перед игрой
    :param map: карта на экране
    :return:
    """
    global stop
    screen.fill(pygame.Color("black"))
    all_maps.draw(screen)
    all_maps.update()
    stop = False
    draw_back(['Чтобы начать игру, нажмите пробел'], 'start')
    if map == 2:
        for i in range(8):
            GhostPlay(i)
    elif map == 1:
        for i in range(4):
            GhostPlay(i)
    elif map == 3:
        for i in range(2):
            GhostPlay(i)
    pacman = Pacman(pacman_sprite, load_image("moving_pacman.png"), 2, 1, 22, 24)
    if map != 3:
        for i in range(lives):
            screen.blit(image_life, (100 + 43 * i, 685))
        draw_back(['Баллы', score], 'points')
    else:
        for i in range(lives):
            screen.blit(image_life, (315 + 43 * i, 540))
        draw_back(['Баллы', score], 'points_3')


def show_start_screen():
    """
    Отрисовка всех элементов стартового интерфейса
    :return:
    """
    global mouse_on_screen
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    StartScreen.print_text(start)
    for ghost in all_ghosts:
        ghost.move()
        if ghost.show_name == 1:
            screen.blit(ghost.text, (ghost.start_x, ghost.start_y))
    if mouse_on_screen and pygame.mouse.get_focused():
        change_place(mouse_on_screen)
    all_ghosts.update()
    all_ghosts.draw(screen)


def about():
    """
    Обработка действий с окном описания игры
    :return:
    """
    global mouse_on_screen, f6, color_back, music_on
    f6 = False
    color_back = 0
    while True:
        show_about()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            # Включение / выключение звука
            elif pygame.key.get_pressed()[pygame.K_e]:
                if music_on:
                    pygame.mixer.music.pause()
                    music_on = False
                else:
                    pygame.mixer.music.unpause()
                    music_on = True
            elif event.type == pygame.MOUSEMOTION:
                show_about()
                # Изменение цвета кнопки "Назад"
                x, y = event.pos
                if 563 <= x <= 563 + 75 and 597 <= y <= 597 + 37 and not f6:
                    color_back = 1
                    f6 = True
                elif f6 and not (563 <= x <= 563 + 75 and 597 <= y <= 597 + 37):
                    color_back = 0
                    f6 = False
                if pygame.mouse.get_focused():
                    show_about()
                    change_place(event.pos)
                    mouse_on_screen = event.pos
            # Обработка остановки призраков
            elif event.type == CONTINUEMOVE:
                for ghost in all_ghosts:
                    ghost.continue_moving()
                pygame.time.set_timer(CONTINUEMOVE, 0)
            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    event.button == 1:
                # Обработка выхода в главное меню
                if f6:
                    start_screen_on()
                    return
        pygame.display.flip()


def controls_screen():
    """
    Обработка действий с окном управления
    :return:
    """
    global mouse_on_screen, f6, color_back, music_on
    while True:
        show_controls()
        for event in pygame.event.get():
            # Выход из игры
            if event.type == pygame.QUIT:
                terminate()
            elif pygame.key.get_pressed()[pygame.K_e]:
                if music_on:
                    pygame.mixer.music.pause()
                    music_on = False
                else:
                    pygame.mixer.music.unpause()
                    music_on = True
            elif event.type == pygame.MOUSEMOTION:
                show_controls()
                # Изменение цвета кнопки "Назад" при наведении
                x, y = event.pos
                if 538 <= x <= 538 + 125 and 525 <= y <= 525 + 61 and not f6:
                    color_back = 1
                    f6 = True
                elif f6 and not (538 <= x <= 538 + 125 and 525 <= y <= 525 + 61):
                    color_back = 0
                    f6 = False
                # Обработка движения курсора
                if pygame.mouse.get_focused():
                    show_controls()
                    change_place(event.pos)
                    mouse_on_screen = event.pos
            elif event.type == CONTINUEMOVE:
                for ghost in all_ghosts:
                    ghost.continue_moving()
                pygame.time.set_timer(CONTINUEMOVE, 0)
            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    event.button == 1:
                # Возвращение в главный экран
                if f6:
                    start_screen_on()
                    return
        pygame.display.flip()


def show_controls():
    """
    Вывод экрана с описанием упраления
    :return:
    """
    global mouse_on_screen, color_back
    screen.fill((0, 0, 0))
    # Текст на экране
    text_controls = ["Управление",
                     "Стрелки для управления пакмэном",
                     "Esc: Пауза/Продолжить",
                     "E: Включить/Выключить звук",
                     "Назад"]

    # Запуск движения призраков
    for ghost in all_ghosts:
        ghost.move()
        if ghost.show_name == 1:
            screen.blit(ghost.text, (ghost.start_x, ghost.start_y))
    all_ghosts.update()
    all_ghosts.draw(screen)

    # Изображение курсора на экране
    if mouse_on_screen and pygame.mouse.get_focused():
        change_place(mouse_on_screen)

    # Вывод текст на экран
    draw_back(text_controls, 'controls')
    all_sprites.draw(screen)


def show_menu(button):
    """
    Отрисовка меню паузы
    :param button: кнопка, которая выбрана нажатием клавиатуры
    :return:
    """
    ghost_sprites.draw(screen)
    pygame.draw.rect(screen, (0, 175, 240), ([WIDTH // 2 - 225, HEIGHT // 2 - 100], [450, 150]), 10)
    pygame.draw.rect(screen, pygame.Color("black"), ([WIDTH // 2 - 225, HEIGHT // 2 - 100], [450, 150]))
    # Текст на экране
    text_menu = ["Вернуться в игру",
                 "Начать игру заново"]

    # Вывод текста на экран
    if button == 1:
        draw_back(text_menu, 'menu_1')
    elif button == 2:
        draw_back(text_menu, 'menu_2')


def pause_menu():
    """
    Меню во время паузы (обработка)
    :return:
    """
    global start_game, start, stop_game, \
        lives, score, map_on_screen_num, \
        music_on, stop
    button_1 = True
    show_menu(1)
    while True:
        for event in pygame.event.get():
            # Выход из игры
            if event.type == pygame.QUIT:
                terminate()
            # Включение / выключение звука
            if pygame.key.get_pressed()[pygame.K_e]:
                if music_on:
                    pygame.mixer.music.pause()
                    music_on = False
                else:
                    pygame.mixer.music.unpause()
                    music_on = True
            if pygame.key.get_pressed()[pygame.K_UP]:
                show_menu(1)
                button_1 = True
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                show_menu(2)
                button_1 = False
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                if button_1:
                    start_game = True
                    return
                else:
                    for pm in pacman_sprite:
                        pm.kill()
                    for rect in all_rects:
                        rect.kill()
                    for ghost in ghost_sprites:
                        ghost.kill()
                    lives = 3
                    score = 0
                    stop = False
                    map_on_screen_num = 1
                    before_game(map_on_screen_num)
                    return
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                start_game = True
                return
        pygame.display.flip()


def show_about():
    """
    Вывод экрана с описанием игры
    :return:
    """
    global mouse_on_screen, color_back
    screen.fill((0, 0, 0))

    # Текст на экране
    text_about = ["Пакман - аркадная видеоигра, вышедшая в 1980 году.",
                  "Задача игрока — управляя Пакманом, съесть все точки в лабиринте, ",
                  "избегая встречи с привидениями.",
                  "Авторы игры: Никита и Александр",
                  "Яндекс Лицей 2021",
                  "Назад"]

    # Запуск движения призраков
    for ghost in all_ghosts:
        ghost.move()
        if ghost.show_name == 1:
            screen.blit(ghost.text, (ghost.start_x, ghost.start_y))
    all_ghosts.update()
    all_ghosts.draw(screen)

    # Обработка движения курсора
    if mouse_on_screen and pygame.mouse.get_focused():
        change_place(mouse_on_screen)
    # Вывод текста на экран
    draw_back(text_about, 'about')
    all_sprites.draw(screen)


def add_table(name):
    """
    Добавление нового рекорда в таблицу
    :param name: имя игрока
    :return:
    """
    # Добавление имени в файл с рекордами
    file_path = os.path.join('data', 'records.txt')
    file_records = open(file_path, mode='a')
    file_records.write(str(score) + ' ' + name + '\n')
    file_records.close()

    # Сортировка файла с рекордами
    file_records = open(file_path, mode='r')
    data = file_records.readlines()
    file_records.close()

    data.sort(key=lambda a: int(a.split()[0]),
              reverse=True)

    # Запись отсортированного файла с рекордами
    file_records = open(file_path, mode='w')
    for line in data:
        file_records.write(line)
    file_records.close()


def record_menu(end=False):
    """
    Меню рекордов
    :param end: выбор меню в начале или в конце игры
    :return:
    """
    global mouse_on_screen, mouse_on_screen, music_on
    color_back = pygame.Color("white")

    file_path = os.path.join('data', 'records.txt')
    file_records = open(file_path, mode='r')
    data = file_records.readlines()
    file_records.close()

    while True:
        if end:
            show_record_menu(data, color_back, True)
        else:
            show_record_menu(data, color_back)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            elif pygame.key.get_pressed()[pygame.K_e]:
                if music_on:
                    pygame.mixer.music.pause()
                    music_on = False
                else:
                    pygame.mixer.music.unpause()
                    music_on = True
            elif event.type == CONTINUEMOVE:
                for ghost in all_ghosts:
                    ghost.continue_moving()
                pygame.time.set_timer(CONTINUEMOVE, 0)

            elif event.type == pygame.MOUSEMOTION:
                if 534 <= event.pos[0] <= 643 and 596 <= event.pos[1] <= 637:
                    color_back = pygame.Color("yellow")
                else:
                    color_back = pygame.Color("white")
                if end:
                    show_record_menu(data, color_back, True)
                else:
                    show_record_menu(data, color_back)
                if pygame.mouse.get_focused():
                    change_place(event.pos)
                    mouse_on_screen = event.pos

            elif event.type == pygame.MOUSEBUTTONDOWN and \
                    event.button == 1:
                if 534 <= event.pos[0] <= 643 and 596 <= event.pos[1] <= 637:
                    return
        pygame.display.flip()


Ghost(all_ghosts, GHOSTS[0])
pygame.mixer.init()
pygame.mixer.music.load(song)
pygame.mixer.music.play(100)
pygame.mixer.music.set_volume(0.3)
start_screen_on()
before_game(map_on_screen_num)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        # Начало игры
        elif pygame.key.get_pressed()[pygame.K_SPACE] and \
                not start_game and not stop:

            screen.fill(pygame.Color("black"))
            all_maps.draw(screen)
            start_game = True
        # Включение / выключение звука
        elif pygame.key.get_pressed()[pygame.K_e]:
            if music_on:
                pygame.mixer.music.pause()
                music_on = False
            else:
                pygame.mixer.music.unpause()
                music_on = True

        # Изменения направления призраков
        elif event.type == CHANGE:
            for ghost in ghost_sprites:
                ghost.change()
            pygame.time.set_timer(CHANGE, 3500)
        elif pygame.key.get_pressed()[pygame.K_ESCAPE] and start_game:
            start_game = False
            pause_menu()

        # Движение пакмана
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and start_game:
            for hero in pacman_sprite:
                hero.move("right")
        elif pygame.key.get_pressed()[pygame.K_LEFT] and start_game:
            for hero in pacman_sprite:
                hero.move("left")
        elif pygame.key.get_pressed()[pygame.K_UP] and start_game:
            for hero in pacman_sprite:
                hero.move("up")
        elif pygame.key.get_pressed()[pygame.K_DOWN] and start_game:
            for hero in pacman_sprite:
                hero.move("down")

    # Игровой процесс
    if start_game:
        screen.fill(pygame.Color("black"))
        if map_on_screen_num != 3:
            draw_back(['Баллы', score], 'points')
        else:
            draw_back(['Баллы', score], 'points_3')
        # Отрисовка всех групп спрайтов
        all_points.draw(screen)
        all_rects.update()
        all_rects.draw(screen)
        all_maps.draw(screen)
        pacman_sprite.draw(screen)
        for pacman in pacman_sprite:
            pacman.move()

        # Отрисовка оставшихся жизней
        if map_on_screen_num != 3:
            for i in range(lives):
                screen.blit(image_life, (100 + 43 * i, 685))
        else:
            for i in range(lives):
                screen.blit(image_life, (315 + 43 * i, 540))
        if iterations == 10:
            pacman_sprite.update()
            iterations = 0
        for ghost in ghost_sprites:
            ghost.move()
        ghost_sprites.update()
        ghost_sprites.draw(screen)

        iterations += 1
        # Переключение на новый уровень
        if (score == 1840 and map_on_screen_num == 1) or \
                (score == 3680 and map_on_screen_num == 2):
            start_game = False
            winn_lvl()
        # Выигрыш
        if score == 4170 and map_on_screen_num == 3:
            start_game = False
            winn_game()

        if stop_game:
            lives -= 1
            start_game = False
            for pm in pacman_sprite:
                x, y = pm.rect.x, pm.rect.y
            kill_pacman = Pacman(pacman_kill, load_image("killing_pacman.png"),
                                 11, 1, 32, 32, x, y)

    # Остановка игрового процесса
    if stop_game:
        stop = True
        screen.fill(pygame.Color("black"))
        all_points.draw(screen)
        all_rects.draw(screen)
        all_maps.draw(screen)
        ghost_sprites.draw(screen)
        pacman_kill.draw(screen)
        # Анимация смерти пакмана
        iteration_kill += 1
        if iteration_kill == 10:
            pacman_kill.update()
            iteration_kill = 0
            kill_num += 1
        if kill_num == 11:
            kill_num = 0
            stop_game = False
            for ghost in ghost_sprites:
                ghost.kill()
            for pm in pacman_sprite:
                pm.kill()
            for pm in pacman_kill:
                pm.kill()
            if lives == -1:
                # Запись рекорда игрока и завершение игры
                add_table(new_record())
                game_over()
            else:
                before_game(map_on_screen_num)
                stop = False
    clock.tick(FPS)
    pygame.display.flip()
