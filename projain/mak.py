import pygame
from pygame import event
from pygame import mouse
from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION, MOUSEWHEEL
# Intialize the pygame
pygame.init()
# create screen
screen = pygame.display.set_mode((800, 600))

font = pygame.font.Font("projain/Aquire-BW0ox.otf", 64)
textX = 10
textY = 10

def show_font():
    show = font.render("Galactic Frontier", True ,(0, 255, 0))
    screen.blit(show, (55, 120))
#show Start font
def start():
    start = font.render("Start", True ,(120, 150, 0))
    screen.blit(start, (280, 300))
#show Quit font
def show_quit():
    show_quit = font.render("QUIT", True ,(120, 150, 0))
    screen.blit(show_quit, (320, 420))
running = True
while running:
    mouse_1 = (pygame.mouse.get_pos())
    # click start or quit to QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # click start
        if event.type == pygame.MOUSEBUTTONDOWN and 280 <= mouse_1[0] <= 510 and 300<= mouse_1[1] <= 370: 
            running = False
        # click quit
        if event.type == pygame.MOUSEBUTTONDOWN and 320 <= mouse_1[0] <= 465 and 420<= mouse_1[1] <= 465: 
            running = False
    screen.fill((20, 20, 0))
    show_font()
    start()
    show_quit()
    pygame.display.update()
    
