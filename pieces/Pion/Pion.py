import pygame
from ..Piece import Piece

class Pion(Piece):
    def __init__(self, color):
        super().__init__(color, "Pion")


    def can_move(self, pos_depart, tab):
        possible = []
        if self.color == "white":
            if pos_depart[0] == 7:
                return []
            if tab[pos_depart[0] - 1][pos_depart[1]] == "":
                possible.append((pos_depart[0] - 1, pos_depart[1]))
                if pos_depart[0] == 6 and tab[pos_depart[0] - 2][pos_depart[1]] == "":
                    possible.append((pos_depart[0] - 2, pos_depart[1]))

            if pos_depart[1] + 1 <= 7 and tab[pos_depart[0] - 1][pos_depart[1]+1] != "":
                if tab[pos_depart[0] - 1][pos_depart[1]+1].color == "black":
                    possible.append((pos_depart[0] - 1 ,pos_depart[1]+1))

            if pos_depart[1] - 1 >= 0 and tab[pos_depart[0] - 1][pos_depart[1]-1] != "":    
                if tab[pos_depart[0] - 1][pos_depart[1]-1].color == "black":
                    possible.append((pos_depart[0] - 1 ,pos_depart[1] - 1)) 



        if self.color == "black":
            if pos_depart[0] == 0:
                return []
            if tab[pos_depart[0] + 1][pos_depart[1]] == "":
                possible.append((pos_depart[0] + 1, pos_depart[1]))
                if pos_depart[0] == 1 and tab[pos_depart[0] + 2][pos_depart[1]] == "":
                    possible.append((pos_depart[0] + 2, pos_depart[1]))

            if pos_depart[1] + 1 <= 7 and tab[pos_depart[0] + 1][pos_depart[1]+1] != "":
                if tab[pos_depart[0] + 1][pos_depart[1]+1].color == "white":
                    possible.append((pos_depart[0] + 1 ,pos_depart[1]+1))

            if pos_depart[1] - 1 >= 0 and tab[pos_depart[0] + 1][pos_depart[1]-1] != "":    
                if tab[pos_depart[0] + 1][pos_depart[1]-1].color == "white":
                    possible.append((pos_depart[0] + 1 ,pos_depart[1] - 1)) 
        return possible   

    


#⊂(◉‿◉)つ