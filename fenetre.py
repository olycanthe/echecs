import pygame

def taille_echecs(fenetre_x, fenetre_y):
    pygame.display.set_caption('echecs'  )  # Nom de la fenêtre
    return pygame.display.set_mode((fenetre_x, fenetre_y))