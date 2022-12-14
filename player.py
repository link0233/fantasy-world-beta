import pygame 
from config import *

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREENSIZE[0]//2,SCREENSIZE[1]//2)

        self.Vector = pygame.Vector2()

    def Update(self,data):
        key = pygame.key.get_pressed()
        #move
        movespeed = PLAYER_MOVE_SPEED
        if key[pygame.K_LSHIFT] :
            movespeed = PLAYER_RUN_SPEED
        self.Vector.x = 0
        self.Vector.y = 0
        
        if key[pygame.K_w]:
            self.Vector.y = -1
        if key[pygame.K_s]:
            self.Vector.y = 1
        if key[pygame.K_a]:
            self.Vector.x = -1
        if key[pygame.K_d]:
            self.Vector.x = 1

        if self.Vector.magnitude() > 0:
            self.Vector = self.Vector.normalize()

        self.rect.x += self.Vector.x * movespeed
        self.rect.y += self.Vector.y * movespeed