import random
import math 
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game.components.enemies.enemy import Enemy


class Enemy_3(Enemy):
    X_POS_LIST = [50, 100, 150, 200, 250 , 300, 350, 400, 450, 500]  #pocision random
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 3
    LEFT = 'left'  # asignar valores constante, buena practica para evitar error con string
    RIGHT = 'right'
    MOV_X = [LEFT, RIGHT]
    INTERVAL = 200
    WAVE_AMPLITUDE = 5
    WAVE_FREQUENCY = 0.1

    def __init__(self, image):
        self.image = image
        # self.rect = self.image.get_rect()
        # self.rect.x = random.choice(self.X_POS_LIST)
        # self.rect.y = self.Y_POS
        # self.mov_x = random.choice(self.MOV_X)
        # self.index = 0  #contador de desplazamiento 
        super().__init__(self.image)

    def update (self):

        sinusoidal_movement = self.WAVE_AMPLITUDE * math.sin(self.WAVE_FREQUENCY * self.index)
        self.rect.y += self.SPEED_Y + sinusoidal_movement 
        super().update()
        # if self.mov_x == self.LEFT:
        #     self.rect.x -= self.SPEED_X
        #     if self.index > self.INTERVAL or self.rect.x <= 0:
        #         self.mov_x = self.RIGHT
        #         self.index = 0

        # else:
        #     self.rect.x += self.SPEED_X
        #     if self.index > self.INTERVAL or self.rect.x >= SCREEN_WIDTH - self.rect.width:
        #         self.mov_x = self.LEFT
        #         self.index = 0

        # self.index += 1
        
        # if self.rect.y > SCREEN_HEIGHT:
        #     self.rect.y = -10 
        #     self.rect.x = random.choice(self.X_POS_LIST)


    # def draw (self, screen):
    #     screen.blit(self.image, self.rect)
