import pygame
from config import *
from sprite import Sprites

class main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        self.sprite = Sprites()
        self.clock = pygame.time.Clock()

        self.data = {}
        
    def gameloop(self):
        while True:
            self.screen.fill((0,0,0))

            self.clock.tick(60)
            self.get_event()
            self.sprite.update(self.data)

            pygame.display.update()

    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
                pygame.quit()
                import sys;sys.exit()

    def quit(self):
        pass

if __name__=="__main__":
    main().gameloop()