import pygame
import random

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

#enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

def player(x,y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# game loop
running = True
while running:

    # RGB
    screen.fill((74, 103, 65))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if keystroke is pressed, check right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                 playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #Checking for boundries of spaceship so it doesn't go out of bounds
    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    #enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()


