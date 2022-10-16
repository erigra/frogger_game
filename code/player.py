import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((50,50) )
        self.image.fill("red")
        self.rect = self.image.get_rect(center = pos)