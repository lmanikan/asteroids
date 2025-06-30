from constants import *
from circleshape import *
import pygame

class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y,SHOT_RADIUS)

    def draw(self, screen):
        return pygame.draw.circle(screen,(255,255,255),self.position,
                                  radius=self.radius,width=2)
    
    def update(self, dt):
        self.position += self.velocity*dt