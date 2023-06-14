#clase para heredar valores. hereda comportamiento, metodos, atr. de padres a hijos para evitar 
#escrbir el mismo codigo siempre

import pygame
from game.components.enemies.enemy_3 import Enemy_3
from game.utils.constants import ENEMY_3


class Ship_3(Enemy_3):
    WIDTH = 100   #definir tambien en spaceship
    HEIGTH = 120


    def __init__(self):
        self.image = ENEMY_3
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)   




