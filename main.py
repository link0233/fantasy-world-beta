import pygame
from config import *

class main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        
    def gameloop(self):
        while True:
            self.get_event()

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