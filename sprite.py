import pygame
from config import *

class Group:
    def __init__(self):
        self.layers = {}
        for layerNumber in range(MAX_LAYER): self.layers[str(layerNumber)] = pygame.sprite.Group()

    def add(self,sprite:pygame.sprite.Sprite,layer): self.layers[str(layer)].add(sprite)
    def update(self):
        for i in range(MAX_LAYER):
            self.layers[str(i)].update()
    def draw(self):
        screen = pygame.display.get_surface()
        for i in range(MAX_LAYER):
            self.layers[str(i)].draw(screen)

from player import *

class Sprites:
    def __init__(self):
        self.group = Group()

        self.player = player()

        self.group.add(self.player,0)

    def update(self,data):
        self.player.Update(data)
        
        self.group.update()
        self.group.draw()