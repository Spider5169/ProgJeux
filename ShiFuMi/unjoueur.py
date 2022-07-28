import tour_ordi, tour_joueur, score, manche, choix_debut


def partie():
    j1 = choix_debut.nom_joueur(1)
    j2 = "Ordinateur"
    nb_manche_win = choix_debut.nb_manche()
    print("La partie Commence, c'est en",nb_manche_win,"manches gagnantes.")
    round = 0
    gagne = True
    while gagne :
        round += 1
        print("Manche",round,"en cours :")
        choix_ordi = tour_ordi.tour_ordi()
        print (choix_ordi)
        choix_joueur = tour_joueur.tour_joueur()
        print(choix_joueur)
        result = manche.manche(choix_joueur,choix_ordi, j1, j2)
        if result == 0:
            round -= 1
        nom = score.voir_score(nb_manche_win, j1, j2)
        #on verifie si 1 joueur a gagné
        gagne = score.verif(nb_manche_win)

    print("\n\t Fin de la Partie\n")
    print("on affiche le vainqueur ici :", nom)




if __name__ == '__main__' :
    partie()