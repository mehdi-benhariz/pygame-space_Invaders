import pygame
import random
from Bullet import Bullet

from Player import Player

pygame.init()
# create the screen
screen = pygame.display.set_mode((800, 600))
# Design
pygame.display.set_caption('project:space invader')
background = pygame.image.load('background.png')

player = Player()


# def fire():
#     global bull_X, bull_Y, is_fire, score
#     bull_Y = Y
#     bull_X = X
#     is_fire = True
#     for i in range(7):
#         if abs(Xen[i]-bull_X) < 15 or abs(Yen[i] - bull_Y) < 15:
#             destroyed[i] = True
#             score += 1
#     print(score)


# enemy diplay
enemyIm = []
Xen = []
Yen = []
dx = []
destroyed = []

for i in range(7):
    enemyIm.append(pygame.image.load("enemy.png"))
    Xen.append(random.randint(0, 800))
    Yen.append(random.randint(10, 500))
    dx.append(5)
    destroyed.append(False)


def enemy(i):
    global destroyed, enemyIm, Xen, Yen
    if destroyed[i] == False:
        screen.blit(enemyIm[i], (Xen[i], Yen[i]))


def enemyMove(i):
    global Xen, dx, Yen
    Xen[i] += dx[i]
    if Xen[i] <= 0:
        dx[i] = 5
        Yen[i] += 10
    elif Xen[i] >= 736:
        dx[i] = -5
        Yen[i] += 10


# score affiche
font = pygame.font.Font('freesansbold.ttf', 32)


def show_score(X, Y):
    screen.blit(font.render("score:" + str(score), True, (0, 255, 0)), (X, Y))


# game over affiche
game = pygame.font.Font('freesansbold.ttf', 64)


def show_game_over(X, Y):
    screen.blit(game.render("GAME OVER", True, (255, 0, 0)), (X, Y))


# looping the function
running = True
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player.move(event.key)
            if event.key == pygame.K_SPACE:
                player.fire(screen=screen)

    screen.fill((200, 200, 200))
    # show the player
    player.show(screen=screen)
    # show the bullets if exist
    for bullet in Bullet.bullets:
        bullet.show(screen)
    # for i in range(7):
    #     if Yen[i] > 440:
    #         for j in range(7):
    #             Yen[j] = 2000
    #         # show_game_over(200, 250)
    #         break
    #     if destroyed[i] == False:
    #         # enemy(i)
    #         enemyMove(i)

    # show_score(10, 10)
    pygame.display.update()
