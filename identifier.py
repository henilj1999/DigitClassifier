from builtins import range
from locale import str
import pandas as pd
import imageio
from pygame.constants import MOUSEBUTTONUP
from sklearn.neural_network import MLPClassifier
import pygame
from pygame.locals import *

dataset = pd.read_csv('C:/Users/Henil Jain\Desktop/Number Identifier/data.csv')
l = []
for i in range(0, 15625):
    l.append(str(i))

X = dataset[l].values
Y = dataset['output'].values
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15,), random_state=1)
clf = clf.fit(X, Y)

black = (0, 0, 0)
white = (255, 255, 255)

for i in range(0, 10):
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

    tempX = []
    im = imageio.imread("input.png")
    for i in range(0, 125):
        for j in range(0, 125):
            if im[i, j][0] == 255 and im[i, j][1] == 255 and im[i, j][2] == 255:
                tempX.append(0)
            else:
                tempX.append(1)

    tp = []
    tp.append(tempX)

    Y_pred = clf.predict(tp)

    print(Y_pred)
