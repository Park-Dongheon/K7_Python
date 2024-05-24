
import sys
import pygame

from alien import Alien
from ship import Ship


class Game:
    def __init__(self, title):
        self.title = title
        pygame.init()

        self.screen_surf = pygame.display.set_mode(size=(800, 640))
        #print(type(screen_surf), screen_surf.get_rect())
        self.ship = Ship(self.screen_surf)
        self.ship.move_midbottom()

        self.aliens = []
        alien = Alien(self.screen_surf)
        alien.move(50, 50)
        self.aliens.append(alien)

        alien = Alien(self.screen_surf)
        alien.move(150, 150)
        self.aliens.append(alien)

        font = pygame.font.SysFont(None, 64)
        self.font_surf = font.render(
            str(5678), 
            True, 
            'black'
            )
        #print(font_surf.get_rect())

        self.bullets = []
        

        bullet_rect = pygame.Rect(0, 0, 10, 50)
        #print(bullet_rect)
        self.bullets.append(bullet_rect)

        self.clock = pygame.time.Clock()

    def start(self):
        while True:
            events = pygame.event.get() 
            for e in events:
                print(e.type, type(e.type))
                if e.type == pygame.QUIT:
                    #print('QUIT')
                    sys.exit()
                elif e.type == pygame.KEYDOWN:
                    pass
                    #print('KEYDOWN')
                    #print(e.key, type(e.key)) # 32 SPACE, 13 ENTER, 
                    # 1073741904 left_key 
                elif e.type == pygame.KEYUP:
                    #print('KEYUP')
                    #print(e.key, type(e.key))
                    # sys.exit()
                    if e.key == pygame.K_SPACE:
                        #print("SPACE")
                        sys.exit()

            self.screen_surf.fill('white')
            self.ship.render()
            for alien in self.aliens:
                alien.render()
            self.screen_surf.blit(self.font_surf, (100, 100, 
                                        self.font_surf.get_rect().width,
                                        self.font_surf.get_rect().height))   
            pygame.display.flip()
            self.clock.tick(60)

    def __str__(self):
       return self.title

