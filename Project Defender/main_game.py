import pygame
import math
import random

# Intialize The Pygame
pygame.init()

# Create The Screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('Project Defender/background.jpg')

# Title
pygame.display.set_caption("Project Defender")

# Icon
icon = pygame.image.load('Project Defender/icon.png')
pygame.display.set_icon(icon)

screenY = -600

# Player
playerImg = pygame.image.load('Project Defender/spaceship.png')
playerX = 370
playerY = 480

# Enemy
enemyImg = pygame.image.load('Project Defender/ghost.png')
enemyX = random.randint(-5, 740)
enemyY = 50
enemyX_change = 0.1
enemyY_change = 40

# Bullet
bulletImg = pygame.image.load('Project Defender/square.png')
bulletX = 0
bulletY = 0
bulletX_change = 0
bulletY_change = 0.5
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 24, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow((enemyX-bulletX), 2)) + (math.pow((enemyY-bulletY), 2)))
    if distance < 27:
        return True
    else:
        return False

# Main Game
running = True
hit = 0
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, screenY))
    screenY += 0.1
    if screenY >= 0:
        screenY = -600
    
    pygame.mouse.set_visible(False)

    if bullet_state == "ready":
        bulletY = playerY
        bulletX = playerX

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_press = pygame.mouse.get_pressed()
            if mouse_press[0]:
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False

    mouse_location = pygame.mouse.get_pos()
    playerX = mouse_location[0] - 25
    playerY = mouse_location[1] - 25

    enemyX += enemyX_change
    if playerX <= -5:
        playerX = -5
    elif playerX >= 740:
        playerX = 740
    if playerY <= 0:
        playerY = 0
    elif playerY >= 535:
        playerY = 535
    if enemyX >= 740:
        enemyX = 740
        enemyX_change = -enemyX_change
    elif enemyX <= -5:
        enemyX = -5
        enemyX_change = -enemyX_change

    # Bullet Movement
    if bulletY <= -20:
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        if hit < 4:
            if bulletX < enemyX:
                bulletX += 0.5
            elif bulletX > enemyX:
                bulletX -= 0.5

    # Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision and bullet_state == "fire":
        bullet_state = "ready"
        hit += 1
        
    if hit < 4:
        enemy(enemyX, enemyY)
    player(playerX, playerY)
    pygame.display.update()
