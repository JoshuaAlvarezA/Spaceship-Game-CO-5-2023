#objeto para crear multiple enemigos 
import random

from game.components.enemies.ship import Ship
from game.components.enemies.predator_ship import PredatorShip
from game.components.enemies.alien_ship import AlienShip
from game.components.enemies.golden_ship import GoldenShip



class EnemyHandler:
    SHIP =  'Ship'
    PREDATOR = 'Predator'
    GOLDEN = 'Golden'
    ALIEN = 'Alien'
    LIST_SHIP = [SHIP, PREDATOR, GOLDEN, ALIEN]


    def __init__(self):
        self.enemies = []
        # self.list_ships = [Ship(), Predator_Ship(), Alien_Ship(), Golden_Ship()]
        # self.ship = random.choice(self.list_ships)

    def update(self, bullet_handler, player):
        ship_choice = random.choice(self.LIST_SHIP)
        if ship_choice == self.SHIP:
            self.add_enemy(Ship())
        elif ship_choice == self.PREDATOR:
            self.add_enemy(PredatorShip())
        elif ship_choice == self.ALIEN:
            self.add_enemy(AlienShip())
        elif ship_choice == self.GOLDEN:
            self.add_enemy(GoldenShip())
        
        for enemy in self.enemies:
            self.colission_player(enemy,player)
            enemy.update(bullet_handler)
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self, enemy_ship):
        
        if len(self.enemies) < 2:
            #dos enemigo a la vez
            self.enemies.append(enemy_ship)
            
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def colission_player(self, enemy, player):
        if(enemy.rect.colliderect(player.rect)):
            player.is_alive = False

    
        
