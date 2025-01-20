import pygame
from tkinter import Label, Button
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
from functions import *

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
                    
                for sprite in updatable:
                    sprite.update(dt)  # Calls `update` on everything in the updatable group

                for asteroid in asteroids.copy():
                    if player.collisions(asteroid):
                        print(f"Game ended. Your score was: {total_score}")
                        Label(window, text=f"Score: {total_score}").pack()
                        Button(window, text="RESTART", command=restart_program).pack()
                        Button(window, text="QUIT", command=exit).pack()
                        window.protocol("WM_DELETE_WINDOW", on_closing)
                        window.mainloop()
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
