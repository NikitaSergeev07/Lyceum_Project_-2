from SETTINGS import BOARDPATH, ELEMENTPATH, TEXTPATH, DATAPATH, MUSICPATH, MUSICPLAYING, DEFAULTCOLOR, SPRITERATIO, \
    square, SPRITEOFFSET, WIDTH, HEIGHT, SCREEN
from Pacman import Pacman
from Ghost import Ghost

game = Game(1, 0)
ghostsafeArea = [15, 13]  # Мдесто, куда убегают призраки, когда на них нападают
ghostGate = [[15, 13], [15, 14]]


# Создаем функцию передвижения персонажей
def canMove(row, col):
    if col == -1 or col == len(GAMEBOARD[0]):
        return True
    if GAMEBOARD[int(row)][int(col)] != 3:
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


# Рисуем основные элементы игры
def displayLaunchScreen():
    # Рисуем Пакману название
    pacmanTitle = ["tile016.png", "tile000.png", "tile448.png", "tile012.png", "tile000.png", "tile013.png"]
    for i in range(len(pacmanTitle)):
        letter = pygame.image.load(TEXTPATH + pacmanTitle[i])
        letter = pygame.transform.scale(letter, (int(square * 4), int(square * 4)))
        screen.blit(letter, ((2 + 4 * i) * square, 2 * square, square, square))

    # Рисуем персонажей и их имена
    characterTitle = [
        # Персонаж
        "tile002.png", "tile007.png", "tile000.png", "tile018.png", "tile000.png", "tile002.png", "tile020.png",
        "tile004.png", "tile018.png",
        # /
        "tile015.png", "tile042.png", "tile015.png",
        # Имя
        "tile013.png", "tile008.png", "tile002.png", "tile010.png", "tile013.png", "tile000.png", "tile012.png",
        "tile004.png"
    ]
    for i in range(len(characterTitle)):
        letter = pygame.image.load(TEXTPATH + characterTitle[i])
        letter = pygame.transform.scale(letter, (int(square), int(square)))
        screen.blit(letter, ((4 + i) * square, 10 * square, square, square))

    # Рисуем персонажей и их имена
    characters = [
        # Красный призрак
        [
            "tile449.png", "tile015.png", "tile107.png", "tile015.png", "tile083.png", "tile071.png", "tile064.png",
            "tile067.png", "tile078.png", "tile087.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile108.png", "tile065.png", "tile075.png", "tile072.png", "tile077.png", "tile074.png", "tile089.png",
            "tile108.png"
        ],
        # Розовый призрак
        [
            "tile450.png", "tile015.png", "tile363.png", "tile015.png", "tile339.png", "tile336.png", "tile324.png",
            "tile324.png", "tile323.png", "tile345.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile364.png", "tile336.png", "tile328.png", "tile333.png", "tile330.png", "tile345.png", "tile364.png"
        ],
        # Голубой призрак
        [
            "tile452.png", "tile015.png", "tile363.png", "tile015.png", "tile193.png", "tile192.png", "tile211.png",
            "tile199.png", "tile197.png", "tile213.png", "tile203.png",
            "tile015.png", "tile015.png", "tile015.png",
            "tile236.png", "tile200.png", "tile205.png", "tile202.png", "tile217.png", "tile236.png"
        ],
        # Оранжевый призрак
        [
            "tile451.png", "tile015.png", "tile363.png", "tile015.png", "tile272.png", "tile270.png", "tile266.png",
            "tile260.png", "tile281.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile300.png", "tile258.png", "tile267.png", "tile281.png", "tile259.png", "tile260.png", "tile300.png"
        ]
    ]
    for i in range(len(characters)):
        for j in range(len(characters[i])):
            if j == 0:
                letter = pygame.image.load(TEXTPATH + characters[i][j])
                letter = pygame.transform.scale(letter, (int(square * SPRITERATIO), int(square * SPRITERATIO)))
                screen.blit(letter,
                            ((2 + j) * square - square // 2, (12 + 2 * i) * square - square // 3, square, square))
            else:
                letter = pygame.image.load(TEXTPATH + characters[i][j])
                letter = pygame.transform.scale(letter, (int(square), int(square)))
                screen.blit(letter, ((2 + j) * square, (12 + 2 * i) * square, square, square))
    # Рисуем пакмана и призраков
    event = ["tile449.png", "tile015.png", "tile452.png", "tile015.png", "tile015.png", "tile448.png", "tile453.png",
             "tile015.png", "tile015.png", "tile015.png", "tile453.png"]
    for i in range(len(event)):
        character = pygame.image.load(TEXTPATH + event[i])
        character = pygame.transform.scale(character, (int(square * 2), int(square * 2)))
        screen.blit(character, ((4 + i * 2) * square, 24 * square, square, square))
    # Рисуем стены
    wall = ["tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png",
            "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png",
            "tile454.png"]
    for i in range(len(wall)):
        platform = pygame.image.load(TEXTPATH + wall[i])
        platform = pygame.transform.scale(platform, (int(square * 2), int(square * 2)))
        screen.blit(platform, ((i * 2) * square, 26 * square, square, square))
    # Рисуем дорогу
    credit = ["tile003.png", "tile004.png", "tile022.png", "tile008.png", "tile013.png", "tile015.png", "tile011.png",
              "tile004.png", "tile000.png", "tile012.png", "tile025.png", "tile015.png", "tile418.png", "tile416.png",
              "tile418.png", "tile416.png"]
    for i in range(len(credit)):
        letter = pygame.image.load(TEXTPATH + credit[i])
        letter = pygame.transform.scale(letter, (int(square), int(square)))
        screen.blit(letter, ((6 + i) * square, 30 * square, square, square))
    # Нажмите пробел, чтобы играть(инструкции)
    instructions = ["tile016.png", "tile018.png", "tile004.png", "tile019.png", "tile019.png", "tile015.png",
                    "tile019.png", "tile016.png", "tile000.png", "tile002.png", "tile004.png", "tile015.png",
                    "tile020.png", "tile014.png", "tile015.png", "tile016.png", "tile011.png", "tile000.png",
                    "tile025.png"]
    for i in range(len(instructions)):
        letter = pygame.image.load(TEXTPATH + instructions[i])
        letter = pygame.transform.scale(letter, (int(square), int(square)))
        screen.blit(letter, ((4.5 + i) * square, 35 * square - 10, square, square))

    pygame.display.update()


running = True
onLaunchScreen = True
displayLaunchScreen()


# Создаем функцию для того, чтобы ставить игру на паузу
def pause(time):
    cur = 0
    while not cur == time:
        cur += 1


# Основной цикл игры
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
                    pygame.mixer.music.load(MUSICPATH + "pacman_beginning.wav")
                    pygame.mixer.music.play()
                    musicPlaying = 1
            elif event.key == pygame.K_q:
                running = False
                game.recordHighScore()

    if not onLaunchScreen:
        game.update()
