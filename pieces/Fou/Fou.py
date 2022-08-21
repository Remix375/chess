import pygame
from ..Piece import Piece

class Fou(Piece):
    def __init__(self, color):
        super().__init__(color, "Fou")



    #get all possible moves of the piece
    def can_move(self, pos, grid):
        possible = []

        #if empty or if ennemie piece we can go

        #top-right
        x = pos[1] + 1
        y = pos[0] - 1
        while x <= 7 and y >= 0:
            if grid[y][x] == "":
                possible.append((y,x))
                x += 1
                y -= 1
            else:
                if grid[y][x].color != self.color:
                    possible.append((y,x))
                break
            
        #bottom-right
        x = pos[1] + 1
        y = pos[0] + 1
        while x <= 7 and y <= 7:
            if grid[y][x] == "":
                possible.append((y,x))
                x += 1
                y += 1
            else:
                if grid[y][x].color != self.color:
                    possible.append((y,x))
                break
            
        #top-left
        x = pos[1] - 1
        y = pos[0] - 1
        while y >= 0 and x >= 0:
            if grid[y][x] == "":
                possible.append((y,x))
                x -= 1
                y -= 1
            else:
                if grid[y][x].color != self.color:
                    possible.append((y,x))
                break


        #bottom-left
        x = pos[1] - 1
        y = pos[0] + 1
        while y <= 7 and x >= 0:
            if grid[y][x] == "":
                possible.append((y,x))
                x -= 1
                y += 1
            else:
                if grid[y][x].color != self.color:
                    possible.append((y,x))
                break

        return possible