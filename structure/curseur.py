import pygame

class Selecteur:

    def __init__(self,fenetre_x, fenetre_y):
        self.fenetre_x = fenetre_x #Largeur de la fenêtre
        self.fenetre_y = fenetre_y #Longueur de la fenêtre
        self.position = [fenetre_x/2, fenetre_y/2] # position de depart du curseur au centre

    # deplacement du curseur de 1/8 du total de la fenetre ce qui represente une case de damier
    def droite(self): 
        self.position[0] += self.fenetre_x/8 

    def gauche(self): 
        self.position[0] -= self.fenetre_x/8

    def bas(self): 
        self.position[1] += self.fenetre_y/8

    def haut(self): 
        self.position[1] -= self.fenetre_y/8

    def input(self):
        clavier = pygame.key.get_pressed()

        if clavier[pygame.K_UP]:
            self.haut()
        elif clavier[pygame.K_DOWN]:
            self.bas()
        elif clavier[pygame.K_RIGHT]:
            self.droite()
        elif clavier[pygame.K_LEFT]:
            self.gauche()   

    def selecteur(self, marron , fen):
        
        if self.position[0] <= 0:
            self.position[0] = 0
        elif self.position[0] >= self.fenetre_y:
            self.position[0] = self.fenetre_y - self.fenetre_y/8

        if self.position[1] <= 0:
            self.position[1] = 0
        elif self.position[1] >= self.fenetre_x:
            self.position[1] = self.fenetre_x - self.fenetre_x/8
        
        pygame.draw.rect(fen, marron , (self.position[0], self.position[1], self.fenetre_x/8 ,self.fenetre_x/8), 10)
