
import main
import random

# le jeu choisis un prix aléatoirement
prix = 0
def valeur_kdo():
    global prix
    prix = random.randint(1,100)
    print("\nA vous de jouer :")
    return prix

# on demande au joueur un nombre et on verifie que c'est bien un entier
def demande_valeur():
    valeur = input("Quelle est la valeur que vous choisissez ?\n")
    try :
        val_num = int(valeur)
        controle_valeur(val_num)
    except :
        print ("Vous devez saisir seulement un nombre.\n")
        demande_valeur()

# on vérifie que la valeur soit bien entre 1 et 100
valeur_num = 0
def controle_valeur(entree, mini = 1, maxi = 100):
    global valeur_num
    if entree > maxi or entree < mini :
        print("Vous devez trouver une valeur entre 1 et 100...\n")
        demande_valeur()
    else :
        valeur_num = entree
        return valeur_num

# on compare la valeur au prix choisi
def comparer():
    global valeur_num, prix
    if valeur_num < prix :
        print("C'est Plus +")
    elif valeur_num > prix :
        print("C'est moins -")

def justeprix():
    print("\tBienvenue dans le JUSTE PRIX")
    print("Ici vous devrez deviner la valeur situé entre 1 et 100 !")

    valeur_kdo()
    tour = 0
    while not valeur_num == prix :
        demande_valeur()
        comparer()
        tour += 1

    print ("Felicitations, la valeur à découvrir était bien",prix,".")
    print ("Vous avez réussis en",tour,"tours. Merci\n")
    print ("\tFin")


if __name__ == '__main__':
    justeprix()
'''faire une boucle pour restart tant qu on veut, avec une  def restart()
    restart = input("Une nouvelle partie ?\n\t1 pour OUI\n\t2 pour NON\n")
    try :
        restart_choix = int(restart)
        controle_valeur(restart_choix,1,2)
    except :
        print("\nSaisie incorrecte.")
        quit()
    if restart_choix == 1 :
        justeprix()
    else :
        main.print_hi()
'''