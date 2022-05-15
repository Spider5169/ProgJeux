from random import *


# on donne un nom aux joueurs
def nom_joueur(name):
    saisie = input("Quel est le nom du joueur {} ?\n".format(name))
    if not saisie == "":
        return saisie
    else:
        saisie2 = "Player{}".format(name)
        return saisie2


# on determine qui commence par hasard
def pile_face():
    debut = randint(1, 2)
    return debut


# degats de l'attaque choisi
def degat_choisi(attaque2):
    if attaque2 == 1:
        degats = randint(2, 6)
        return degats
    elif attaque2 == 2:
        degats = randint(0, 8)
        return degats
    elif attaque2 == 3:
        deg = (0, 5)
        degats = choice(deg)
        return degats
    else:
        print("Vous avez raté votre coup !")
        degats = 0
        return degats


# on choisi l'attaque que l'on lance
def attack():
    print("Choisissez une attaque :\n"
          "1 : Coup de poing [2-6] pts de dégats\n"
          "2 : Coup de Pied [0-8] pts de dégats\n"
          "3 : Coup de Tête 5 pts de dégats, 50% chance de réussir\n")
    atta = input("Choix :")
    try :
        attaque = int(atta)
        return degat_choisi(attaque)
    except :
        return attack()


# pour alterner qui attaque
def commence_tour(commence):
    if (commence % 2) == 0:
        nom_debut = 2
        nom_fin = 1
        return nom_debut, nom_fin
    else:
        nom_debut = 1
        nom_fin = 2
        return nom_debut, nom_fin


def duel():
    print("\tBienvenue dans Duel")
    print("Ici 2 Adversaires vont s'affronter avec 10 pts de vie chacun.")
    print("C'est simple, le 1er qui a 0 pts de vie perd la partie.")
    joueur1 = nom_joueur(1)
    joueur2 = nom_joueur(2)
    print(joueur1, "VS", joueur2, "\tPret ? c'est parti...")
    commence = pile_face()
    if commence == 1:
        print("C'est", joueur1, "qui commence.\n")
    else:
        print("C'est", joueur2, "qui commence.\n")
    hp_j1 = 10
    hp_j2 = 10
    tour = 0
    while hp_j1 > 0 and hp_j2 > 0:
        nom_com = commence_tour(commence)
        if nom_com[0] == 1:
            j_att = joueur1
            j_def = joueur2
        else:
            j_att = joueur2
            j_def = joueur1
        print("Attaque de :", j_att)
        degat_subit = attack()
        print(degat_subit, ":", type(degat_subit))
        if (commence % 2) == 0:
            hp_j1 -= degat_subit
            print(degat_subit, "pts de dégats, il reste", hp_j1, "pts de vie à", j_def)
        else:
            hp_j2 -= degat_subit
            print(degat_subit, "pts de dégats, il reste", hp_j2, "pts de vie à", j_def)
        tour += 1
        commence += 1
        print("Fin du tour :", tour, "\n")

    if hp_j1 < 1:
        print(joueur2, "remporte la partie en", tour, "tours")
    else:
        print(joueur1, "remporte la partie en", tour, "tours")


if __name__ == "__main__":
    duel()
