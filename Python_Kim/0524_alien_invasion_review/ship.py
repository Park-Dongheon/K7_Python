import pygame


class Ship:
    def __init__(self, screen_surf):
        self.image_path = 
        self.SPEED = 10
        self.ship_img_surf = pygame.image.load(self.image_path).convert()
        self.ship_rect = self.ship_img_surf.get_rect()
        self.screen_surf = screen_surf
    
    def render(self):
        self.screen_surf.blit(self.ship_img_surf, self.ship_rect)

    def move_midbottom(self):
        self.ship_rect.midbottom = self.screen_surf.get_rect().midbottom

    def right(self):
        screen_rect = self.screen_surf.get_rect()
        if self.ship_rect.x < screen_rect.width-self.ship_rect.width:
            self.ship_rect.x = self.ship_rect.x + self.SPEED        

    def left(self):
        if 0 < self.ship_rect.x:
            self.ship_rect.x = self.ship_rect.x - self.SPEED

    def update(self):
        
    def get_rect(self):
        return self.ship_rect