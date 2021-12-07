import pygame

class Piece:
    def __init__(self, color, piece):
        if color == "white":
            self.image = pygame.image.load("./pieces/{}/{}_b.png".format(piece, piece))
        else:
            self.image = pygame.image.load("./pieces/{}/{}_n.png".format(piece, piece))

        self.rect = self.image.get_rect()
        self.piece = piece

        self.color = color

    #change position of piece
    def position(self, pos_x, pos_y):
        self.rect.center = pos_x, pos_y

    #draw piece
    def draw(self, fenetre):
        fenetre.blit(self.image, self.rect)

    #move piece when picked up
    def move(self, movement):
        self.rect.move_ip(movement)


    def __str__(self):
        return self.piece