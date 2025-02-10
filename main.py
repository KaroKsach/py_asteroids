import pygame
from pygame import Color
from constants import *
from player import Player
def main():
    pygame.init()

    player_init_x = SCREEN_WIDTH/2
    player_init_y = SCREEN_HEIGHT/2
    player = Player(player_init_x, player_init_y)



    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(Color(0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
    
if __name__ == "__main__":
    main()
