import random
from game.utils.constants import SCREEN_WIDTH
from game.components.enemies.enemy import Enemy


class Golden_Destroyer(Enemy):
    X_POS_LIST = [i for i in range(50, SCREEN_WIDTH, 50)]  #pocision random
    Y_POS = 20
    SPEED_X = 7
    SPEED_Y = 0.5
    LEFT = 'left'  # asignar valores constante, buena practica para evitar error con string
    RIGHT = 'right'
    MOV_X = [LEFT, RIGHT]
    INTERVAL = 500
    TELEPORT_X_POS_LIST = [100, 200, 300, 400, 500, 600]  # Pocisiones predefinidas en x
    TELEPORT_INTERVAL = 100  # Cambiar la posición en x cada 100 frames
    LIFE = 3

    def __init__(self, image):
        self.image = image
    #     self.rect = self.image.get_rect()
    #     self.rect.x = random.choice(self.X_POS_LIST)
    #     self.rect.y = self.Y_POS
    #     self.mov_x = random.choice(self.MOV_X)
    #     self.index = 0  #contador de desplazamiento 
        
        super().__init__(self.image, self.LIFE)
        

    def move(self):

        if self.index % self.TELEPORT_INTERVAL == 0:
            next_position_index = (self.index // self.TELEPORT_INTERVAL) % len(self.TELEPORT_X_POS_LIST)
            self.rect.x = self.TELEPORT_X_POS_LIST[next_position_index]

        super().move()

    # def update (self):
    #     self.rect.y += self.SPEED_Y
    #     if self.mov_x == self.LEFT:
    #         self.rect.x -= self.SPEED_X
    #         if self.index > self.INTERVAL or self.rect.x <= 0:
    #             self.mov_x = self.RIGHT
    #             self.index = 0

    #     else:
    #         self.rect.x += self.SPEED_X
    #         if self.index > self.INTERVAL or self.rect.x >= SCREEN_WIDTH - self.rect.width:
    #             self.mov_x = self.LEFT
    #             self.index = 0

    #     self.index += 1

    #     if self.rect.y > SCREEN_HEIGHT:
    #         self.rect.y = -10 
    #         self.rect.x = random.choice(self.X_POS_LIST)


    # def draw (self, screen):
    #     screen.blit(self.image, self.rect)
