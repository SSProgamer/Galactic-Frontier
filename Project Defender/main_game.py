import pygame
import math
import random

# Intialize The Pygame
pygame.init()

# Create The Screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('stage/Stage1_1.png')

# Title
pygame.display.set_caption("Project Defender")

# Icon
icon = pygame.image.load('Project Defender/Assets/icon.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Project Defender/spaceship.png')
playerX = 300
playerY = 550
all_playerImg = []
all_playerX = []
all_playerY = []
num_of_player = 0
player_state = False

turret_sec_lo = pygame.image.load('Project Defender/Assets/test.png')

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_health = []
enemy_state = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('Project Defender/Assets/test.png'))
    enemyX.append((-100)-i*75)
    enemyY.append(235)
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


def player(x, y):
    screen.blit(playerImg, (x, y))


def all_player(x, y, i):
    screen.blit(all_playerImg[i], (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow((enemyX-bulletX), 2)) +
                         (math.pow((enemyY-bulletY), 2)))
    if distance < 27:
        return True
    else:
        return False


# Main Game
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    if bullet_state == "ready" and len(all_playerX) != 0:
        bulletY = all_playerX[0] + 30
        bulletX = all_playerY[0] + 30

    mouse_location = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_press = pygame.mouse.get_pressed()
            if mouse_press[0] and player_state == False and \
                mouse_location[0] >= 300 and mouse_location[0] <= 364 and \
                    mouse_location[1] >= 550 and mouse_location[1] <= 600:
                pygame.mouse.set_visible(False)
                player_state = True
            elif mouse_press[0] and player_state:
                pygame.mouse.set_visible(True)
                player_state = False
                all_playerImg.append(pygame.image.load('Project Defender/Assets/test2.png'))
                all_playerX.append((mouse_location[0]//60)*(60)+10)
                all_playerY.append((mouse_location[1]//60)*(60))
                num_of_player += 1
                playerX = 300
                playerY = 550
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False

    if player_state:
        playerX = mouse_location[0]-30
        playerY = mouse_location[1]-30
        screen.blit(turret_sec_lo, ((mouse_location[0]//60)*(60)+10, (mouse_location[1]//60)*(60)))

    while True in enemy_state:
        #Remove Dead Enemy
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

    player(playerX, playerY)
    for i in range(num_of_player):
        all_player(all_playerX[i], all_playerY[i], i)

    for i in range(num_of_enemies):
        if enemyX[i] >= 0 and enemyX[i] <= 800 and len(all_playerX) != 0:
            fire_bullet(all_playerX[0] + 30, all_playerY[0] + 30)

        #Enemy Movement
        if enemyX[i] < 150:
            enemyX[i] += enemyX_change[i]
        elif enemyY[i] < 350 and enemyX[i] < 557:
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] < 560:
            enemyX[i] += enemyX_change[i]
        elif enemyY[i] > 249:
            enemyY[i] -= enemyY_change[i]
        else:
            enemyX[i] += enemyX_change[i]

        # Collision
        if len(all_playerY) != 0:
            collision = isCollision(enemyX[i], enemyY[i], all_playerX[0] + 30, all_playerY[0] + 30)
        if len(all_playerY) != 0 and collision and bullet_state == "fire":
            bullet_state = "ready"
            enemy_health[i] -= 1
        if enemy_health[i] == 0 or enemyX[i] > 800:
            enemy_state[i] = True

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= -20:
        bullet_state = "ready"

    pygame.display.update()
