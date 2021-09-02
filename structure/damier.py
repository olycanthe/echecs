import pygame


class Plateau:

    def __init__(self,fenetre_x,fenetre_y):
        #Mise en place de la fenêtre et de sa taille
        self.fenetre_x = fenetre_x #600 #Largeur de la fenêtre
        self.fenetre_y = fenetre_y #600 #Longueur de la fenêtre
        self.fen = pygame.display.set_mode((fenetre_x, fenetre_y))
        pygame.display.set_caption('damier')#Nom de la fenêtre
        #self.fen.fill((167, 103, 38)) #couleur du fond: marron
        self.blanc = ( 255, 255, 255) # couleur blanc
        self.noir =  (0, 0, 0)        # couleur noir 


    def damier(self):

        for ligne in range (4): #création d'une boucle pour le nombre de carrés verticaux
            verticale1=ligne*self.fenetre_x/4
            verticale2=ligne*self.fenetre_x/4+self.fenetre_y/8
    
            for i in range (4): #création d'une boucle pour le nombre de carrés horizontaux
                horizontale1=i*self.fenetre_x/4
                horizontale2=i*self.fenetre_x/4+self.fenetre_y/8

                # description rect(taille fenetre, couleur de la forme, 
                #                   (position vertical sur fenetre, position horizontale, taille verticale objet , taille horizontale),
                #                    ligne ou carre plein)

                pygame.draw.rect(self.fen, self.noir  , (verticale1, horizontale1, self.fenetre_x/8 ,self.fenetre_x/8), 0)
                pygame.draw.rect(self.fen, self.blanc , (verticale1, horizontale2, self.fenetre_x/8 ,self.fenetre_x/8), 0)

                pygame.draw.rect(self.fen, self.noir  , (verticale2, horizontale2, self.fenetre_x/8 ,self.fenetre_x/8), 0)
                pygame.draw.rect(self.fen, self.blanc , (verticale2, horizontale1, self.fenetre_x/8 ,self.fenetre_x/8), 0)
    
