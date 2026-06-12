import pygame


pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Rectangle and Text")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 50)

text = font.render("Hello Pygame!", True, BLACK)
text_rect = text.get_rect(center=(WIDTH // 2, 100))

rect_x = 300
rect_y = 250
rect_width = 200
rect_height = 100
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    screen.blit(text, text_rect)

    pygame.display.update()

pygame.quit()
