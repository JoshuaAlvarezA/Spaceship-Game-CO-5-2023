#clase para heredar valores. hereda comportamiento, metodos, atr. de padres a hijos para evitar 
#escrbir el mismo codigo siempre

import pygame
from game.components.enemies.golden_destroyer import Golden_Destroyer
from game.utils.constants import ENEMY_4


class GoldenShip(Golden_Destroyer):
    WIDTH = 80   #definir tambien en spaceship
    HEIGTH = 60


    def __init__(self):
        self.image = ENEMY_4
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image)   




