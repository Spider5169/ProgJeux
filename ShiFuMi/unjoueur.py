from random import random

import controle
import tour_ordi, tour_joueur, score, manche


def partie():
    print("La partie Commence, c'est en 2 manches gagnantes.")
    round = 0
    while round < 3 :
        round += 1
        print("Manche",round,"en cours :")
        choix_ordi = tour_ordi.tour_ordi()
        print (choix_ordi)
        choix_joueur = tour_joueur.tour_joueur()
        print(choix_joueur)
        result = manche.manche(choix_joueur,choix_ordi)
        if result == 0:
            round -= 1
        nom = score.voir_score()


    print("\n\t Fin de la Partie\n")
    print("on affiche le vainqueur ici :", nom)




if __name__ == '__main__' :
    partie()