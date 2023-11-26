import pygame

#Initialize the pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))

# title and icon
pygame.display.set_caption("Space Invaders 581")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

# game loop
running = True
while running:

    # RGB
    screen.fill((74, 103, 65))

    playerY -= 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX, playerY)
    pygame.display.update()


