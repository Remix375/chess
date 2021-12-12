import pygame
from ..Piece import Piece

class Roi(Piece):
    def __init__(self, color):
        super().__init__(color, "Roi")


    def can_move(self, pos, grid):
        possible = []
        x = pos[0]
        y = pos[1]

        for i in range(-1, 2):
            for k in range(-1, 2):
                current_x = x + i
                current_y = y + k
                if current_x <= 7 and current_x >= 0 and current_y <= 7 and current_y >= 0:
                    if grid[current_y][current_x] == "":
                        possible.append((current_x, current_y))
                    else:
                        if grid[current_y][current_x].color != self.color:
                            possible.append((current_x, current_y))
        return possible

