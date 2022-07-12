import controle

def tour_joueur():
    liste =["Pierre","Feuille","Ciseaux"]
    a = 0
    for i in liste :
        a += 1
        print("\t",a,":",i)
    choix = input("Quel est votre choix ?\n")
    reponse = controle.controle(choix)
    if reponse == False:
        return tour_joueur()
    else :
        return reponse



if __name__ == "__main__":
    tour_joueur()