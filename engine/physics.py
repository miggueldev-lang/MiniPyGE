class PhysicsBody:
    def __init__(self, entity, gravity=0.5, friction = 0.8 , max_speed=10):
        self.entity = entity
        self.gravity = gravity
        self.friction = friction
        self.max_speed = max_speed

        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0

        self.use_gravity = False

    def apply_force(self, fx, fy):
        self.ax += fx
        self.ay += fy

    def update_physics(self):
        if self.use_gravity:
            self.ay += self.gravity
        
        # aplicar aceleração à velocidade
        self.vx += self.ax
        self.vy += self.ay

        # limitar velocidade máxima
        self.vx = max(-self.max_speed, min(self.max_speed, self.vx))
        self.vy = max(-self.max_speed, min(self.max_speed, self.vy))

        # aplicar fricção somente no eixo X
        self.vx *= self.friction

        # mover o rect (Pygame usa rects)
        self.entity.rect.x += self.vx
        self.entity.rect.y += self.vy

        # sincronizar x,y
        self.entity.x = self.entity.rect.x
        self.entity.y = self.entity.rect.y

        # resetar aceleração
        self.ax = 0
        self.ay = 0
        

class PhysicsManager:
    def __init__(self):
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)
    
    def remove_body(self, body):
        if body in self.bodies:
            self.bodies.remove(body)
    
    def update(self):
        for body in self.bodies:
            body.update_physics()