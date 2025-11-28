from engine.scene import Scene
from engine.entity import Entity, EntityManager
from engine.physics import PhysicsBody
import pygame

class TitleScene(Scene):
    def __init__(self, game, number=1, color=(30,30,30)):
        super().__init__(game)
        self.number = number
        self.color = color
        self.title_text = self.font.render(f"Title Scene {self.number}", True, (255, 255, 255))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                next_scene = self.number + 1 if self.number < 3 else 1
                colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
                self.game.change_scene(TitleScene(self.game, next_scene, colors[next_scene - 1]))
    
    def draw(self, screen):
        screen.fill(self.color)
        text_rect = self.title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(self.title_text, text_rect)

class InputTestScene(Scene):
    def __init__(self, game):
        super().__init__(game)

    def draw(self, screen):
        screen.fill((30,30,30))

        input = self.game.input

        lines = [
            f"Ultima tecla: {pygame.key.name(input.last_key) if input.last_key else 'Nenhuma'}",
            f"Teclas segurando: {[pygame.key.name(k) for k in input.key_states if input.key_states[k]]}",
            f"Pressionadas no frame: {[pygame.key.name(k) for k in input.key_pressed]}",
            f"Soltas no frame: {[pygame.key.name(k) for k in input.key_released]}"
        ]

        y = 80
        for line in lines:
            text_surface = self.font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (20, y))
            y += text_surface.get_height() + 40

class AssetsTestScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.assets = game.assets
        
        self.test_image = self.assets.load_image("example_image.png")
        self.test_image = self.game.pygame.transform.scale(self.test_image, (self.game.width //2 , self.game.height//2))
        self.test_sound = self.assets.load_sound("example_music.mp3")

    def enter(self):
        self.tocando = False
        pass  # Toca em loop

    def update(self, dt):
        input = self.game.input

        if input.is_key_pressed("jump") and not self.tocando:
            if self.test_sound:
                self.test_sound.play(-1)
                self.tocando = True
        elif input.is_key_held("cancel") and self.tocando:
            self.test_sound.stop()
            self.tocando = False
                

    def draw(self, screen):
        screen.fill((50, 50, 50))
        if self.test_image:
            screen.blit(self.test_image, (180, 150))

class FontTestScene(Scene):
    def enter(self):
        self.text = ""

        self.font = self.game.assets.font("knewave.ttf", 32)
        
        if self.font is None:
            print("❌ Erro ao carregar fonte!")
        else:
            print("✔ Fonte carregada com sucesso!")

    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:

                # apagar caractere
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                
                # quebra de linha
                elif event.key == pygame.K_RETURN:
                    self.text += "\n"

                # todas as outras teclas
                else:
                    self.text += event.unicode

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill(self.background_color)

        if self.font:
            y_offset = 0
            for line in self.text.split("\n"):
                rendered = self.font.render(line, True, (255,255,255))
                screen.blit(rendered, (50, 50 + y_offset))
                y_offset += rendered.get_height()

class EntityTestScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        from engine.entity import Entity, EntityManager

        self.entity_manager = EntityManager(game)
        for i in range(5):
            entity = Entity(game, x=50 + i*60, y=200)
            self.entity_manager.add_entity(entity)

    def update(self, dt):
        self.entity_manager.update(dt)

    def draw(self, screen):
        self.entity_manager.draw(screen)

class TestEntity(Scene):
    def enter(self):
        # Cria alguns quadrados na tela
        for i in range(5):
            e = self.entities.add_entity(Entity(self.game, x=50 + i*60, y=200))
            e.add_tag("box")

    def update(self, dt):
        super().update(dt)
    
    def draw(self, surface):
        surface.fill((20, 20, 20))
        super().draw(surface)

class TestHitboxes(Scene):
    def enter(self):
        # Cria 4 entidades com hitbox ligada
        for i in range(5):
            e = self.entities.add_entity(Entity(self.game, 60 + i * 80, 200))
            e.debug = True    # ativa hitbox
            e.add_tag("debug")
    
    def draw(self, surface):
        surface.fill((20, 20, 20))
        super().draw(surface)

class TestLayers(Scene):
    def enter(self):
        # camada 0 - fundo
        e1 = self.entities.add_entity(Entity(self.game, 50, 50, 200, 200, layer=0))
        e1.color = (80, 80, 250)
        e1.draw = lambda s: self.game.pygame.draw.rect(s, e1.color, e1.rect)

        # camada 1 - meio
        e2 = self.entities.add_entity(Entity(self.game, 80, 80, 200, 200, layer=1))
        e2.color = (250, 80, 80)
        e2.draw = lambda s: self.game.pygame.draw.rect(s, e2.color, e2.rect)

        # camada 2 - frente
        e3 = self.entities.add_entity(Entity(self.game, 110, 110, 200, 200, layer=2))
        e3.color = (80, 250, 80)
        e3.draw = lambda s: self.game.pygame.draw.rect(s, e3.color, e3.rect)

class CollisionTestScene(Scene):
    def enter(self):
        self.physics = self.game.physics
        self.player = self.entities.add_entity(Entity(self.game, 100, 100, 50, 50))
        self.player.color = (0, 200, 0)
        self.player.debug = True
        self.player.enable_physics(self.physics, gravity = 0)
        self.player.physics.use_gravity = False

        self.block = self.entities.add_entity(Entity(self.game, 300, 100, 100, 100))
        self.block.color = (200, 0, 0)

    def update(self, dt):
        input = self.game.input
        speed = 200 * dt
        self.entities.update(dt)

        self.physics.update()

        if input.is_key_held("move_right"): self.player.physics.apply_force(1,0)
        if input.is_key_held("move_left"): self.player.physics.apply_force(-1, 0)
        if input.is_key_held("move_up"): self.player.rect.y -= 5
        if input.is_key_held("move_down"): self.player.rect.y += 5

        collisions = self.entities.get_collisions(self.player)
        for entity in collisions:
            print("Colidiu com entidade!")
        
    def draw(self, screen):
        screen.fill((50, 50, 50))
        super().draw(screen)

class TestPhysicsAndCamera(Scene):
    def enter(self):
        self.physics = self.game.physics

        # Fundo azul
        self.background_color = (135, 206, 235)

        # Entidade que cai
        self.player = self.entities.add_entity(Entity(self.game, 100, 100, 50, 50))
        self.player.color = (0, 255, 0)
        self.player.debug = False

        # Ativando física
        self.player.enable_physics(self.physics, gravity=0.1)
        self.player.physics.use_gravity = True

        # Chão estático
        self.ground = self.entities.add_entity(Entity(self.game, 0, 500, 800, 100))
        self.ground.color = (139, 69, 19)
        self.ground.physics = PhysicsBody(self.ground)  # Sem gravidade, sem movimento
        self.on_ground = False

        # definindo o alvo da camera
        self.camera.follow(self.player)

    def update(self, dt):
        input = self.game.input
        # Atualiza entidades
        self.entities.update(dt)

        # Atualiza o sistema geral de física
        self.physics.update()

        # Atualiza a camera
        self.camera.update()

        # Verifica se o player está no chão
        self.on_ground = self.player.intersects(self.ground)
        # para de cair se estiver no chão
        if self.on_ground:
            self.player.physics.vy = 0
            self.player.rect.bottom = self.ground.rect.top

        # Permite pular se estiver no chão
        if self.on_ground and input.is_key_held("jump"):
            self.player.physics.vy = -5  # impulso para cima

        # movimentação para direita e para esquerda
        if input.is_key_held("move_right"): self.player.physics.apply_force(1, 0)
        if input.is_key_held("move_left"): self.player.physics.apply_force(-1, 0)

    def draw(self, screen):
        screen.fill(self.background_color)
        self.entities.draw(screen)

if __name__ == "__main__":
    import pygame
    from engine.core import Game

    pygame.init()
    game = Game()
    game.change_scene(AssetsTestScene(game))
    game.run()
    pygame.quit()
