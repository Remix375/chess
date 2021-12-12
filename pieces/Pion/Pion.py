import pygame
from ..Piece import Piece

class Pion(Piece):
    def __init__(self, color):
        super().__init__(color, "Pion")


    #methode de mouvement a faire
    def can_move(self, pos, grid):
        possible = []
        for k in grid:
            for i in k:
                possible.append((i, k))

        return possible