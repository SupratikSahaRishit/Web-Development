import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()


player_rect = Rect(200, 500, 50, 50)
player_rect2 = Rect(200, 0, 50, 50)

speed_a = 8
speed_b = -7


rect3 = Rect(0, 250, 50, 50)
rect4 = Rect(550, 250, 50, 50)

speed_c = 6
speed_d = -6

run = True

while run:

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    clock.tick(60)


    player_rect.bottom += speed_a
    player_rect2.top += speed_b

    if player_rect.colliderect(player_rect2):
        speed_a *= -1
        speed_b *= -1

    if player_rect.top < 0 or player_rect.bottom > 600:
        speed_a *= -1

    if player_rect2.top < 0 or player_rect2.bottom > 600:
        speed_b *= -1


    rect3.left += speed_c
    rect4.left += speed_d

    if rect3.colliderect(rect4):
        speed_c *= -1
        speed_d *= -1

    if rect3.left < 0 or rect3.right > 600:
        speed_c *= -1

    if rect4.left < 0 or rect4.right > 600:
        speed_d *= -1


    window.fill((255, 255, 255))

    pygame.draw.rect(window, (255, 255, 0), player_rect)   
    pygame.draw.rect(window, (255, 0, 255), player_rect2) 
    pygame.draw.rect(window, (0, 255, 0), rect3)           
    pygame.draw.rect(window, (0, 0, 255), rect4)           

    pygame.display.update()

pygame.quit()