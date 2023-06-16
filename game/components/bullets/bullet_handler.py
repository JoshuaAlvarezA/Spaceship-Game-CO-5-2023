#administrar todas las balas del juego 
from game.utils.constants import BULLET_ENEMY_TYPE, BULLET_SPACESHIP_TYPE
from game.components.bullets.bullet_enemy import BulletEnemy
from game.components.bullets.bullet_ship import BulletShip

class BulletHandler:
    def __init__(self):
        self.bullets = []  #todas las balas del juego 

    def update(self, player, enemy_handler):
        for bullet in self.bullets:
            if (not bullet.show):
                self.remove_bullet(bullet)
            if bullet.type == BULLET_SPACESHIP_TYPE:
                bullet.update(enemy_handler)
            elif bullet.type == BULLET_ENEMY_TYPE:
                bullet.update(player)
                



    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

#definir strings en variables para evitar errores
    def add_bullet(self, type, center):
        if type == BULLET_ENEMY_TYPE:
            self.bullets.append(BulletEnemy(center))
        elif type == BULLET_SPACESHIP_TYPE:
            self.bullets.append(BulletShip(center))

    def remove_bullet(self, bullet):
        self.bullets.remove(bullet)
