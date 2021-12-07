import pygame
from ..Piece import Piece

class Tour(Piece):
    def __init__(self, color):
        super().__init__(color, "Tour")

    #get all possible moves of the piece
    def can_move(self, pos, grid):
        possible = []

        #right
        x = pos[0]+1
        y = pos[1]
        while x <= 7:
            if grid[y][x] == "":
                possible.append((x,y))
                x += 1
            else:
                break
            
        #left
        x = pos[0]-1
        y = pos[1]
        while x >= 0:
            if grid[y][x] == "":
                possible.append((x,y))
                x -= 1
            else:
                break
            
        
        x = pos[0]
        y = pos[1] + 1
        #down
        while y <= 7:
            if grid[y][x] == "":
                possible.append((x,y))
                y += 1
            else:
                break



        x = pos[0]
        y = pos[1] - 1
        #up
        while y >= 0:
            if grid[y][x] == "":
                possible.append((x,y))
                y -= 1
            else:
                break

        return possible