

class Bullet:
    def __init__(self, image, center, type):
        self.image = image 
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.type = type 
        self.show = True

    def update(self, object):
        if self.rect.colliderect(object.rect):

            if self.show and not object.has_power:
            #self.show = False

                object.life -= 1
                if object.life == 0:
                    
                    object.is_alive = False
                    self.is_alive = False
            self.show = False 

            # pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    