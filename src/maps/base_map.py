import pygame
import numpy as np
from src.utils.colors import Colors


class BaseMap:
    def __init__(self, width: int = 601, height: int = 451, tile: int = 20) -> None:
        self.cols = width // tile
        self.rows = height // tile
        self.tile = tile
        self.grid = np.zeros((self.rows, self.cols), dtype=int)
        self._set_walls()

    def _set_walls(self):
        self.grid[0][4:-4] = -1
        self.grid[-1][4:-4] = -1

        for i in range(self.rows):
            self.grid[i][4] = -1
            if i not in (10, 9):
                self.grid[i][-4] = -1

    def show(self, screen: pygame.Surface, thickness: int = 1) -> None:
        for row in range(self.rows):
            y = row * self.tile
            for col in range(self.cols):
                x = col * self.tile

                if self.grid[row][col] == -1:
                    pygame.draw.rect(screen, Colors.BLACK.value,
                                     (x, y, self.tile, self.tile))

                pygame.draw.line(screen, Colors.BLACK.value,
                                 (x, y), (x + self.tile, y), thickness)
                pygame.draw.line(screen, Colors.BLACK.value,
                                 (x + self.tile, y), (x + self.tile, y + self.tile), thickness)
                pygame.draw.line(screen, Colors.BLACK.value,
                                 (x + self.tile, y + self.tile), (x, y + self.tile), thickness)
                pygame.draw.line(screen, Colors.BLACK.value,
                                 (x, y + self.tile), (x, y), thickness)
