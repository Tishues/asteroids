#Asteroids remake for boot.dev course on 'Object Oriented Programming'.
import pygame
from sys import exit
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
from functions import smallfont, play_again


def main():
    pygame.init() #Pygame Initialized.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Setting the game window.
    clock = pygame.time.Clock() #A clock for tickrate and timing.
    dt = 0
    total_score = 0 #Total score tallying all asteroids shot.
    background = pygame.image.load("images/asteroids_background.jpg") #Background image.

    #Sprite groups.
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #Adding objects to sprite groups.
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True: #Gameloop.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN: #Press ESC to quit program quickly.
                    if event.key == pygame.K_ESCAPE:
                        exit()


            for sprite in updatable:
                sprite.update(dt)  # Updating everything in updatable group.


            for asteroid in asteroids.copy():
                # Game Over, Score and Restart.
                if player.collisions(asteroid):
                    #Total score end screen.
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
                    #Y/n end screen label.
                    text = smallfont.render('Y/N', 13, (0, 0, 0))
                    textx = SCREEN_WIDTH / 2 - text.get_width() / 2
                    texty = SCREEN_HEIGHT / 1.65 - text.get_height() / 2
                    textx_size = text.get_width()
                    texty_size = text.get_height()
                    pygame.draw.rect(screen, (255, 255, 255), ((textx - 5, texty - 5),
                                                                (textx_size + 10, texty_size +
                                                                10)))
                    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2,
                                        SCREEN_HEIGHT / 1.65 - text.get_height() / 2))
                    play_again() #Ends program and restarts a new one if player accepts.    
                  
                for shot in shots.copy(): #Splits asteroids into smaller asteroids and deletes the shot.
                    if asteroid.collisions(shot) or shot.collisions(asteroid):
                        asteroid.split()
                        shot.kill()
                        total_score += 1


            pygame.Surface.fill(screen, (0,0,0))
            screen.blit(background, (0, 0)) #Background image applied.

            for sprite in drawable:
                sprite.draw(screen)  #Drawing ALL drawable objects.

            pygame.display.flip()

            dt = clock.tick(60) / 1000 #Tickrate.
              

if __name__ == "__main__":
    main()
