import pygame
from ..Piece import Piece


class Tour(Piece):
    def __init__(self, color):
        super().__init__(color, "Tour")

    #get all possible moves of the piece
    def can_move(self, pos, grid):
        possible = []

        #if empty or if ennemie piece we can go

        #right
        x = pos[0]+1
        y = pos[1]
        while x <= 7:
            if grid[y][x] == "":
                possible.append((x,y))
                x += 1
            else:
                if grid[y][x].color != self.color:
                    possible.append((x,y))
                break
            
        #left
        x = pos[0]-1
        y = pos[1]
        while x >= 0:
            if grid[y][x] == "":
                possible.append((x,y))
                x -= 1
            else:
                if grid[y][x].color != self.color:
                    possible.append((x,y))
                break
            
        
        x = pos[0]
        y = pos[1] + 1
        #down
        while y <= 7:
            if grid[y][x] == "":
                possible.append((x,y))
                y += 1
            else:
                if grid[y][x].color != self.color:
                    possible.append((x,y))
                break



        x = pos[0]
        y = pos[1] - 1
        #up
        while y >= 0:
            if grid[y][x] == "":
                possible.append((x,y))
                y -= 1
            else:
                if grid[y][x].color != self.color:
                    possible.append((x,y))
                break

        return possible

    


