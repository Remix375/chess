import pygame
from ..Piece import Piece

class Fou(Piece):
    def __init__(self, color):
        super().__init__(color, "Fou")