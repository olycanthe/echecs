import pygame
from pygame import image

class Piece(): # sprite element non static pas comme un decor

    def __init__(self,fenetre_x, fenetre_y,fen):
        self.fenetre_x = fenetre_x #Largeur de la fenêtre
        self.fenetre_y = fenetre_y #Longueur de la fenêtre
        self.fen = fen

    def creation_piece(self, png):
        image = pygame.image.load(png)  # va chercher l'image avec les pieces d'echecs
        return pygame.transform.scale(image, (int(self.fenetre_x/8), int(self.fenetre_x/8)))

    def roi(self):
        roi_blanc = self.creation_piece('png/Chess_klt60.png')
        roi_noir = self.creation_piece('png/Chess_kdt60.png')

        self.fen.blit(roi_blanc, (self.fenetre_x/8*4, self.fenetre_y / 8 * 7))
        self.fen.blit(roi_noir, (self.fenetre_x/8*4, 0))

    def reine(self):
        reine_blanche = self.creation_piece('png/Chess_qlt60.png')
        reine_noire = self.creation_piece('png/Chess_qdt60.png')

        self.fen.blit(reine_blanche, (self.fenetre_x/8*3, self.fenetre_y / 8 * 7))
        self.fen.blit(reine_noire, (self.fenetre_x/8*3, 0))

    def cavalier(self):
        cavalier_blanc = self.creation_piece('png/Chess_nlt60.png')
        cavalier_noir = self.creation_piece('png/Chess_ndt60.png')

        self.fen.blit(cavalier_blanc, (self.fenetre_x/8*6, self.fenetre_y/8*7))
        self.fen.blit(cavalier_blanc, (self.fenetre_x/8, self.fenetre_y/8*7))
        self.fen.blit(cavalier_noir, (self.fenetre_x/8*6, 0))
        self.fen.blit(cavalier_noir, (self.fenetre_x/8, 0))

    def tour(self):
        tour_blanche = self.creation_piece('png/Chess_rlt60.png')
        tour_noire = self.creation_piece('png/Chess_rdt60.png')

        self.fen.blit(tour_blanche, (0, self.fenetre_y/8*7))
        self.fen.blit(tour_blanche, (self.fenetre_x/8*7, self.fenetre_y/8*7))
        self.fen.blit(tour_noire, (0, 0))
        self.fen.blit(tour_noire, (self.fenetre_x/8*7, 0))

    def fou(self):
        fou_noir = self.creation_piece('png/Chess_bdt60.png')
        fou_blanc =  self.creation_piece('png/Chess_blt60.png')

        self.fen.blit(fou_blanc, (self.fenetre_x/8*2, self.fenetre_y/8*7))
        self.fen.blit(fou_blanc, (self.fenetre_x/8*5, self.fenetre_y/8*7))
        self.fen.blit(fou_noir, (self.fenetre_x/8*2, 0))
        self.fen.blit(fou_noir, (self.fenetre_x/8*5, 0))

    def pion(self):
        pion_noir = self.creation_piece('png/Chess_pdt60.png')
        pion_blanc =  self.creation_piece('png/Chess_plt60.png')

        for noir in range(8):
            self.fen.blit(pion_blanc, (self.fenetre_x/8*noir, self.fenetre_x/8*6))
            self.fen.blit(pion_noir, (self.fenetre_x/8*noir, self.fenetre_x/8*1))
