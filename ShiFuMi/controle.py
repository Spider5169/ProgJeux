import tour_joueur

def controle(entree) :
    try :
        entier = int(entree)

    except:
        print("Vous n'avez pas saisie un choix valide.")
        return False

    else :
        return entier


def controle_win(test):
    try :
        nom_gagnant = str(test)

    except :
        print("Après vérification, il n'y a pas encore de gagnant.")
        return False

    else :
        return nom_gagnant