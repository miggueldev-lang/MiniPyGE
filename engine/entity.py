class Entity:
    def __init__(self, game, x=0, y=0, w=32, h=32, layer = 1):
        self.game = game
        self.x = x
        self.y = y

        self.width = w
        self.height = h

        self.alive = True
        self.visible = True

        self.rect = game.pygame.Rect(self.x, self.y, self.width, self.height)

        self.hitbox = self.rect.copy()
        self.debug = False

        self.tags = set()

        self.layer = layer

        self.color = (0, 155, 0)

        self.physics = None
    
    def enable_physics(self, system, **kwargs):
        from engine.physics import PhysicsBody

        self.physics = PhysicsBody(self, **kwargs)
        system.add_body(self.physics)

    def intersects(self, other):
        return self.hitbox.colliderect(other.hitbox)

    def update(self, dt):
        # atualiza a fisica das entidades
        if self.physics:
            self.physics.update_physics()

        # sincroniza o rect com a nova posição
        self.rect.topleft = (self.x, self.y)
        # hitbox que sempre é carregada em cima do rect
        self.hitbox.topleft = self.rect.topleft

    def draw(self, screen):
        if self.visible:
            cam_rect = self.game.scene.camera.apply(self.rect)
            self.game.pygame.draw.rect(screen, self.color, cam_rect)

        if self.debug:
            cam_rect = self.game.scene.camera.apply(self.hitbox)
            pygame = self.game.pygame
            pygame.draw.rect(screen, (255, 0, 0), cam_rect, 3)
    
    def add_tag(self, tag):
        self.tags.add(tag)

    def remove_tag(self, tag):
        self.tags.discard(tag)
    
    def has_tag(self, tag):
        return tag in self.tags
    
    def destroy(self):
        self.alive = False


class EntityManager:
    def __init__(self, game):
        self.game = game
        self.entities = []
    
    def add_entity(self, entity):
        self.entities.append(entity)
        return entity
    
    def remove_entity(self, entity):
        if entity in self.entities:
            self.entities.remove(entity)
            return True
        return False

    def get_collisions(self, entity):
        result = []
        for other in self.entities:
            if other is not entity and other.alive:
                if entity.rect.colliderect(other.rect):
                    result.append(other)
        
        return result

    def get_collisions_tag(self, entity, tag):
        result = []
        for other in self.entities:
            if other is not entity and other.alive and other.has_tag(tag):
                if entity.intersects(other):
                    result.append(other)

    def update(self, dt):
        for entity in self.entities:
            if entity.alive:
                entity.update(dt)
        
        self.entities = [e for e in self.entities if e.alive]

    def draw(self, screen):
        for entity in sorted(self.entities, key=lambda e: e.layer):
            if entity.visible:
                entity.draw(screen)

    def find_by_tag(self, tag):
        return [e for e in self.entities if e.has_tag(tag)]
    
    def find_one(self, tag):
        for e in self.entities:
            if e.has_tag(tag):
                return e
        return None