import pygame
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
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pygame.image.load('Project Defender/ghost.png')
enemyX = random.randint(-5, 740)
enemyY = 50
enemyX_change = 0.1
enemyY_change = 40


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Main Game
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, screenY))
    screenY += 0.1
    if screenY >= 0:
        screenY = -600
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -0.5
            if event.key == pygame.K_d:
                playerX_change = 0.5
            if event.key == pygame.K_w:
                playerY_change = -0.5
            if event.key == pygame.K_s:
                playerY_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change = 0
            if event.key == pygame.K_ESCAPE:
                running = False
    playerX += playerX_change
    enemyX += enemyX_change
    if playerX <= -5:
        playerX = -5
    elif playerX >= 740:
        playerX = 740
    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 535:
        playerY = 535
    if enemyX >= 740:
        enemyX = 740
        enemyX_change = -0.1
    elif enemyX <= -5:
        enemyX = -5
        enemyX_change = 0.1
    enemy(enemyX, enemyY)
    player(playerX, playerY)
    pygame.display.update()
