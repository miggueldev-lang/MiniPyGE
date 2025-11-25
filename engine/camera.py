class Camera:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0

        self.viewport_width = width
        self.viewport_height = height

        self.target = None
        self.smooth = 0.15

        self.world_width = None
        self.world_height = None

        self.follow_x = True
        self.follow_y = True
    
    def set_world_bounds(self, width, height):
        self.world_width = width
        self.world_height = height

    def follow(self, entity):
        self.target = entity
    
    def update(self):
        """ATUALIZAR POSIÇÃO DA CAMERA BASEADA NO ALVO"""
        if not self.target:
            return
        
        target_x = self.target.rect.centerx - self.viewport_width // 2
        target_y = self.target.rect.centery - self.viewport_height // 2

        # Seguir eixo condicional
        if not self.follow_x:
            target_x = self.x
        if not self.follow_y:
            target_y = self.y
        
        # suavização
        self.x += (target_x - self.x) * self.smooth
        self.y += (target_y - self.y) * self.smooth

        # limitar pelo mundo
        if self.world_width is not None:
            self.x = max(0, min(self.x, self.world_width - self.viewport_width))

        if self.world_height is not None:
            self.y = max(0, min(self.y, self.world_height - self.viewport_height))

 
    def apply(self, rect):
        return rect.move(-self.x, -self.y)