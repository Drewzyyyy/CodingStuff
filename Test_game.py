import pygame

#initialize pygame
pygame.init()

#initialize screen
screen = pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("Space_Invaders")
icon = pygame.image.load("Assets/icon.png")
pygame.display.set_icon(icon)

#run the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,255,255))
    pygame.display.update()