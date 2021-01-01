import pygame

pygame.init()
width, height = 288, 512
backgroundColor = 255, 0, 0

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
icon = pygame.image.load("assets/yellowbird-upflap.png").convert()
icon = pygame.transform.scale(icon, (17, 17))
pygame.display.set_icon(icon)
pygame.display.set_caption("Flappy Bird")

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)
transparent = (0, 0, 0, 0)

background = pygame.image.load("assets/background-day.png").convert()
backgroundRect = background.get_rect()
backgroundRect.topleft = (0, 0)
screen.blit(background, backgroundRect)

startScreen = pygame.image.load("assets/message.png").convert_alpha()
startScreenRect = startScreen.get_rect()
startScreenRect.center = (width / 2, height / 2)
screen.blit(startScreen, startScreenRect)

pygame.display.update()

birdPositionX, birdPositionY = 144, 304

while True:
    clock.tick(30)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            print(f"{mouse[0]} {mouse[1]}")

            while True:
                screen.fill(black)

                background = pygame.image.load("assets/background-day.png").convert()
                backgroundRect = background.get_rect()
                backgroundRect.topleft = (0, 0)
                screen.blit(background, backgroundRect)

                bird = pygame.image.load("assets/yellowbird-upflap.png").convert()
                birdRect = bird.get_rect()
                birdRect.center = (birdPositionX, birdPositionY)
                screen.blit(bird, birdRect)

                pygame.display.update()
