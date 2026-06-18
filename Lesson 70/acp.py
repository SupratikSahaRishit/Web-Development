import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Rectangle Sprites")


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


x = 100
y = 100
sprite_width = 60
sprite_height = 60
speed = 5


enemy_x = 500
enemy_y = 300


running = True
clock = pygame.time.Clock()

while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed


    x = max(0, min(x, WIDTH - sprite_width))
    y = max(0, min(y, HEIGHT - sprite_height))


    screen.fill(WHITE)


    pygame.draw.rect(screen, BLUE, (x, y, sprite_width, sprite_height))
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, sprite_width, sprite_height))
    pygame.display.flip()

    clock.tick(60)


pygame.quit()