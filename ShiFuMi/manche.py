import score

def manche(choix_joueur, choix_ordi, nom_j1 = "Papa", nom_j2 = "la Machine"):
    if choix_joueur == choix_ordi:
        print("Egalité, le tour ne compte pas...")
        return 0
    elif choix_ordi == 1 and choix_joueur == 3 :
        print("La manche est remportée par",nom_j2)
        score.score(2)
    elif choix_ordi == 3 and choix_joueur == 1 :
        print("La manche est remportée par", nom_j1)  # créer def pour choisir nom_joueur
        score.score(1)
    elif choix_ordi < choix_joueur:
        print("La manche est remportée par", nom_j1)  # créer def pour choisir nom_joueur
        score.score(1)
    elif choix_ordi > choix_joueur:
        print("La manche est remportée par",nom_j2)
        score.score(2)

