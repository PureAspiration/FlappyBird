import pygame
import random

gravity = 0.4
highScore = 0

pygame.init()
width, height = 288, 512
backgroundColor = 255, 0, 0

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
icon = pygame.image.load("assets/icon.png").convert()
icon = pygame.transform.scale(icon, (35, 35))
pygame.display.set_icon(icon)
pygame.display.set_caption("Flappy Bird")

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)
transparent = (0, 0, 0, 0)


def gameoverScreen(pipes, birdPosX, birdPosY, floor, score):
    background = pygame.image.load("assets/background-day.png").convert()
    backgroundRect = background.get_rect()
    backgroundRect.topleft = (0, 0)
    screen.blit(background, backgroundRect)

    for i in range(len(pipes)):
        pipeTop = pygame.image.load("assets/pipe-green.png").convert()
        pipeTop = pygame.transform.rotate(pipeTop, 180)
        pipeRect = pipeTop.get_rect()
        pipeRect.midbottom = (pipes[i][0], pipes[i][1] - 50)
        screen.blit(pipeTop, pipeRect)

        pipeBottom = pygame.image.load("assets/pipe-green.png").convert()
        pipeRect = pipeBottom.get_rect()
        pipeRect.midtop = (pipes[i][0], pipes[i][1] + 50)
        screen.blit(pipeBottom, pipeRect)

    bird = pygame.image.load("assets/yellowbird-upflap.png").convert()
    birdRect = bird.get_rect()
    birdRect.center = (birdPosX, birdPosY)
    screen.blit(bird, birdRect)

    base = pygame.image.load("assets/base.png").convert()
    baseRect = base.get_rect()
    baseRect.midright = (floor, 500)
    screen.blit(base, baseRect)
    base = pygame.image.load("assets/base.png").convert()
    baseRect = base.get_rect()
    baseRect.midleft = (floor, 500)
    screen.blit(base, baseRect)

    gameover = pygame.image.load("assets/gameover.png").convert_alpha()
    gameoverRect = gameover.get_rect()
    gameoverRect.center = (width / 2, 100)
    screen.blit(gameover, gameoverRect)

    scoreMenu = pygame.image.load("assets/scores.png").convert()
    scoreMenu = pygame.transform.scale(scoreMenu, (200, 200))
    scoreMenuRect = scoreMenu.get_rect()
    scoreMenuRect.center = (width / 2, height / 2)
    screen.blit(scoreMenu, scoreMenuRect)

    button = pygame.image.load("assets/button-ok.png").convert()
    button = pygame.transform.scale(button, (125, 41))
    buttonRect = button.get_rect()
    buttonRect.center = (width / 2, 400)
    screen.blit(button, buttonRect)

    global highScore
    if score > highScore:
        highScore = score
        print("New High Score!")
        scoreNew = pygame.image.load("assets/scores-new.png").convert()
        scoreNew = pygame.transform.scale(scoreNew, (55, 26))
        scoreNewRect = scoreNew.get_rect()
        scoreNewRect.center = (115, 268)
        screen.blit(scoreNew, scoreNewRect)
        print("New High Score!")

    for i in range(len(str(score))):
        scoreDigit = str(score)[len(str(score)) - i - 1]
        scoreNumber = pygame.image.load(f"assets/numbers/{scoreDigit}.png").convert_alpha()
        scoreNumberRect = scoreNumber.get_rect()
        scoreNumberRect.center = (195 - (i * 25), 230)
        screen.blit(scoreNumber, scoreNumberRect)

    for i in range(len(str(highScore))):
        highScoreDigit = str(highScore)[len(str(highScore)) - i - 1]
        scoreNumber = pygame.image.load(f"assets/numbers/{highScoreDigit}.png").convert_alpha()
        scoreNumberRect = scoreNumber.get_rect()
        scoreNumberRect.center = (195 - (i * 25), 305)
        screen.blit(scoreNumber, scoreNumberRect)

    pygame.display.update()


