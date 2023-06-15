import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_SPACESHIP_TYPE

class Spaceship:    #para agregar imagen necesitamos posicion
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500 
    WIDTH = 40
    HEIGHT = 60
    SPEED = 10
    SHOOTING_TIME = 5000
#con self se vuelve atributo, python lo convierte automaticamente 

    def __init__(self):
        self.image = SPACESHIP 
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.shooting_time = 0

    def update(self, user_input, bullet_handler):
        #se debe mover solo si se oprime tecla
        if user_input [pygame.K_LEFT]:
            self.move_left()
        elif user_input [pygame.K_DOWN]:
            self.move_down()
        elif user_input [pygame.K_RIGHT]:
            self.move_right()
        elif user_input [pygame.K_UP]:
            self.move_up()
        elif user_input [pygame.K_SPACE]:
            self.shoot(bullet_handler)

        

    
    def draw (self, screen):
        screen.blit(self.image, self.rect)
    
    # vamos a crear metodos para movimiento 
    
    def move_left(self):
        #restriccion para que no salga de los limites 
        self.rect.x -= self.SPEED
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH - self.WIDTH
    
    def move_right(self):
        #restriccion para que no salga de los limites 
        self.rect.x += self.SPEED
        if self.rect.right > SCREEN_WIDTH:
            self.rect.x = 0
    


    def move_up(self):
        #restriccion para que no salga de los limites 
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SPEED 
    

    
    def move_down(self):
        #restriccion para que no salga de los limites 
        if self.rect.y < SCREEN_HEIGHT - self.HEIGHT:
            self.rect.y += self.SPEED 


    def shoot(self, bullet_handler):
        self.shooting_time +=1
        bullet_handler.add_bullet(BULLET_SPACESHIP_TYPE, self.rect.center)
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_handler.add_bullet(BULLET_SPACESHIP_TYPE, self.rect.center)


    

    