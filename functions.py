# Add functions here to be used in main.py to keep it clean and easy to read
import os
import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init() # Pygame initialized for menu/restart function
window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # Sets a screen window for the menu/restart function
clock = pygame.time.Clock() # A clock for menu/restart function
bigfont = pygame.font.Font(None, 80) # A large font
smallfont = pygame.font.Font(None, 45) # A smaller font
smallestfont = pygame.font.Font(None, 30) # Smallest font

    # Exits the program and starts a new one
def restart_program():
    python = sys.executable
    os.execv(python, [python] + sys.argv)

    # Menu for gameover with restart/quit options
def gameover_menu():
    game_over()
    yes_or_no()
    text = smallfont.render('Restart game?', 13, (0, 0, 0))
    textx = SCREEN_WIDTH / 2 - text.get_width() / 2
    texty = SCREEN_HEIGHT / 2 - text.get_height() / 2
    textx_size = text.get_width()
    texty_size = text.get_height()
    pygame.draw.rect(window, (255, 255, 255), ((textx - 5, texty - 5),
                                                (textx_size + 10, texty_size +
                                                10)))
    window.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2,
                        SCREEN_HEIGHT / 2 - text.get_height() / 2))

    pygame.display.flip()
    # Gameover menu
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
            elif event.type == pygame.KEYDOWN: # Keys to interact with menu
                if event.key == pygame.K_y:  # Press Y or Enter to restart
                    restart_program()
                if event.key == pygame.K_RETURN:
                    restart_program()
                if event.key == pygame.K_n: # Press N or ESC to quit game
                    sys.exit()
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

def yes_or_no(): # Y/N end screen label
    text = smallfont.render('Yes(y) / No(n)', 13, (255, 255, 255))
    window.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2,
                        (SCREEN_HEIGHT / 1.65 - text.get_height() / 2)-20))
    

def game_over(): # Displays 'game over' title on end screen
        text = bigfont.render(f"GAME OVER", 13, (255, 255, 255))
        window.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 50))

def pause_menu_labels():  # Lables for pause screen
    def yes_y():
        text = smallfont.render(f"Yes (y)", 13, (255, 255, 255))
        window.blit(text, ((SCREEN_WIDTH / 2 - text.get_width()) - 100 / 2, 545))
    def no_n():
        text = smallfont.render(f"No (n)", 13, (255, 255, 255))
        window.blit(text, ((SCREEN_WIDTH / 2 - text.get_width()) + 300 / 2, 545))
    def carry_on():
        text = bigfont.render(f"Continue?", 13, (255, 255, 255))
        window.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 475))
    carry_on()
    no_n()
    yes_y()


# Controls displayed on screen
def p_for_pause(): # pause 
        text = smallestfont.render(f"Menu", 13, (180, 180, 180))
        window.blit(text, ((SCREEN_WIDTH /2) - text.get_width()/2, (SCREEN_HEIGHT /2)-210))
        def w_for_forward(): # forward
            text = smallestfont.render(f"W: Thrust Forward", 13, (180, 180, 180))
            window.blit(text, ((SCREEN_WIDTH /2) - text.get_width()/2, (SCREEN_HEIGHT /1.25)-25))
        def a_for_left(): # left
            text = smallestfont.render(f"A: Turn Left", 13, (180, 180, 180))
            window.blit(text, ((SCREEN_WIDTH /2) - text.get_width()/2, (SCREEN_HEIGHT /1.25)-50))
        def d_for_right(): # right
            text = smallestfont.render(f"D: Turn Right", 13, (180, 180, 180))
            window.blit(text, ((SCREEN_WIDTH /2) - text.get_width()/2, (SCREEN_HEIGHT /1.25)-75))
        def space_for_shoot(): # shoot
            text = smallestfont.render(f"SPACE: Shoot", 13, (180, 180, 180))
            window.blit(text, ((SCREEN_WIDTH /2) - text.get_width()/2, (SCREEN_HEIGHT /1.25)-100))
        w_for_forward()
        a_for_left()
        d_for_right()
        space_for_shoot()


def esc_for_menu(): # shoot
    text = smallestfont.render(f"ESC: Menu", 13, (180, 180, 180))
    window.blit(text, (3, SCREEN_HEIGHT - 23))