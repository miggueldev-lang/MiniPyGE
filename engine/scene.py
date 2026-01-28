import pygame
from engine.entity import EntityManager
from engine.camera import Camera

class Scene: 
    def __init__(self, game): 
        self.game = game
        self.font = pygame.font.SysFont("arial", 48)
        self.entities = EntityManager(game)
        self.camera = Camera(game.width, game.height)

        self.background_color = (30, 30, 30)

    def enter(self):
        pass

    def exit(self):
        pass
    
    def handle_events(self, events):
        pass
    
    def update(self, dt):
        self.entities.update(dt)
    
    def draw(self, screen):
        screen.fill(self.background_color)
        self.entities.draw(screen)

class SceneManager:
    def __init__(self, game):
        self.game = game
        self.scenes = {}
        self.current_scene = None
    
    def add_scene(self, name: str, scene: Scene):
        self.scenes[name] = scene
    
    def change_scene(self, name):
        if self.current_scene:
            self.current_scene.exit()
        
        self.current_scene = self.scenes.get(name)
        
        if self.current_scene:
            self.game.scene = self.current_scene
            self.current_scene.enter()