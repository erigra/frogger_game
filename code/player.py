import pygame
from os import walk

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        
        # images
        
        self.import_assets()
        self.frame_index = 0
        self.status = "down"
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        # float based movement
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.speed = 200

    def import_assets(self):
        self.animations = {}         # Dictionary with key (example "down": ) and value: path+filename to associated files
        for index, folder in enumerate(walk("../graphics/player")):
            if index == 0 :
                for name in folder[1]:
                    self.animations[name] = []
            else:
                for file_name in folder[2]:
                    path = folder[0].replace("\\", "/") + "/" + file_name
                    surf = pygame.image.load(path).convert_alpha()
                    key = folder[0].split("\\")[1]
                    self.animations[key].append(surf)
        print(self.animations)
                
    def move(self,dt):
        # normalize a vector if not 0
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def player_input(self):
        key_pressed = pygame.key.get_pressed()
        # horizontal input
        if key_pressed[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        elif key_pressed[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        else:
            self.direction.x = 0
        # vertical input
        if key_pressed[pygame.K_UP]:
            self.direction.y = -1
            self.status = "up"
        elif key_pressed[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = "down"
        else:
            self.direction.y = 0

    def animate(self,dt):
        current_animation = self.animations[self.status]
        if self.direction.magnitude() != 0:
            self.frame_index += 10 * dt
            if self.frame_index >= len(current_animation):
                self.frame_index = 0
        else:
            self.frame_index = 0
        self.image = current_animation[int(self.frame_index)]

    def update(self, dt):
        self.player_input()
        self.animate(dt)
        self.move(dt)
        