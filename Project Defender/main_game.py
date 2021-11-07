import pygame
import math
import random

# Intialize The Pygame
pygame.init()

# Create The Screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('stage/stage01_2.png')

# Title
pygame.display.set_caption("Project Defender")

# Icon
icon = pygame.image.load('Project Defender/Assets/icon.png')
pygame.display.set_icon(icon)

# Turret
turret_1 = pygame.image.load('Project Defender/Assets/turret_1.png')
turret_2 = pygame.image.load('Project Defender/Assets/turret_2.png')
turret_3 = pygame.image.load('Project Defender/Assets/turret_3.png')
all_turretImg = []
all_turretlo = []
num_of_turret = 0
turret_state = False
turret_sec_lo = pygame.image.load('Project Defender/Assets/test.png')
slot_1 = pygame.image.load('Project Defender/Assets/slot_1.png')
slot_2 = pygame.image.load('Project Defender/Assets/slot_2.png')
slot_3 = pygame.image.load('Project Defender/Assets/slot_3.png')

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_health = []
enemy_state = []
num_of_enemies = 6
check_enemy_move = False

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('Project Defender/Assets/test.png'))
    enemyX.append((-100)-i*75)
    enemyY.append(240)
    enemyX_change.append(1)
    enemyY_change.append(1)
    enemy_health.append(4)
    enemy_state.append(False)

# Bullet
bulletImg = pygame.image.load('Project Defender/square.png')
bulletX = 0
bulletY = 0
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"


def player(select, x, y):
    screen.blit(select, (x, y))


def all_player(location, i):
    screen.blit(all_turretImg[i], (location[0], location[1]))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# Main Game
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(slot_1, (100, 540))
    screen.blit(slot_2, (320, 540))
    screen.blit(slot_3, (540, 540))

    mouse_location = pygame.mouse.get_pos()
    fix_mouse_lo = [(mouse_location[0]//60)*(60)+10,
                    (mouse_location[1]//60)*(60)]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_press = pygame.mouse.get_pressed()
            if mouse_press[0] and check_enemy_move == False and turret_state == False:
                if mouse_location[0] >= 100 and mouse_location[0] <= 260 and \
                        mouse_location[1] >= 540 and mouse_location[1] <= 600:
                    select = turret_1
                    pygame.mouse.set_visible(False)
                    turret_state = True
                elif mouse_location[0] >= 320 and mouse_location[0] <= 480 and \
                        mouse_location[1] >= 540 and mouse_location[1] <= 600:
                    select = turret_2
                    pygame.mouse.set_visible(False)
                    turret_state = True
                elif mouse_location[0] >= 540 and mouse_location[0] <= 700 and \
                        mouse_location[1] >= 540 and mouse_location[1] <= 600:
                    select = turret_3
                    pygame.mouse.set_visible(False)
                    turret_state = True
            elif mouse_press[0] and turret_state and \
                    mouse_location[0] < 780 and mouse_location[1] < 540 \
                    and fix_mouse_lo not in all_turretlo:
                pygame.mouse.set_visible(True)
                turret_state = False
                all_turretImg.append(select)
                all_turretlo.append(fix_mouse_lo)
                num_of_turret += 1
            if mouse_press[2]:
                pygame.mouse.set_visible(True)
                turret_state = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                check_enemy_move = True
            if event.key == pygame.K_1 and check_enemy_move == False:
                select = turret_1
                pygame.mouse.set_visible(False)
                turret_state = True
            if event.key == pygame.K_2 and check_enemy_move == False:
                select = turret_2
                pygame.mouse.set_visible(False)
                turret_state = True
            if event.key == pygame.K_3 and check_enemy_move == False:
                select = turret_3
                pygame.mouse.set_visible(False)
                turret_state = True

    if turret_state:
        playerX = mouse_location[0]-30
        playerY = mouse_location[1]-30
        if mouse_location[0] < 780 and mouse_location[1] < 540:
            screen.blit(turret_sec_lo, (fix_mouse_lo[0], fix_mouse_lo[1]))
        player(select, playerX, playerY)

    while True in enemy_state:
        # Remove Dead Enemy
        for i in range(num_of_enemies):
            if enemy_state[i]:
                del enemyImg[i]
                del enemyX[i]
                del enemyY[i]
                del enemyX_change[i]
                del enemyY_change[i]
                del enemy_health[i]
                del enemy_state[i]
                num_of_enemies -= 1
                break

    for i in range(num_of_turret):
        all_player(all_turretlo[i], i)

    for i in range(num_of_enemies):
        # Enemy Movement
        if check_enemy_move:
            if enemyX[i] < 130:
                enemyX[i] += enemyX_change[i]
            elif enemyY[i] < 360 and enemyX[i] < 549:
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] < 550:
                enemyX[i] += enemyX_change[i]
            elif enemyY[i] > 240:
                enemyY[i] -= enemyY_change[i]
            else:
                enemyX[i] += enemyX_change[i]

        # Collision
        
        if enemy_health[i] == 0 or enemyX[i] > 800:
            enemy_state[i] = True

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    pygame.display.update()
