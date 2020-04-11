from builtins import range, open

import pygame
from pygame.constants import MOUSEBUTTONUP
from pygame.locals import *
import imageio
import csv

black = (0, 0, 0)
white = (255, 255, 255)

for i in range(0, 3):
    brush = pygame.image.load("brush.png")
    brush = pygame.transform.scale(brush, (10, 10))
    pygame.init()
    size = (125, 125)
    screen = pygame.display.set_mode(size)
    screen.fill(white)
    pygame.display.update()
    z = 0
    check = True

    while check:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.image.save(screen, "input.png")
                check = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                z = 1
            elif event.type == MOUSEBUTTONUP:
                z = 0

            if z == 1:
                screen.blit(brush, (x-5, y-5))
                pygame.display.update()


    l = []
    im = imageio.imread("input.png")
    for i in range(0, 125):
        for j in range(0, 125):
            if im[i, j][0] == 255 and im[i, j][1] == 255 and im[i, j][2] == 255:
                l.append(0)
            else:
                l.append(1)
    l.append(0)
    with open("data.csv", 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(l)

    csvFile.close()
    pygame.quit()
