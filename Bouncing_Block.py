import pygame
import sys

pygame.init()

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Bouncing Box')

#Box properties

x = 200
y = 200

box_width = 100
box_height = 60

speed_x = 4
speed_y = 4

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x += speed_x
    y += speed_y

    if x <= 0 or x + box_width >= WIDTH:
        speed_x = -speed_x

    if y <= 0 or y + box_height >= HEIGHT:
        speed_y = -speed_y

    screen.fill((0,0,0))

    pygame.draw.rect(screen,(255,0,255),(x,y,box_width,box_height))

    pygame.display.update()

    clock.tick(60)   
