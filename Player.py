import pygame

from Bullet import Bullet


class Player:
    def __init__(self):
        self.playerImg = pygame.image.load("space-invaders.png")
        self.x = 370
        self.y = 500
        self.val = 10
        self.score = 0

    def show(self, screen):
        screen.blit(self.playerImg, (self.x, self.y))

    def move(self, key):
        if key == pygame.K_RIGHT and self.x < 736:
            self.x += self.val
        elif key == pygame.K_LEFT and self.x > 0:
            self.x -= self.val
        elif key == pygame.K_UP and self.y > 0:
            self.y -= self.val
        elif key == pygame.K_DOWN and self.y < 536:
            self.y += self.val

    def fire(self, screen):
        bullet = Bullet(self.x + 15, self.y)
        bullet.set_fire(True)
        Bullet.bullets.append(bullet)
        for bullet in Bullet.bullets:
            bullet.show(screen)
