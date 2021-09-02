import pygame
from structure import damier
from structure import curseur

pygame.init() 


# x et y doivent être égaux pour former un carré 
fenetre_x = 600 #Largeur de la fenêtre
fenetre_y = 600 #Longueur de la fenêtre

echecs = True # Initialisation de la boucle principale:
clock = pygame.time.Clock() # initialisation des FPS

dam = damier.Plateau(fenetre_x,fenetre_y) # appelle de la classe pour le damier
curse = curseur.Selecteur(fenetre_x,fenetre_y) # appelle de la classe pour le selecteur


while echecs == True:

    curse.input()
    dam.damier()
    curse.selecteur()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             echecs = False # Arret de la boucle principale et donc ferneture du jeu

    # Flip the display
    pygame.display.flip()
    clock.tick(10)

pygame.quit() # arrete le programme