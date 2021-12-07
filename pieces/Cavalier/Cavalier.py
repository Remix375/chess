import pygame
from ..Piece import Piece

class Cavalier(Piece):
    def __init__(self, color):
        super().__init__(color, "Cavalier")