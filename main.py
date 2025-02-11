import pygame
from pygame import Color
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot
def main():
    pygame.init()

    player_init_x = SCREEN_WIDTH/2
    player_init_y = SCREEN_HEIGHT/2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(player_init_x, player_init_y)
    asteroid_field = AsteroidField()
    

    clock = pygame.time.Clock()
    dt = 60
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(Color(0, 0, 0))
        
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game Over!")
                exit(0)

        pygame.display.flip()
        dt = clock.tick(60)/1000
    
if __name__ == "__main__":
    main()
