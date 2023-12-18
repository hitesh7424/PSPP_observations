#Program to print text in desired size using pygame tool
import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
done = False
#load the fonts
font = pygame.font.SysFont("Times new Roman", 72)
text = font.render("Hello, Pygame", True, (158, 16, 16))
while not done:
for event in pygame.event.get():
Output
