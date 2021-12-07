import pygame
from ..Piece import Piece

class Tour(Piece):
    def __init__(self, color):
        super().__init__(color, "Tour")


    def can_move(self, pos_depart, pos_arrivee, tab):
    
        if pos_depart[0] == pos_arrivee[0]:
            for k in range(pos_depart[1]+1, pos_arrivee[1]):
                if tab[pos_depart[0]][k] != "":
                    return False
        
        if pos_depart[1] == pos_arrivee[1]:
            for k in range(pos_depart[0], pos_arrivee[0]):
                if tab[k][pos_depart[1]] != "":
                    return False

        return False