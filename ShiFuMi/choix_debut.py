

def nom_joueur(numero):
    nom_joueur = input("Saisissez le nom du joueur {}:\n".format(numero))
    if nom_joueur == "":
        nom_joueur= "Joueur"+str(numero)
    return nom_joueur


def nb_manche():
    manche = input("En combien de victoire voulez-vous jouer ?")
    if manche == "" :
        manche = 2
    return manche