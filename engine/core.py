import pygame

from engine.input import InputManager
from engine.assets import AssetsManager
from engine.physics import PhysicsManager
from engine.scene import SceneManager
from engine.entity import EntityManager


class Game:
    def  __init__(self, width=800, height=600, title="My Adventure Game"):
        self.pygame = pygame

        self.width = width
        self.height = height
        self.title = title

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()
        self.running = True

        self.scene_manager = SceneManager(self)
        self.scene = None

        self.input = InputManager(pygame)
        self.assets = AssetsManager(pygame)
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

                self.scene.update(dt)

                self.physics.update()

                self.scene.draw(self.screen)
            
            
            pygame.display.flip()
        
        pygame.quit()