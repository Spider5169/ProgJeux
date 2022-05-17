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
def degat_choisi(attaque2, tour):
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
    elif attaque2 == 4:
        if tour < 4 :
            print("Vous avez raté votre coup !")
            degats = 0
            return degats
        else :
            degats = randint(25,50)
            return degats
    else:
        print("Vous avez raté votre coup !")
        degats = 0
        return degats


#liste des attaques possibles, penser a rajouter dans degat_choisi
def liste_attaque(tour):
    liste_attaque = {
        "Poing":{
            "min":2,
            "max":6,
            "chance" : ""
        },
        "Pied":{
            "min":0,
            "max":9,
            "chance" : ""
        },
        "Tête":{
            "min":5,
            "max":5,
            "chance" : " - 50% de chance de réussir",
        },
        "Spécial":{
            "min":25,
            "max":50,
            "chance": "- coup Ultime débloqué"
        }
    }
    a = 0
    if tour > 4 :
        for i,y in liste_attaque.items() :
            b = randint(1,4)
            if b <2 :
                a += 1
                print(a,": Coup de", i,"[",liste_attaque[i]["min"],"-",liste_attaque[i]["max"],"] pts de dégats",liste_attaque[i]["chance"])
            elif a < 3 :
                a += 1
                print(a, ": Coup de", i, "[", liste_attaque[i]["min"], "-", liste_attaque[i]["max"], "] pts de dégats",
                      liste_attaque[i]["chance"])
            else:
                break
    else :
        for i,y in liste_attaque.items() :
            if a < 3 :
                a += 1
                print(a,": Coup de", i,"[",liste_attaque[i]["min"],"-",liste_attaque[i]["max"],"] pts de dégats",liste_attaque[i]["chance"])
            else :
                break


# on choisi l'attaque que l'on lance
def attack(tour):
    print("Choisissez une attaque :")
    liste_attaque(tour)
    atta = input("Choix :")
    try :
        attaque = int(atta)
        return degat_choisi(attaque, tour)
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

#tour de combat
def tour_att(hp_j1, hp_j2, commence, joueur1, joueur2):
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
        degat_subit = attack(tour)
        if (commence % 2) == 0:
            hp_j1 -= degat_subit
            print(degat_subit, "pts de dégats, il reste", hp_j1, "pts de vie à", j_def)
        else:
            hp_j2 -= degat_subit
            print(degat_subit, "pts de dégats, il reste", hp_j2, "pts de vie à", j_def)
        tour += 1
        commence += 1
        print("Fin du tour :", tour, "\n")
    return tour

#choisir nombre de PV pour ralonger parties
def pts_de_vie(default):
    hp = input("Combien de Points de vie ont les joueurs ? (par défaut 10, max 50)")
    try :
        pts = int(hp)
        if 1 < pts < 51 :
            return pts
        else :
            print ("Erreur, HP par défaut appliqués")
            pts = default
            return  pts
    except :
        return pts_de_vie(10)


#prog principal du jeu
def duel():
    print("\tBienvenue dans Duel")
    print("Ici 2 Adversaires vont s'affronter avec 10 pts de vie chacun.")
    print("C'est simple, le 1er qui a 0 pts de vie perd la partie.")
    joueur1 = nom_joueur(1) #on demande nom des joueurs
    joueur2 = nom_joueur(2) #on demande nom des joueurs
    print(joueur1, "VS", joueur2, "\tPret ? c'est parti...")
    hp_j1 = hp_j2 = pts_de_vie(10)  #on determine combien de pts de vie
    commence = pile_face()  #on determine qui commence
    debut = " commence la partie.\n"
    if commence == 1:   #on affiche qui commence
        print(joueur1, debut)
    else:
        print(joueur2, debut)
    tour = tour_att(hp_j1,hp_j2,commence,joueur1,joueur2)   #deroulement de la partie
    fin = "remporte la partie en "+str(tour)+" tours."
    if hp_j1 < 1:   #on affiche le gagnant
        print(joueur2, fin)
    else:
        print(joueur1, fin)


if __name__ == "__main__":
    duel()
