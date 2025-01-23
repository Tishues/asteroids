import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
from functions import *
pygame.init()
screen = pygame.display.set_mode((600,400))
bigfont = pygame.font.Font(None, 80)
smallfont = pygame.font.Font(None, 45)

def play_again():
    text = bigfont.render('Play again?', 13, (0, 0, 0))
    textx = SCREEN_WIDTH / 2 - text.get_width() / 2
    texty = SCREEN_HEIGHT / 2 - text.get_height() / 2
    textx_size = text.get_width()
    texty_size = text.get_height()
    pygame.draw.rect(screen, (255, 255, 255), ((textx - 5, texty - 5),
                                               (textx_size + 10, texty_size +
                                                10)))

    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2,
                       SCREEN_HEIGHT / 2 - text.get_height() / 2))

    clock = pygame.time.Clock()
    pygame.display.flip()
    in_main_menu = True
    while in_main_menu:
        clock.tick(50)
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
                        restart_program()



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
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if button:
                            pygame.quit()
                    
                for sprite in updatable:
                    sprite.update(dt)  # Calls `update` on everything in the updatable group

                for asteroid in asteroids.copy():
                    if player.collisions(asteroid):
                        print(f"Game ended. Your score was: {total_score}")
                        play_again()
                        #Label(window, text=f"Score: {total_score}").pack()
                        #Button(window, text="RESTART", command=restart_program).pack()
                        #Button(window, text="QUIT", command=exit).pack()
                        #window.protocol("WM_DELETE_WINDOW", on_closing)
                        #window.mainloop()
                        #button test: if button:
                            #pygame.draw.rect(screen,color_light,[SCREEN_WIDTH/2,SCREEN_HEIGHT/2,140,40])
                        #else:
                            #pygame.draw.rect(screen,color_dark,[SCREEN_WIDTH/2,SCREEN_HEIGHT/2,140,40])
                        #screen.blit(text , (SCREEN_WIDTH/2+50, SCREEN_HEIGHT/2))
                        #pygame.display.update()
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
