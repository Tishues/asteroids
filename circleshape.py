import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        pass               
        # sub-classes must override
        
    def collisions(self, other_shape):
        r1 = self.radius
        r2 = other_shape.radius
        p1 = self.position
        p2 = other_shape.position
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        distance = (dx * dx + dy * dy) ** 0.5
        should_collide = distance <= (r1 + r2)
        return should_collide