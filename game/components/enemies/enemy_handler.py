#objeto para crear multiple enemigos 
import random

from game.components.enemies.ship import Ship
from game.components.enemies.predator_ship import Predator_Ship
from game.components.enemies.alien_ship import Alien_Ship
from game.components.enemies.golden_ship import Golden_Ship


class EnemyHandler:
    def __init__(self):
        self.enemies = []
        # self.list_ships = [Ship(), Predator_Ship(), Alien_Ship(), Golden_Ship()]
        # self.ship = random.choice(self.list_ships)

    def update(self, bullet_handler):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(bullet_handler)
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        
        if len(self.enemies) < 2:
            #dos enemigo a la vez
            self.enemies.append(Alien_Ship())
            
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
