import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self, self.containers)
        super().__init__(position[0], position[1], SHOT_RADIUS)
        self.velocity = pygame.math.Vector2(0, 0)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)