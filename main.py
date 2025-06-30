import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():

    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (updatable,drawable,asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable,drawable,shots)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    game_clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():         
            if event.type == pygame.QUIT:
                return
                   
        screen.fill("black")
        for object in drawable:
            object.draw(screen)        
        updatable.update(dt)


        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                return

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        dt = game_clock.tick(60)/1000
        

if __name__ == "__main__":
    main()