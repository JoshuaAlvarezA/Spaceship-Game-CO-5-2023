import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import BULLET, BULLET_SPACESHIP_TYPE


class BulletShip(Bullet):
    WIDTH = 9
    HEIGTH = 32
    SPEED = 20

    def __init__(self, center):
        self.image = BULLET
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image, center, BULLET_SPACESHIP_TYPE)


    def update(self, enemy_handler): #enemy implementation for review
        self.rect.y -= self.SPEED

        if self.rect.y <= 0:
            self.show = False


        for enemy in enemy_handler.enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.life -= 1
                if(enemy.life == 0):
                    enemy.is_alive = False
                    self.show = False
                    enemy.is_destroyed = True
            