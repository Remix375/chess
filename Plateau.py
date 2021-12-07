import pygame

from pieces.Pion.Pion import *
from pieces.Cavalier.Cavalier import *
from pieces.Fou.Fou import *
from pieces.Tour.Tour import *
from pieces.Roi.Roi import *
from pieces.Dame.Dame import *




class Plateau:
    def __init__(self, fenetre, plateau = [
        [Tour("black"), Cavalier("black"), Fou("black"), Dame("black"), Roi("black"), Fou("black"), Cavalier("black"), Tour("black")],
        [Pion("black"), Pion("black"), Pion("black"), Pion("black"), Pion("black"), Pion("black"), Pion("black"), Pion("black")],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        [Pion("white"), Pion("white"), Pion("white"), Pion("white"), Pion("white"), Pion("white"), Pion("white"), Pion("white")],
        [Tour("white"), Cavalier("white"), Fou("white"), Dame("white"), Roi("white"), Fou("white"), Cavalier("white"), Tour("white")]
    ]):

        self.plateau = plateau

        self.moving_piece = False
        self.original_moving_pos = ()

        self.x_window_size = fenetre.get_size()[0]
        self.y_window_size = fenetre.get_size()[1]

        self.size_x = self.x_window_size // 10
        self.size_y = self.y_window_size // 10


    def draw(self, fenetre):
        #iteration on all pieces on chessboard
        for line in range(8):
            for case in range(8):
                #get position on 8x8 board
                pos_x = self.size_x * (case+1)
                pos_y = self.size_y*(line+1)

                #create board square
                square = pygame.Rect(pos_x, pos_y, self.size_x, self.size_y)
                if ( line + case ) % 2 == 0:
                    pygame.draw.rect(fenetre, (100, 34, 53), square)
                else:
                    pygame.draw.rect(fenetre, (46, 225, 38), square)

                #place piece on case if it is ther
                if self.plateau[line][case] and self.plateau[line][case] != self.moving_piece:
                    self.plateau[line][case].position(pos_x + self.size_x//2, pos_y + self.size_y//2)
                    self.plateau[line][case].draw(fenetre)

        #draw piece that we are moving
        if self.moving_piece:
            self.moving_piece.draw(fenetre)
        
        #self.plateau[0][0].draw(fenetre, 100, 100)


    #pick piece up to move it
    def take_piece(self):
        pos = pygame.mouse.get_pos()

        square = pos[0] // self.size_x - 1, pos[1] // self.size_y - 1 
        if self.plateau[square[1]][square[0]]:
            self.moving_piece = self.plateau[square[1]][square[0]]
            self.original_moving_pos = square
    
    #drop piece if grabbed
    def place_piece(self):
        pos = pygame.mouse.get_pos()

        square = pos[0] // self.size_x - 1, pos[1] // self.size_y - 1 


        if square[0] <= 7 and square[0] >= 0 and square[1] <= 7 and square[1] >= 0 and self.moving_piece:
            #if self.moving_piece.can_move(self.original_moving_pos, square, self.plateau):
            self.plateau[self.original_moving_pos[1]][self.original_moving_pos[0]] = ""
            self.plateau[square[1]][square[0]] = self.moving_piece
            

        self.moving_piece = False

    #move piece when grabbed
    def move_piece(self, movement):
        if self.moving_piece:
            self.moving_piece.move(movement)


        

    def __str__(self):
        ret = ""

        for line in self.plateau:
            for case in line:
                ret += case

        return ret




#⊂(◉‿◉)つ