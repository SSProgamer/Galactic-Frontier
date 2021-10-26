import pygame
from pygame import event
# Intialize the pygame
pygame.init()
# create screen
screen = pygame.display.set_mode((800, 600))

font = pygame.font.Font("Aquire-BW0ox.otf", 64)
textX = 10
textY = 10

def show_font():
    show = font.render("Welcome", True ,(0, 255, 0))
    screen.blit(show, (200, 250))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((20, 20, 0))
    show_font()
    pygame.display.update()
    
