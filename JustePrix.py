
import random

def JustePrix():
    print("Bienvenue dans le Juste Prix")
    print("Ici vous devrez deviner la valeur situé entre 1 et 100 !")
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
    def controle_valeur(entree):
        global valeur_num
        if entree > 100 or entree < 1 :
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


    valeur_kdo()
    tour = 0
    while not valeur_num == prix :
        demande_valeur()
        comparer()
        tour += 1

    print ("Felicitations, la valeur à découvrir était bien",prix,".")
    print ("Vous avez réussis en",tour,"tours. Merci\n")
    print ("\tFin")
