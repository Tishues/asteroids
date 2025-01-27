import pygame
import random
from constants import ASTEROID_MIN_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_MAX_RADIUS, ASTEROID_IMAGE, ASTEROID_MID_RADIUS
from circleshape import CircleShape

asteroid_big = pygame.transform.scale(ASTEROID_IMAGE, (125,125))
asteroid_med = pygame.transform.scale(ASTEROID_IMAGE, (75,75))
asteroid_sml = pygame.transform.scale(ASTEROID_IMAGE, (50,50))
def rotate_center(image, rect, angle):
    rotate_image = pygame.transform.rotate(image, angle)
    rotate_rect = rotate_image.get_rect(center=rect.center)
    return rotate_image, rotate_rect

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)
        
    def draw(self, screen):
        oldRect = asteroid_big.get_rect(center=(self.position.x, self.position.y))
        screen.blit(asteroid_big, (oldRect))
        #.blit(ASTEROID_IMAGE, (self.position.x, self.position.y))
        #pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

        # Asteroid cleanup as they leave the screen
        if self.position.x < - 70:
            Asteroid.kill(self)
        if self.position.x > SCREEN_WIDTH + 70:
            Asteroid.kill(self)
        if self.position.y < - 70:
            Asteroid.kill(self)
        if self.position.y > SCREEN_HEIGHT + 70:
            Asteroid.kill(self)

    # Splits asteroids into smaller asteroids
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        if self.radius <= ASTEROID_MAX_RADIUS:
            random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = AsteroidMedium(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = AsteroidMedium(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2

class AsteroidMedium(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)

    def draw(self, screen):
        oldRect = asteroid_med.get_rect(center=(self.position.x, self.position.y))
        screen.blit(asteroid_med, (oldRect))
        #.blit(ASTEROID_IMAGE, (self.position.x, self.position.y))
        #pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

        # Asteroid cleanup as they leave the screen
        if self.position.x < - 70:
            AsteroidMedium.kill(self)
        if self.position.x > SCREEN_WIDTH + 70:
            AsteroidMedium.kill(self)
        if self.position.y < - 70:
            AsteroidMedium.kill(self)
        if self.position.y > SCREEN_HEIGHT + 70:
            AsteroidMedium.kill(self)

    # Splits asteroids into smaller asteroids
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        if self.radius <= ASTEROID_MID_RADIUS:
            random_angle = random.uniform(20, 50)
            a = self.velocity.rotate(random_angle)
            b = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = AsteroidSmall(self.position.x, self.position.y, new_radius)
            asteroid.velocity = a * 1.2
            asteroid = AsteroidSmall(self.position.x, self.position.y, new_radius)
            asteroid.velocity = b * 1.2



class AsteroidSmall(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)

    def draw(self, screen):
        oldRect = asteroid_sml.get_rect(center=(self.position.x, self.position.y))
        screen.blit(asteroid_sml, (oldRect))
        #.blit(ASTEROID_IMAGE, (self.position.x, self.position.y))
        #pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

        # Asteroid cleanup as they leave the screen
        if self.position.x < - 70:
            AsteroidSmall.kill(self)
        if self.position.x > SCREEN_WIDTH + 70:
            AsteroidSmall.kill(self)
        if self.position.y < - 70:
            AsteroidSmall.kill(self)
        if self.position.y > SCREEN_HEIGHT + 70:
            AsteroidSmall.kill(self)

        # kills small asteroids
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return