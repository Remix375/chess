import pygame
from ..Piece import Piece

class Roi(Piece):
    def __init__(self, color):
        super().__init__(color, "Roi")
