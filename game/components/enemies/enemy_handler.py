#objeto para crear multiple enemigos 
from game.components.enemies.ship import Ship
from game.components.enemies.ship_2 import Ship_2
from game.components.enemies.ship_3 import Ship_3
from game.components.enemies.ship_4 import Ship_4


class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.enemies.append(Ship())
        self.enemies.append(Ship())
        self.enemies.append(Ship())
        self.enemies.append(Ship_2())
        self.enemies.append(Ship_3())
        self.enemies.append(Ship_4())

    def update(self):
        for enemy in self.enemies:
            enemy.update()

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)