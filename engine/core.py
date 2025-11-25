import pygame

from engine.input import InputManeger
from engine.assets import AssetsManeger
from engine.physics import PhysicsManager
from engine.scene import Scene
from engine.entity import EntityManager


class Game:
    def  __init__(self, width=800, height=600, title="My Adventure Game"):
        self.width = width
        self.height = height
        self.title = title

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()
        self.running = True

        self.scene = None
        self.pygame = pygame

        self.input = InputManeger(pygame)
        self.assets = AssetsManeger(pygame)
        self.entities = EntityManager(self)
        self.physics = PhysicsManager()
    
    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            if self.scene:
                self.scene.handle_events(events)
                self.input.update(events)
            
            if self.scene:
                self.scene.update(dt)
            
            if self.scene:
                self.scene.draw(self.screen)
            
            pygame.display.flip()
        
        pygame.quit()
    
    def change_scene(self, scene):
        if self.scene:
            self.scene.exit()
        self.scene = scene
        self.scene.enter()
