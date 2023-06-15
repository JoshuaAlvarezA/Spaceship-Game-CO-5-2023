#clase para heredar valores. hereda comportamiento, metodos, atr. de padres a hijos para evitar 
#escrbir el mismo codigo siempre

import pygame
from game.components.enemies.predator import Predator
from game.utils.constants import ENEMY_2


class PredatorShip(Predator):
    WIDTH = 60   #definir tambien en spaceship
    HEIGTH = 80


    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)   




