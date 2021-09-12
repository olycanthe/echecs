import pygame

class Plateau:

    def damier(self, couleur, blanc, fenetre_x, fenetre_y, fen):
        pygame.draw.rect(fen, blanc, (0,0, fenetre_x, fenetre_y), 0) # création d'une page blanche

        case_x = fenetre_x/8
        case_y = fenetre_y/8

        # création du damier 8x8= ce qui correspond au nombre de case dans un echiquier
        for horizontale in range(8):
            for verticale in range(8):
                incre = horizontale*case_x
                incre2 = verticale*case_y

                #retour de la division si une case noir doit petre créé
                if horizontale % 2 != 0 and verticale % 2 == 0 :
                    pygame.draw.rect(fen, couleur, (incre, incre2, case_x, case_y), 0)
                if horizontale % 2 == 0 and verticale % 2 != 0 :
                    pygame.draw.rect(fen, couleur, (incre, incre2, case_x, case_y), 0)