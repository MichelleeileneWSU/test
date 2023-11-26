import pygame

#Initialize the pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))

# title and icon
pygame.display.set_caption("Space Invaders 581")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB
    screen.fill((74, 103, 65))
    pygame.display.update()