import pygame, sys
import time

from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
from Plateau import *


hauteur, largeur = 1000, 1000
fenetre = pygame.display.set_mode((hauteur, largeur))
background = (100, 135, 110)

plateau = Plateau(fenetre)

continuer = True

while continuer:


    fenetre.fill(background)
    plateau.draw(fenetre)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

        elif event.type == MOUSEBUTTONDOWN:
            plateau.take_piece()

        elif event.type == MOUSEBUTTONUP:
            plateau.place_piece()

        elif event.type == MOUSEMOTION:
            plateau.move_piece(event.rel)


    pygame.display.update()
    time.sleep(0.001)


pygame.display.quit()

sys.exit()











#⊂(◉‿◉)つ