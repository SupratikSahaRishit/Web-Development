import pygame

pygame.init()

w = 600
h = 600

scrn = pygame.display.set_mode((w, h))
pygame.display.set_caption('image')

imp = pygame.image.load("rocketship.gif")

scrn.blit(imp, (200, 0))

pygame.display.flip()

status = True
while status:

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            status = False

pygame.quit()
