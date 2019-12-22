import pygame
from Cow import Cow
from Ufo import Ufo
from Dino import Dino
from Player import Player
import random

# iniciar o pygame
pygame.init()

screen = pygame.display.set_mode((825, 452))
imagemfundo = pygame.image.load('fundoestrada.jpg')
clock = pygame.time.Clock()

# title  and icon
pygame.display.set_caption("Corrida Maluca")
icon = pygame.image.load('icone.png')
pygame.display.set_icon(icon)

obstaculos = []

player = Player(160, 310, pygame.image.load('player2.png'), 2)

t = pygame.time.get_ticks()/1000


def fisica():
    a = 0.035
    vo = 5
    s = vo*t + a*t*t/2
    return s


def gameover():
    pygame.time.delay(100)
    global running, event
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
        screen.blit(imagemfundo, (0, 0))
        largeFont = pygame.font.SysFont('comicsans', 30)
        grande = pygame.font.SysFont('comicsans', 50)
        gm = grande.render('GAME OVER', 1, (0, 0, 0))
        vmed = largeFont.render('A Velocidade média do carro durante o percurso foi: {:.3} '.format(fisica()/t) + ' m/s' ,1, (0, 0, 0))
        tempo = largeFont.render('A duraçao do jogo foi de ' + str(t) + ' segundos e foram percorridos {:.3} '.format(fisica()) + ' metros', 1, (0, 0, 0))
        screen.blit(tempo, (80, 150))
        screen.blit(vmed, (140, 200))
        screen.blit(gm, (330, 100))
        pygame.display.update()


pygame.time.set_timer(pygame.USEREVENT + 1, 4700)
pygame.time.set_timer(pygame.USEREVENT + 3, 20000)

vel = 5

# game loop
running = True
while running:

    pygame.time.delay(100)
    screen.blit(imagemfundo, (0, 0))

    c1 = Cow(800, 280, pygame.image.load('cow.png'), 1)
    u1 = Ufo(800, 280, pygame.image.load('sci-fi.png'), 1)
    d1 = Dino(800, 280, pygame.image.load('dinosaur2.png'), 1)

    c2 = Cow(800, 340, pygame.image.load('cow.png'), 2)
    u2 = Ufo(800, 340, pygame.image.load('sci-fi.png'), 2)
    d2 = Dino(800, 340, pygame.image.load('dinosaur2.png'), 2)

    for o in obstaculos:
        screen.blit(o.img, (o.x, o.y))
        if player.linha == o.linha:
            if player.x + 120 >= o.x >= 150:
                gameover()
        o.x -= vel
        if o.x <= -64:
            obstaculos.pop(obstaculos.index(o))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and player.y == 310:
                player.y -= 58
                player.linha = 1
            if event.key == pygame.K_DOWN and player.y == 252:
                player.y += 58
                player.linha = 2

        elif event.type == pygame.USEREVENT + 1:
            r = random.randrange(0, 8)
            if r == 0:
                obstaculos.append(c1)
            elif r == 1:
                obstaculos.append(u1)
            elif r == 2:
                obstaculos.append(d1)
            elif r == 3:
                obstaculos.append(c2)
            elif r == 4:
                obstaculos.append(u2)
            elif r == 5:
                obstaculos.append(d2)

        if event.type == pygame.USEREVENT + 3:
            vel += 0.5

    screen.blit(player.img, (player.x, player.y))
    pygame.display.update()
