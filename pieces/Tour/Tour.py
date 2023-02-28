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
        y = pos[0]
        x = pos[1]+1
        while x <= 7:
            if grid[y][x] == "":
                possible.append((y,x))
                x += 1
            else:
                if grid[y][x].color != self.color:
                    possible.append((y,x))
                break
            
        #left
        y = pos[0]
        x = pos[1]-1
        while x >= 0:
            if grid[y][x] == "":
                possible.append((y,x))
                x -= 1
            else:
                if grid[y][x].color != self.color:
                    possible.append((y,x))
                break
            
        
        y = pos[0] + 1
        x = pos[1]
        #down
        while y <= 7:
            if grid[y][x] == "":
                possible.append((y,x))
                y += 1
            else:
                if grid[y][x].color != self.color:
                    possible.append((y,x))
                break



        y = pos[0] - 1
        x = pos[1]
        #up
        while y >= 0:
            if grid[y][x] == "":
                possible.append((y, x))
                y -= 1
            else:
                if grid[y][x].color != self.color:
                    possible.append((y, x))
                break

        return possible

    

#⊂(◉‿◉)つ