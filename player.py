import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

upsidedown_player = pygame.transform.rotate(PLAYER_IMAGE, 180)
person = pygame.transform.scale(upsidedown_player, (45,60))
rotated_person = person
def rotate_center(image, rect, angle):
    rotate_image = pygame.transform.rotate(image, angle)
    rotate_rect = rotate_image.get_rect(center=rect.center)
    return rotate_image, rotate_rect

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rotation =  0
        self.shoot_timer = 0
        
    # Defining the Triangle that will be drawn for the player
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    

    # Drawing the triangle as the player
    def draw(self, screen):
        oldRect = rotated_person.get_rect(center=(self.position.x, self.position.y))
        screen.blit(rotated_person, (oldRect))
        
        #pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # Used to rotate right or left with -
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    # Used to move forward or backward with -
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    # Playing shot direction, speed and cooldown.
    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position)
        shot.velocity = forward * PLAYER_SHOOT_SPEED

    # Update method to overide parent class
    def update(self, dt):
        global rotated_person
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()
        rotate = 0
        
        # Move the character around the screen.
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: # Rotating left
            self.rotate(-dt)
            rotated_person = pygame.transform.rotate(person, -self.rotation)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # Rotating right
            self.rotate(dt)
            rotated_person = pygame.transform.rotate(person, -self.rotation)
        if keys[pygame.K_w] or keys[pygame.K_UP]: #Move forward
            self.move(dt)
        #if keys[pygame.K_s] or keys[pygame.K_DOWN]: # Removed reverse to make game more challenging.
        #    self.move(-dt) # Delete # from the start of the lines to add it back.

        # Wrap around world for the player only.
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0