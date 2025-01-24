#Add functions here to be used in main.py to keep it clean and easy to read.
import os
import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init() #Pygame initialized for menu/restart function.
window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #Sets a screen window for the menu/restart function.
clock = pygame.time.Clock() #A clock for menu/restart function.
bigfont = pygame.font.Font(None, 80) #A large font.
smallfont = pygame.font.Font(None, 45) #A smaller font.

    #Exits the program and starts a new one.
def restart_program():
    python = sys.executable
    os.execv(python, [python] + sys.argv)

    #Menu function with button to restart the program on game-over.
def play_again():
    text = bigfont.render('Play again?', 13, (0, 0, 0))
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
    #Gameover menu.
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
            elif event.type == pygame.KEYDOWN: #Keys to interact with menu.
                if event.key == pygame.K_y:  #Press Y, Space or Enter to restart.
                    restart_program()
                if event.key == pygame.K_SPACE:
                    restart_program()
                if event.key == pygame.K_RETURN:
                    restart_program()
                if event.key == pygame.K_n: #Press N or ESC to quit game.
                    sys.exit()
                if event.key == pygame.K_ESCAPE:
                    sys.exit()