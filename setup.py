import pygame
import color
import fenetre
from structure import damier
from structure import curseur
from pion import pion

pygame.init() 

# x et y doivent être égaux pour former un carré 
fenetre_x = 800 #Largeur de la fenêtre
fenetre_y = 800 #Longueur de la fenêtre

fen = fenetre.taille_echecs(fenetre_x, fenetre_y) # fonction pour créer la fenetre

echecs = True # Initialisation de la boucle principale:
clock = pygame.time.Clock() # initialisation des FPS

damier = damier.Plateau() # appelle de la classe pour le damier
curseur = curseur.Selecteur(fenetre_x,fenetre_y) # appelle de la classe pour le selecteur
piece = pion.Piece(fenetre_x,fenetre_y,fen)


while echecs == True:

    curseur.input()
    damier.damier(color.bleu(), color.blanc(),fenetre_x, fenetre_y, fen)
    curseur.selecteur(color.marron(), fen)
    piece.cavalier()
    piece.tour()
    piece.reine()
    piece.roi()
    piece.fou()
    piece.pion()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             echecs = False # Arret de la boucle principale et donc ferneture du jeu

    # Flip the display
    pygame.display.flip()
    clock.tick(10)

pygame.quit() # arrete le programme