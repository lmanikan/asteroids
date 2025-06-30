from constants import *
from circleshape import *
import pygame
import random


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen,(255,255,255),self.position,
                                  radius=self.radius,width=2)
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        else:
            random_angle = random.uniform(20,50)
            asteroid1 = Asteroid(self.position.x,self.position.y,
                                 self.radius - ASTEROID_MIN_RADIUS)
            asteroid1.velocity = (self.velocity.rotate(random_angle))*1.2

            asteroid2 = Asteroid(self.position.x,self.position.y,
                                 self.radius-ASTEROID_MIN_RADIUS)
            asteroid2.velocity = (self.velocity.rotate(-random_angle))*1.2
        pass

    def update(self, dt):
        self.position += self.velocity * dt
        
