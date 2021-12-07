import pygame
from ..Piece import Piece

class Pion(Piece):
    def __init__(self, color):
        super().__init__(color, "Pion")


    #returns true if can move to the square:
    #would be better to return all cases where can move --> to change
    def can_move(self, pos_depart, pos_arrivee, tab):
        if self.color == "white":
            if (pos_arrivee[1] - pos_depart[1]) < -2:
                return False

            elif pos_arrivee[1] - pos_depart[1] == -2:
                if pos_depart[1] != 6:
                    return False
                if pos_arrivee[0] != pos_depart[0]:
                    return False
                elif tab[pos_depart[1]-1][pos_depart[0]] != "" or tab[pos_arrivee[1]][pos_arrivee[0]] != "":
                    return False

            elif pos_arrivee[1] - pos_depart[1] == -1:
                if abs(pos_arrivee[0] - pos_depart[0]) > 1:
                    return False
                elif pos_arrivee[0] != pos_depart[0]:
                    if tab[pos_arrivee[1]][pos_arrivee[0]] == "":
                        return False
                    elif tab[pos_arrivee[1]][pos_arrivee[0]].color == self.color:
                        return False
                elif tab[pos_arrivee[1]][pos_arrivee[0]] != "":
                    return False
            else:
                return False




        if self.color == "black":
            if (pos_arrivee[1] - pos_depart[1]) < 2:
                return False

            elif pos_arrivee[1] - pos_depart[1] == 2:
                if pos_depart[1] != 1:
                    return False
                if pos_arrivee[0] != pos_depart[0]:
                    return False
                elif tab[pos_depart[1]+1][pos_depart[0]] != "" or tab[pos_arrivee[1]][pos_arrivee[0]] != "":
                    return False

            elif pos_arrivee[1] - pos_depart[1] == 1:
                print("h")
                if abs(pos_arrivee[0] - pos_depart[0]) > 1:
                    return False
                elif pos_arrivee[0] != pos_depart[0]:
                    if tab[pos_arrivee[1]][pos_arrivee[0]] == "":
                        return False
                    elif tab[pos_arrivee[1]][pos_arrivee[0]].color == self.color:
                        return False
                elif tab[pos_arrivee[1]][pos_arrivee[0]] != "":
                    return False
                print("h")
            else:
                return False




        return True
