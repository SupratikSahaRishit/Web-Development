import pygame
import random
import math


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 300
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 18
COLLISION_DISTANCE = 27

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")


background = pygame.image.load("background.png")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("player.png")
enemyImg = pygame.image.load("enemy.png")
bulletImg = pygame.image.load("bullet.png")
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

num_of_enemies = 7

enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(num_of_enemies):
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)


bulletX = 0
bulletY = PLAYER_START_Y
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"


score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
over_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score():
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (10, 10))


def game_over():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (180, 220))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 +
                         (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE


running = True

while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    playerX += playerX_change

    if playerX <= 0:
        playerX = 0

    elif playerX >= SCREEN_WIDTH - 64:
        playerX = SCREEN_WIDTH - 64


    for i in range(num_of_enemies):

        if enemyY[i] > 340:
            game_over()
            running = False
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = ENEMY_SPEED_X
            enemyY[i] += enemyY_change[i]

        elif enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] = -ENEMY_SPEED_X
            enemyY[i] += enemyY_change[i]

        # Collision
        if bullet_state == "fire":
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)

            if collision:
                bullet_state = "ready"
                bulletY = PLAYER_START_Y
                score_value += 1

                enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
                enemyY[i] = random.randint(
                    ENEMY_START_Y_MIN,
                    ENEMY_START_Y_MAX
                )

        enemy(enemyX[i], enemyY[i])


    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"

    player(playerX, playerY)
    show_score()

    pygame.display.update()

pygame.quit()