import pygame
from ..Piece import Piece

class Dame(Piece):
    def __init__(self, color):
        super().__init__(color, "Dame")