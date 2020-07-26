import math
import random

import pygame

# intializing the pygame
pygame.init()

# creating the screen
screen = pygame.display.set_mode((1200, 680))

# title and icon
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load('player.png')
playerX = 580
playerY = 560
playerX_change = 0

# enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 1135))
    enemyY.append(random.randint(50, 400))
    enemyX_change.append(0.4)
    enemyY_change.append(40)

# comet
cometimg = pygame.image.load('meteorites.png')
cometX = 200
cometY = 300
cometX_change = 0

# planet
planetimg = pygame.image.load('planet.png')
planetX = 800
planetY = 350
planetX_change = 0

# bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 560
bulletX_change = 0
bulletY_change = 3
bullet_state = "ready"

# score
score = 0


def player(x, y):
    screen.blit(playerimg, (round(x), round(y)))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (round(x), round(y)))


def comet(x, y):
    screen.blit(cometimg, (x, y))


def planet(x, y):
    screen.blit(planetimg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (round(x + 16), round(y + 10)))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:

    # RGB
    screen.fill((128, 128, 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # IF KEYSTROKE IS PRESSED
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            playerX_change = -0.6
        if event.key == pygame.K_d:
            playerX_change = 0.6
        if event.key == pygame.K_SPACE:
            if bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a or event.key == pygame.K_d:
            playerX_change = 0
    # checking for boundaries
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 1136:
        playerX = 1136
    # enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 1136:
            enemyX_change[i] = -0.4
            enemyY[i] += enemyY_change[i]
    # collision
    collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)

    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX[i] = random.randint(0, 1135)
        enemyY[i] = random.randint(50, 400)
    enemy(enemyX[i], enemyY[i], i)

# bullet movment
if bulletY <= 0:
    bulletY = 480
    bullet_state = "ready"

if bullet_state == "fire":
    fire_bullet(bulletX, bulletY)
    bulletY -= bulletY_change

player(playerX, playerY)
comet(cometX, cometY)
planet(planetX, planetY)
pygame.display.update()
