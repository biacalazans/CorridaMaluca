

import pygame
from Cow import Cow
from Ufo import Ufo
from Dino import Dino
import random

# iniciar o pygame
pygame.init()

screen = pygame.display.set_mode((825, 452))
imagemfundo = pygame.image.load('fundoestrada.jpg')

# title  and icon
pygame.display.set_caption("Corrida Maluca")
icon = pygame.image.load('icone.png')
pygame.display.set_icon(icon)

c1 = Cow(800, 200, pygame.image.load('cow.png'), -0.3)
u1 = Ufo(800, 200, pygame.image.load('sci-fi.png'), -0.3)
d1 = Dino(800, 200, pygame.image.load('dinosaur2.png'), -0.3)

obstaculos = list()

playerImg = pygame.image.load('player2.png')
playerX = 160
playerY = 310


def dino(x, y):
    screen.blit(d1.img, (x, y))


def ufo(x, y):
    screen.blit(u1.img, (x, y))


def cow(a, b):
    screen.blit(c1.img, (a, b))


def player(x, y):
    screen.blit(playerImg, (x, y))


pygame.time.set_timer(pygame.USEREVENT, random.randrange(2000, 3500))

# game loop
running = True
while running:

    screen.blit(imagemfundo, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN and playerY == 252:
                playerY += 58
            if event.key == pygame.K_UP and playerY == 310:
                playerY -= 58

        if event.type == pygame.USEREVENT:
            r = random.randrange(0, 2)
            if r == 0:
                obstaculos.append(c1)
            elif r == 1:
                obstaculos.append(u1)
            elif r == 2:
                obstaculos.append(d1)

        for obstaculos in obstaculos:
            screen.blit(obstaculos.img, (obstaculos.x, obstaculos.y))
            obstaculos.x == -1.4
            if obstaculos.x < 0:
                obstaculos.pop(obstaculos.index(obstaculos))

    player(playerX, playerY)
    pygame.display.update()
