from src.maps.base_map import BaseMap
from src.utils.colors import Colors
import pygame
import os
import sys


RES = WIDTH, HEIGHT = 601, 451
os.environ["SDL_VIDEO_WINDOW_POS"] = "2500, 200"


def main():
    pygame.init()
    pygame.display.set_caption('Evacuation Simulation')
    screen = pygame.display.set_mode(RES)
    clock = pygame.time.Clock()

    base_map = BaseMap(WIDTH, HEIGHT, 20)

    while True:
        screen.fill(Colors.WHITE.value)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

        base_map.show(screen)

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
