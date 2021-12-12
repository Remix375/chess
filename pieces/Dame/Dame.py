import pygame
from ..Piece import Piece

class Dame(Piece):
    def __init__(self, color):
        super().__init__(color, "Dame")



    #get all possible moves of the piece
    #movement method
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



            
        #top-right
        x = pos[0] + 1
        y = pos[1] - 1
        while x <= 7 and y >= 0:
            if grid[y][x] == "":
                possible.append((x,y))
                x += 1
                y -= 1
            else:
                if grid[y][x].color != self.color:
                    possible.append((x,y))
                break
            
        #bottom-right
        x = pos[0] + 1
        y = pos[1] + 1
        while x <= 7 and y <= 7:
            if grid[y][x] == "":
                possible.append((x,y))
                x += 1
                y += 1
            else:
                if grid[y][x].color != self.color:
                    possible.append((x,y))
                break
            
        #top-left
        x = pos[0] - 1
        y = pos[1] - 1
        while y >= 0 and x >= 0:
            if grid[y][x] == "":
                possible.append((x,y))
                x -= 1
                y -= 1
            else:
                if grid[y][x].color != self.color:
                    possible.append((x,y))
                break


        #bottom-left
        x = pos[0] - 1
        y = pos[1] + 1
        while y <= 7 and x >= 0:
            if grid[y][x] == "":
                possible.append((x,y))
                x -= 1
                y += 1
            else:
                if grid[y][x].color != self.color:
                    possible.append((x,y))
                break

        return possible