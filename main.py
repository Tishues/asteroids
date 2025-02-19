# Asteroids remake for boot.dev course on 'Object Oriented Programming' + some of my own additions.
import pygame
from sys import exit
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid, AsteroidMedium, AsteroidSmall
from shot import Shot
from functions import smallfont, smallestfont, gameover_menu, pause_menu_labels, p_for_pause, esc_for_menu

def main():
    pygame.init() # Pygame Initialized.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Setting the game window.
    pygame.display.set_caption("Asteroids") # Renaming the window title.
    clock = pygame.time.Clock() # A clock for tickrate and timing.
    dt = 0
    total_score = 0 # Total score tallying all asteroids shot.
    player_lives = 1 # Starting lives for player, displayed as ARMOR in game.
    regain_lives_check = 0 # Used to check if the player has enough kills to regain a life.
    background = pygame.image.load("images/asteroids_background.jpg") #Background image.

        
    def pause_menu(): # Pause menu with conintue/restart/quit options.
        p_for_pause()
        pause_menu_labels() # calling labels from functions.py
        text = smallfont.render('Paused', 13, (0, 0, 0))
        textx = SCREEN_WIDTH / 2 - text.get_width() / 2
        texty = 50
        textx_size = text.get_width()
        texty_size = text.get_height()
        pygame.draw.rect(screen, (255, 255, 255), ((textx - 5, texty - 5),
                                                (textx_size + 10, texty_size +
                                                10)))
        screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 50))

        pygame.display.flip()
        # PAUSE SCREEN MENU.
        in_main_menu = True
        while in_main_menu:
            clock.tick(0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_main_menu = False
                    pygame.display.quit()
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if x >= textx - 5 and x <= textx + textx_size + 5:
                        if y >= texty - 5 and y <= texty + texty_size + 5:
                            in_main_menu = False
                            break
                elif event.type == pygame.KEYDOWN: # Keys to interact with menu.
                    if event.key == pygame.K_y:  # Press Y or Enter to restart.
                        in_main_menu = False
                        break
                    if event.key == pygame.K_RETURN:
                        in_main_menu = False
                        break
                    if event.key == pygame.K_n: # Press N to quit game.
                        exit()
                    if event.key == pygame.K_ESCAPE:
                        in_main_menu = False
                        break
                    if event.key == pygame.K_p:
                        in_main_menu = False
                        break


    # Sprite groups.
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()  
    # Adding objects to sprite groups.
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidMedium.containers = (updatable, drawable, asteroids)
    AsteroidSmall.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    # Score to be displayed on screen while playing.  
    def current_score(): 
        text = smallfont.render(f"Score: {total_score}", 13, (255, 255, 255))
        screen.blit(text, ((SCREEN_WIDTH /2) - text.get_width() /2, 3))
        # current lives/shield displayed on screen while playing  
    def current_lives(): 
        text = smallestfont.render(f"SHIELD: {player_lives}", 13, (0, 255, 0))
        screen.blit(text, ((SCREEN_WIDTH /2) - text.get_width() /2, SCREEN_HEIGHT-23))
        # shield/lives recharching displayed in screen
    def recharging_lives(): 
        text = smallestfont.render(f"CHARGING.. {regain_lives_check}%", 13, (255, 0, 0))
        screen.blit(text, (((SCREEN_WIDTH /2) - text.get_width() /2), SCREEN_HEIGHT-23))


    # GAMELOOP
    while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN: # Press ESC to quit program quickly.
                    if event.key == pygame.K_ESCAPE:
                        pause_menu()
                    if event.key == pygame.K_p:
                        pause_menu()
                    if event.key == pygame.K_SPACE:
                        player.shoot()


            for sprite in updatable:
                sprite.update(dt)  # Updating everything in updatable group.


            for asteroid in asteroids.copy():
                # Lose a life/armor for each asteroid you crash into, when dead GAME OVER menu.
                if player.collisions(asteroid):
                    asteroid.kill()
                    player_lives -= 1
                    if player_lives == -1:
                        gameover_menu()   
                  
                for shot in shots.copy(): # Splits asteroids into smaller asteroids and deletes the shot.
                    if asteroid.collisions(shot) or shot.collisions(asteroid):
                        asteroid.split()
                        shot.kill()
                        total_score += 1
                        if player_lives == 0: # regain life only if lost life
                            if regain_lives_check < 100: # regain 1 life per 100 kills
                                regain_lives_check += 1
                            if regain_lives_check >= 100:
                                regain_lives_check = 0
                                if player_lives == 0:
                                    player_lives += 1


            pygame.Surface.fill(screen, (0,0,0))
            screen.blit(background, (0, 0)) # Background image applied.
            current_score() # Displays score on screen while playing.
            esc_for_menu() # Displays control for pause menu.
            if player_lives == 1:
                current_lives() # Displays players current amount of lives left.
            if player_lives == 0:
                recharging_lives() # Displays how many kills until armor is recharged.

            for sprite in drawable:
                sprite.draw(screen)  # Drawing ALL drawable objects.

            pygame.display.flip()

            dt = clock.tick(60) / 1000 # Tickrate.
              

if __name__ == "__main__":
    main()
