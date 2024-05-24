import pygame


class Alien:
    def __init__(self, screen_surf):
        self.image_path = 
        self.alien_img_surf = pygame.image.load(self.image_path).convert()
        self.alien_rect = self.alien_img_surf.get_rect()
        self.screen_surf = screen_surf

    def render(self):
        self.screen_surf.blit(self.alien_img_surf, self.alien_rect)

    def move(self, x, y):
        self.alien_rect_x = x
        self.alien_rect_y = y