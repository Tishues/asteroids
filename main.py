import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
from functions import play_again, smallfont

def main():
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        dt = 0
        total_score = 0
        print("Starting asteroids!")

        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()
    
        Player.containers = (updatable, drawable)
        Asteroid.containers = (updatable, drawable, asteroids)
        AsteroidField.containers = (updatable,)
        Shot.containers = (updatable, drawable, shots)

        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        asteroid_field = AsteroidField()

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                
                mouse = pygame.mouse.get_pos()
                    
                for sprite in updatable:
                    sprite.update(dt)  # Calls `update` on everything in the updatable group

                for asteroid in asteroids.copy():
                    if player.collisions(asteroid):
                        text = smallfont.render(f"Score: {total_score}", 13, (0, 0, 0))
                        textx = SCREEN_WIDTH / 2 - text.get_width() / 2
                        texty = SCREEN_HEIGHT / 3 - text.get_height() / 2
                        textx_size = text.get_width()
                        texty_size = text.get_height()
                        pygame.draw.rect(screen, (255, 255, 255), ((textx - 5, texty - 5),
                                                (textx_size + 10, texty_size +
                                                10)))

                        screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2,
                                                    SCREEN_HEIGHT / 3 - text.get_height() / 2))
                        play_again()

                    for shot in shots.copy():
                        if asteroid.collisions(shot) or shot.collisions(asteroid):
                            asteroid.split()
                            shot.kill()
                            total_score += 1

                pygame.Surface.fill(screen, (0,0,0))

                for sprite in drawable:
                    sprite.draw(screen)  # Uses `draw()` method for all drawable objects

                pygame.display.flip()

                dt = clock.tick(60) / 1000
              

if __name__ == "__main__":
    main()
