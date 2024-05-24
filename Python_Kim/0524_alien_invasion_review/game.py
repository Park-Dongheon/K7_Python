import sys
import pygame
from ship import Ship
from alien import Alien
from bullet import Bullet

# 객체를 생성
class Game:
    def __init__(self, title):
        pygame.init()
        self.title = title

        self.create_screen()
        self.create_ship()
        self.create_alien()
        self.create_score()


        self.bullets = []
        self.left_pressed = False
        self.right_pressed = False
        self.clock = pygame.time.Clock()

    def start(self, ):
        while True:
            events = pygame.event.get()
            for e in events:
                # print(e.type, type(e.type))
                if e.type == pygame.QUIT:
                    print('QUIT')
                    sys.exit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:
                        self.left_pressed = True
                    if e.key == pygame.K_RIGHT:
                        self.right_pressed = True

                elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_LEFT:
                        self.left_pressed = True
                    if e.key == pygame.K_RIGHT:
                        self.right_pressed = True
                    if e.key == pygame.K_SPACE:
                        bullet = Bullet(self.screen_surf)
                        bullet.move_front_ship(self.ship.get_rect())
                        self.bullets.append(bullet)

            if self.right_pressed:   
                
            if self.left_pressed:

            self.screen_surf.fill('white')
            self.screen_surf.blit(self.ship_img_surf, self.ship_img_surf.get_rect())
            for alien in self.aliens:
                alien.render()
            for bullet in self.bullets:
                bullet.render()
            self.screen_surf.blit(self.font_surf, (100, 100,
                                        self.font_surf.get_rect().width,
                                        self.font_surf.get_rect().height))
            

            self.ship.update()
            self.ship.render()
            pygame.display.flip()
            self.clock.tick(60) 

    def create_score(self):
        self.font_surf = pygame.font.SysFont(None, 64).render(
            str(5678),
            True,
            'black'
        )

    def create_alien(self):
        aliens = []
        for i in range(1, 5):
            for j in range(10):
                alien = Alien(self.screen_surf)
                x_pos = 80 + (60 * 2) * j
                y_pos = 50 + (40 * 2) * i
                alien.move(x_pos, y_pos)
                aliens.append(alien)

    def create_ship(self):
        self.ship = Ship(self.screen_surf)
        self.ship.move_midbottom()

    def create_screen(self):
        self.screen_surf = pygame.display.set_mode(size=(800, 640))


    def __str__(self):
        return self.title
