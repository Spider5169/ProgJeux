

def controle(entree) :
    try :
        entier = int(entree)

    except:
        print("Vous n'avez pas saisie un choix valide.")
        return False

    else :
        if 0 < entier <4 :
            return entier
        else :
            return False


def controle2(entree) :
    try :
        entree = int(entree)

    except:
        print("Vous n'avez pas saisie un choix valide.")
        return False

    else :
        return entree