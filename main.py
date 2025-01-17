import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
        pygame.init
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        dt = 0
        

        print("Starting asteroids!")

        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        
    
        Player.containers = (updatable, drawable)
        Asteroid.containers = (updatable, drawable, asteroids)
        AsteroidField.containers = (updatable,)

        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        asteroid_field = AsteroidField()

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                for sprite in updatable:
                    sprite.update(dt)  # Call `update` on everything in the updatable group
                pygame.Surface.fill(screen, (0,0,0))
                for sprite in drawable:
                    sprite.draw(screen)  # Use YOUR `draw()` method for all drawable objects
                pygame.display.flip()
                dt = clock.tick(60) / 1000
              

if __name__ == "__main__":
    main()
