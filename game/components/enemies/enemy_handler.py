from game.components.enemies.ship import Ship
from game.components.enemies.predator_ship import PredatorShip
from game.components.enemies.alien_ship import AlienShip
from game.components.enemies.golden_ship import GoldenShip



class EnemyHandler:
    MAX_ENEMIES_ON_SCREEN = 3



    def __init__(self):
        self.enemies = []
        self.number_enemy_destroyed = 0
        self.ships_destroyed = 0
        self.predators_destroyed = 0
        self.goldens_destroyed = 0
        self.destroyed_ships = []



    def update(self, bullet_handler, player):

        # Actualizar las naves enemigas y contar las destruidas
        for enemy in self.enemies:
            self.colission_player(enemy, player)
            enemy.update(bullet_handler)

            # Comprobar si el enemigo ha salido de la pantalla
            if not enemy.is_alive or enemy.is_destroyed:
                if enemy.is_destroyed:
                    self.number_enemy_destroyed += 1 
                    if isinstance(enemy, Ship):
                        self.ships_destroyed += 1
                        self.destroyed_ships.append('ship')
                    elif isinstance(enemy, PredatorShip):
                        self.predators_destroyed += 1
                        self.destroyed_ships.append('predator')
                    elif isinstance(enemy, GoldenShip):
                        self.goldens_destroyed += 1
                        self.destroyed_ships.append('golden')
                    elif isinstance(enemy, AlienShip):
                        self.destroyed_ships.append('alien')
                self.remove_enemy(enemy)

        # Lógica para generar nuevos enemigos
        self.generate_new_enemies()



    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self, enemy_ship):
        
        if len(self.enemies) < self.MAX_ENEMIES_ON_SCREEN:
            self.enemies.append(enemy_ship)



    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def colission_player(self, enemy, player):
        if(enemy.rect.colliderect(player.rect)):
            player.life -= 1
            if player.life == 0:
              player.is_alive = False

    def generate_new_enemies(self):
        # Lógica para generar nuevos enemigos según las reglas establecidas
        if len(self.enemies) < self.MAX_ENEMIES_ON_SCREEN:
            if self.ships_destroyed >= 3:
                self.add_enemy(PredatorShip())
                self.ships_destroyed = 0
            elif self.predators_destroyed >= 3:
                self.add_enemy(GoldenShip())
                self.predators_destroyed = 0
            elif self.goldens_destroyed >= 3:
                self.add_enemy(AlienShip())
                self.goldens_destroyed = 0
            else:
                self.add_enemy(Ship())



    def get_enemies_destroyed_summary(self):
        return {
            "ships": self.destroyed_ships.count('ship'),
            "predator": self.destroyed_ships.count('predator'),
            "golden": self.destroyed_ships.count('golden'),
            "alien": self.destroyed_ships.count('alien')
        }


    def reset(self):
        self.enemies = []
        self.number_enemy_destroyed = 0
        self.ships_destroyed = 0
        self.predators_destroyed = 0
        self.goldens_destroyed = 0
        self.destroyed_ships = []
