from constants import *
from circleshape import *
from shot import *
import pygame

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        return pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)
    
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        pass

    def shoot(self):
        shot = Shot(self.position.x,self.position.y)
        shot.velocity = (pygame.Vector2(0,1).rotate(self.rotation))
        shot.velocity *= PLAYER_SHOOT_SPEED
        pass

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation -= dt*PLAYER_TURN_SPEED

        if keys[pygame.K_d]:
            self.rotation += dt*PLAYER_TURN_SPEED

        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            if self.timer > 0:
                self.timer -= dt
            else:
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN
        pass


