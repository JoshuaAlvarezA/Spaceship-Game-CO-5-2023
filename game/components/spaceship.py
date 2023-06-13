import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship:    #para agregar imagen necesitamos posicion
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500 
#con self se vuelve atributo, python lo convierte automaticamente 

    def __init__(self):
        self.image = SPACESHIP 
        self.image = pygame.transform.scale(self.image, (40,60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, user_input):
        #se debe mover solo si se oprime tecla
        if user_input [pygame.K_LEFT]:
            self.move_left()
        elif user_input [pygame.K_DOWN]:
            self.move_down()
        elif user_input [pygame.K_RIGHT]:
            self.move_right()
        elif user_input [pygame.K_UP]:
            self.move_up()

    
    def draw (self, screen):
        screen.blit(self.image, self.rect)

    
    
    
    # vamos a crear metodos para movimiento 
    
    def move_left(self):
        #restriccion para que no salga de los limites 
        self.rect.x -= 10 
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH - 40
    
    def move_right(self):
        #restriccion para que no salga de los limites 
        self.rect.x += 10 
        if self.rect.right > SCREEN_WIDTH:
            self.rect.x = 0
    


    def move_up(self):
        #restriccion para que no salga de los limites 
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10 
    

    
    def move_down(self):
        #restriccion para que no salga de los limites 
        if self.rect.y < SCREEN_HEIGHT - 60:
            self.rect.y += 10 
    