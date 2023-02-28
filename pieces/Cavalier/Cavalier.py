import pygame
from ..Piece import Piece

class Cavalier(Piece):
    def __init__(self, color):
        super().__init__(color, "Cavalier")


    #methode de mouvement a faire
    def can_move(self, pos, grid):
        possible = []

        x = pos[1]
        y = pos[0]

        for i in [-2, 2]:
            for k in [-1, 1]:
                if x + i >= 0 and x + i <= 7 and y+k >=0 and y+k <= 7:
                    if grid[y+k][x+i] == "" or grid[y+k][x+i].color != self.color: 
                        possible.append((y+k, x+i))
                if x+k >= 0 and x+k <= 7 and y+i >= 0 and y+i <=7:
                    if grid[y+i][x+k] == "" or grid[y+i][x+k].color != self.color:
                        possible.append((y+i, x+k))
        return possible