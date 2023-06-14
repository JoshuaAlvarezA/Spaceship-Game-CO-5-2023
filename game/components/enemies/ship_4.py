#clase para heredar valores. hereda comportamiento, metodos, atr. de padres a hijos para evitar 
#escrbir el mismo codigo siempre

import pygame
from game.components.enemies.enemy_4 import Enemy_4
from game.utils.constants import ENEMY_4


class Ship_4(Enemy_4):
    WIDTH = 80   #definir tambien en spaceship
    HEIGTH = 60


    def __init__(self):
        self.image = ENEMY_4
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)   




