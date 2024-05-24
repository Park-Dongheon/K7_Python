import pygame


class Bullet:
    def __init__(self, screen_surf):
        self.bullet_rect = pygame.rect.Rect(0, 0, 500, 10)
        self.screen_surf =screen_surf

    def render(self):
        pygame.draw.rect(self.screen_surf, 'red', self.bullet_rect)


    def move_front_ship(self):
        self.bullet_rect.midbottom = self.ship_rect.midtop

bullet = Bullet()
move_front_ship(self)
bullet.render()