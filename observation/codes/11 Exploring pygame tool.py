# Program to print text in desired size using pygame tool

import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
done = False

# load the fonts
font = pygame.font.SysFont("Times new Roman", 72)
text = font.render("Hello, Pygame", True, (158, 16, 16))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((255, 255, 255))
    screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    pygame.display.flip()
