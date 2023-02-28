import pygame
from ..Piece import Piece

class Roi(Piece):
    def __init__(self, color):
        super().__init__(color, "Roi")


    #get all possible movement of the piece
    def can_move(self, pos, grid):
        possible = []
        x = pos[1]
        y = pos[0]

        #iterate over all neiughbouring cases
        for i in range(-1, 2):
            for k in range(-1, 2):
                current_x = x + i
                current_y = y + k
                #if in board
                if current_x <= 7 and current_x >= 0 and current_y <= 7 and current_y >= 0:
                    #if empty or if ennemie piece, we can go there
                    if grid[current_y][current_x] == "":
                        possible.append((current_y, current_x))
                    else:
                        if grid[current_y][current_x].color != self.color:
                            possible.append((current_y, current_x))
        return possible

#⊂(◉‿◉)つ