def game():
    background = pygame.image.load("assets/background-day.png").convert()
    backgroundRect = background.get_rect()
    backgroundRect.topleft = (0, 0)
    screen.blit(background, backgroundRect)

    startScreen = pygame.image.load("assets/message.png").convert_alpha()
    startScreenRect = startScreen.get_rect()
    startScreenRect.center = (width / 2, height / 2)
    screen.blit(startScreen, startScreenRect)

    birdPosX, birdPosY = 144, 304

    floor = 288

    while True:
        clock.tick(30)

        base = pygame.image.load("assets/base.png").convert()
        baseRect = base.get_rect()
        baseRect.midright = (floor, 500)
        screen.blit(base, baseRect)
        base = pygame.image.load("assets/base.png").convert()
        baseRect = base.get_rect()
        baseRect.midleft = (floor, 500)
        screen.blit(base, baseRect)

        floor -= 4

        if floor <= 0:
            floor = 288

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(f"{mouse[0]} {mouse[1]}")

                score = 0
                pixelsMoved = 0
                pipes = []
                birdJump = False
                birdJumpPixels = 0
                birdFallPixels = 0

                while True:
                    clock.tick(30)

                    screen.fill(black)

                    background = pygame.image.load("assets/background-day.png").convert()
                    backgroundRect = background.get_rect()
                    backgroundRect.topleft = (0, 0)
                    screen.blit(background, backgroundRect)

                    floor -= 4
                    if floor <= 0:
                        floor = 288

                    pixelsMoved += 4
                    if pixelsMoved >= 400 and (pixelsMoved / 200).is_integer():
                        pipeSpawn = random.randint(50, 400)

                        pipes.append([350, pipeSpawn])

                    for i in range(len(pipes)):
                        print(pipes)
                        print("------------------------")
                        pipes[i][0] -= 4

                        if pipes[i][0] <= -100:
                            pipes.pop(0)
                            break

                    for i in range(len(pipes)):
                        if pipes[i][0] == 142:
                            score += 1

                    for i in range(len(pipes)):
                        pipeTop = pygame.image.load("assets/pipe-green.png").convert()
                        pipeTop = pygame.transform.rotate(pipeTop, 180)
                        pipeRect = pipeTop.get_rect()
                        pipeRect.midbottom = (pipes[i][0], pipes[i][1] - 50)
                        screen.blit(pipeTop, pipeRect)

                        pipeBottom = pygame.image.load("assets/pipe-green.png").convert()
                        pipeRect = pipeBottom.get_rect()
                        pipeRect.midtop = (pipes[i][0], pipes[i][1] + 50)
                        screen.blit(pipeBottom, pipeRect)

                    while birdJump:
                        clock.tick(30)
                        birdJumpPixels -= 10
                        birdPosY -= 10

                        if birdJumpPixels <= -50:
                            birdJump = False
                        break

                    while not birdJump:
                        clock.tick(30)
                        birdFallPixels = birdFallPixels + gravity
                        birdPosY += birdFallPixels
                        break

                    bird = pygame.image.load("assets/yellowbird-upflap.png").convert()
                    birdRect = bird.get_rect()
                    birdRect.center = (birdPosX, birdPosY)
                    screen.blit(bird, birdRect)

                    base = pygame.image.load("assets/base.png").convert()
                    baseRect = base.get_rect()
                    baseRect.midright = (floor, 500)
                    screen.blit(base, baseRect)
                    base = pygame.image.load("assets/base.png").convert()
                    baseRect = base.get_rect()
                    baseRect.midleft = (floor, 500)
                    screen.blit(base, baseRect)

                    if len(str(score)) == 1:
                        scoreNumber = pygame.image.load(f"assets/numbers/{score}.png").convert_alpha()
                        scoreNumberRect = scoreNumber.get_rect()
                        scoreNumberRect.center = (width / 2, 100)
                        screen.blit(scoreNumber, scoreNumberRect)
                    elif len(str(score)) == 2:
                        scoreNumber = pygame.image.load(f"assets/numbers/{str(score)[0]}.png").convert_alpha()
                        scoreNumberRect = scoreNumber.get_rect()
                        scoreNumberRect.midright = (width / 2, 100)
                        screen.blit(scoreNumber, scoreNumberRect)
                        scoreNumber = pygame.image.load(f"assets/numbers/{str(score)[1]}.png").convert_alpha()
                        scoreNumberRect = scoreNumber.get_rect()
                        scoreNumberRect.midleft = (width / 2, 100)
                        screen.blit(scoreNumber, scoreNumberRect)
                    elif len(str(score)) == 3:
                        scoreNumber = pygame.image.load(f"assets/numbers/{str(score)[0]}.png").convert_alpha()
                        scoreNumberRect = scoreNumber.get_rect()
                        scoreNumberRect.midright = (width / 2 - 12, 100)
                        screen.blit(scoreNumber, scoreNumberRect)
                        scoreNumber = pygame.image.load(f"assets/numbers/{str(score)[1]}.png").convert_alpha()
                        scoreNumberRect = scoreNumber.get_rect()
                        scoreNumberRect.center = (width / 2, 100)
                        screen.blit(scoreNumber, scoreNumberRect)
                        scoreNumber = pygame.image.load(f"assets/numbers/{str(score)[2]}.png").convert_alpha()
                        scoreNumberRect = scoreNumber.get_rect()
                        scoreNumberRect.midleft = (width / 2 + 12, 100)
                        screen.blit(scoreNumber, scoreNumberRect)
                    elif len(str(score)) == 4:
                        scoreNumber = pygame.image.load(f"assets/numbers/{str(score)[0]}.png").convert_alpha()
                        scoreNumberRect = scoreNumber.get_rect()
                        scoreNumberRect.midright = (width / 2 - 24, 100)
                        screen.blit(scoreNumber, scoreNumberRect)
                        scoreNumber = pygame.image.load(f"assets/numbers/{str(score)[1]}.png").convert_alpha()
                        scoreNumberRect = scoreNumber.get_rect()
                        scoreNumberRect.midright = (width / 2, 100)
                        screen.blit(scoreNumber, scoreNumberRect)
                        scoreNumber = pygame.image.load(f"assets/numbers/{str(score)[2]}.png").convert_alpha()
                        scoreNumberRect = scoreNumber.get_rect()
                        scoreNumberRect.midleft = (width / 2, 100)
                        screen.blit(scoreNumber, scoreNumberRect)
                        scoreNumber = pygame.image.load(f"assets/numbers/{str(score)[3]}.png").convert_alpha()
                        scoreNumberRect = scoreNumber.get_rect()
                        scoreNumberRect.midleft = (width / 2 + 24, 100)
                        screen.blit(scoreNumber, scoreNumberRect)

                    pygame.display.update()

                    if birdPosY <= -50:
                        print("Out Of Bounds")
                        birdPosY = -45

                    for i in range(len(pipes)):
                        if pipes[i][0] - 40 <= birdPosX <= pipes[i][0] + 40:
                            if (birdPosY <= pipes[i][1] - 40) or (birdPosY >= pipes[i][1] + 40):
                                print("Game over")

                                gameoverScreen(pipes, birdPosX, birdPosY, floor, score)

                                while True:
                                    for event in pygame.event.get():

                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            exit()

                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            mouse = pygame.mouse.get_pos()
                                            print(f"{mouse[0]} {mouse[1]}")

                                            if 82 < mouse[0] < 206 and 380 < mouse[1] < 420:
                                                print("Restarting")
                                                game()

                    if birdPosY >= 430:
                        print("Game over")

                        gameoverScreen(pipes, birdPosX, birdPosY, floor, score)

                        while True:
                            for event in pygame.event.get():

                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    exit()

                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse = pygame.mouse.get_pos()
                                    print(f"{mouse[0]} {mouse[1]}")

                                    if 82 < mouse[0] < 206 and 380 < mouse[1] < 420:
                                        print("Restarting")
                                        game()

                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            birdJump = True
                            birdJumpPixels = 0
                            birdFallPixels = 0


game()
