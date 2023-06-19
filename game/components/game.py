import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, WHITE_COLOR, DEFAULT_TYPE, MAIN_MENU
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler
from game.components.bullets.bullet_handler import BulletHandler
from game.components import text_utils
from game.components.powers.power_handler import PowerHandler

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()
        self.score = 0 
        self.number_death = 0
        self.max_score = 0
        self.power_handler = PowerHandler()
        self.in_menu = True
        self.in_game = False
        self.in_stats = False
        self.paused = False
        self.x_pos_mm = 0
        self.y_pos_mm = 0

    def run(self):
        pygame.mixer.music.load(r"game\assets\soundtrack\Empire_Earth.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if self.in_menu:
                self.menu_events()
            elif self.in_game:
                self.events()
            elif self.in_stats:
                self.stats_events()
            
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()


    def menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.in_menu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.play_button.collidepoint(x, y):
                    self.in_menu = False
                    self.in_game = True
                elif self.quit_button.collidepoint(x, y):
                    self.running = False
                    self.in_menu = False


    def stats_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.in_stats = False
            # logica para regresar al menu

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.in_game = False


            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # regresar al menu principal
                if hasattr(self, 'back_to_menu_button') and self.back_to_menu_button.collidepoint(x, y):
                    
                    self.reset()
                    self.in_game = False
                    self.in_menu = True
                # comprobamos nuevo juego
                elif hasattr(self, 'new_game_button') and self.new_game_button.collidepoint(x, y):
                    
                    self.reset()
                    self.playing = True

            #presionar cualquier tecla para arrancar el juego 
            elif event.type == pygame.KEYDOWN:
                if not self.playing:
                    self.in_game = True
                    self.playing = True
                    self.reset() #reiniciar el juego

            

    def update(self):
       if self.in_game and not self.paused: 
            if self.playing:
                user_input = pygame.key.get_pressed()
                self.player.update(user_input, self.bullet_handler)
                self.enemy_handler.update(self.bullet_handler, self.player)
                self.bullet_handler.update(self.player, self.enemy_handler)
                self.score = self.enemy_handler.number_enemy_destroyed
                self.power_handler.update(self.player)
                if not self.player.is_alive:
                    pygame.time.delay(300)
                    self.playing = False
                    self.number_death += 1 

    def draw(self):

        if self.in_menu:
            self.draw_main_menu()
        elif self.in_stats:
            self.draw_stats_page()
        elif self.in_game:
            self.draw_background()
            if self.playing:
                self.clock.tick(FPS)        
                self.player.draw(self.screen)  
                self.enemy_handler.draw(self.screen)
                self.bullet_handler.draw(self.screen)
                self.draw_score()
                self.max_scores()
                self.power_handler.draw(self.screen)
                self.draw_power_time()
            else:
                self.draw_menu()
            pygame.display.update()
            pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed


    def draw_main_menu(self):

        image = pygame.transform.scale(MAIN_MENU, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_mm, self.y_pos_mm))
        self.screen.blit(image, (self.x_pos_mm, self.y_pos_mm - image_height))
        
        #boton jugar
        self.play_button = pygame.draw.rect(self.screen, (0, 255, 0), (475, 250, 150, 50))
        play_text, play_text_rect = text_utils.get_message('Play', 30, (255, 255, 255))
        play_text_rect.center = self.play_button.center
        self.screen.blit(play_text, play_text_rect)

        # salir del juego
        self.quit_button = pygame.draw.rect(self.screen, (255, 0, 0), (475, 320, 150, 50))
        quit_text, quit_text_rect = text_utils.get_message('Quit', 30, (255, 255, 255))
        quit_text_rect.center = self.quit_button.center
        self.screen.blit(quit_text, quit_text_rect)
        
        pygame.display.update()

    

    def draw_menu(self):

        if self.number_death == 0:
            text, text_rect = text_utils.get_message('PRESS ANY KEY TO START', 30, WHITE_COLOR)
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_message('PRESS ANY KEY TO START', 30, WHITE_COLOR)
            self.screen.blit(text, text_rect)
            score, score_rect = text_utils.get_message(f'SCORE: {self.score}', 30,  WHITE_COLOR, heigth=SCREEN_HEIGHT//2 +50)
            text, text_rect = text_utils.get_message(f'Attempts: {self.number_death}', 30,  WHITE_COLOR, heigth=SCREEN_HEIGHT//2 +80)
            max_score, max_score_rect = text_utils.get_message(f'Max Score: {self.max_score}', 30,  WHITE_COLOR, heigth=SCREEN_HEIGHT//2 +110)
            
            self.screen.blit(score, score_rect)  
            self.screen.blit(text, text_rect)  
            self.screen.blit(max_score, max_score_rect)

             #lista de destruidos
            enemies_destroyed = self.enemy_handler.get_enemies_destroyed_summary()
            y_offset = 140
            for enemy_type, count in enemies_destroyed.items():
                enemy_text, enemy_text_rect = text_utils.get_message(f'{enemy_type}: {count}', 30, WHITE_COLOR, heigth=SCREEN_HEIGHT//2 + y_offset)
                self.screen.blit(enemy_text, enemy_text_rect)
                y_offset += 30


             
            self.back_to_menu_button = pygame.draw.rect(self.screen, (255, 0, 0), (20, 100, 200, 50))
            back_to_menu_text, back_to_menu_text_rect = text_utils.get_message('Main Menu', 30, (255, 255, 255))
            back_to_menu_text_rect.center = self.back_to_menu_button.center
            self.screen.blit(back_to_menu_text, back_to_menu_text_rect)
            
            
            self.new_game_button = pygame.draw.rect(self.screen, (0, 255, 0), (880, 100, 200, 50))
            new_game_text, new_game_text_rect = text_utils.get_message('New Game', 30, (255, 255, 255))
            new_game_text_rect.center = self.new_game_button.center
            self.screen.blit(new_game_text, new_game_text_rect)

    def draw_score(self):
        score, score_rect = text_utils.get_message(f'Score: {self.score}', 20,  WHITE_COLOR, 1000, 40)
        self.screen.blit(score, score_rect)

        
        lives, lives_rect = text_utils.get_message(f'Lives: {self.player.life}', 20, WHITE_COLOR, 1000, 70)
        self.screen.blit(lives, lives_rect)


    def max_scores(self):
        max_score, max_score_rect = text_utils.get_message(f'Max Score: {self.max_score}', 20,  WHITE_COLOR, 500, 40)
        self.screen.blit(max_score, max_score_rect)
        
        if(self.score > self.max_score):
            self.max_score = self.score


    def draw_power_time(self):
        if self.player.has_power:
            power_time = round((self.player.power_time - pygame.time.get_ticks()) / 1000, 1)

            if power_time >= 0 :
                text, text_rect = text_utils.get_message(f"{self.player.power_type.capitalize()} is enabled for {power_time}", 20, WHITE_COLOR, 150, 50)
                self.screen.blit(text, text_rect)

            else:
                self.player.has_power = False
                self.player.power_type = DEFAULT_TYPE
                self.player.set_default_image()
            

    def reset(self):
        self.player.reset()
        self.enemy_handler.reset()
        self.bullet_handler.reset()
        self.score = 0
        self.power_handler.reset()
