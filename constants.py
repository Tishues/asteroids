import pygame
pygame.init()
display_info = pygame.display.Info()
SCREEN_WIDTH = display_info.current_w - 15
SCREEN_HEIGHT = display_info.current_h - 100

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200
PLAYER_SHOOT_SPEED = 500
SHOT_RADIUS = 5
PLAYER_SHOOT_COOLDOWN = 0.3
