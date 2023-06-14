#clase para heredar valores. hereda comportamiento, metodos, atr. de padres a hijos para evitar 
#escrbir el mismo codigo siempre

import pygame
from game.components.enemies.enemy_2 import Enemy_2
from game.utils.constants import ENEMY_2


class Ship_2(Enemy_2):
    WIDTH = 60   #definir tambien en spaceship
    HEIGTH = 80


    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)   




