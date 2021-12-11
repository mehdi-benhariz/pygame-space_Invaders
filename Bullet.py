import pygame


class Bullet():
    bullets = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bulletImg = pygame.image.load("torpedo.png")
        self.is_fire = False

    def set_fire(self, val):
        self.is_fire = val

    def show(self, screen):
        if(self.is_fire):

            screen.blit(self.bulletImg, (self.x, self.y))
            self.y -= 5
        # delete the object it hits an ennemy
        # delete the object it goes out of screen
