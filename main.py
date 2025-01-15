import pygame
from constants import *
from player import Player

def main():
        pygame.init
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        dt = 0
        

        print("Starting asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")

        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        Player.containers = (updatable, drawable)
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        print("Drawable Group Contents:", drawable)
        print("Updatable Group Contents:", updatable)

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
