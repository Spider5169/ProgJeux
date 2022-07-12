import tour_joueur

def controle(entree) :
    try :
        entier = int(entree)

    except:
        print("Vous n'avez pas saisie un choix valide.")
        return False

    else :
        return entier