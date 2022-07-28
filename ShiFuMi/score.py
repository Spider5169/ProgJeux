
joueur = 0
ordi = 0

def score(resultat):
    global joueur, ordi
    #print("on met à jour le tableau des scores ici")
    if resultat == 1 :
        joueur += 1
    elif resultat == 2 :
        ordi += 1


def voir_score(nb_manche_win, j1, j2):
    global joueur, ordi
    nom_joueur = j1
    nom_ordi = j2
    nom_j = len(nom_joueur)+2
    nom_jo = round(len(nom_joueur)/2)
    nom_o = len(nom_ordi)+2
    nom_or = round (len(nom_ordi)/2)
    #print("on affiche le tableau ici")
    print("| ","_"*nom_j," |","_"*nom_o,"  |")
    print("|  ",nom_joueur,"  | ",nom_ordi,"   |")
    print("| ","_"*nom_j," |","_"*nom_o,"  |")
    print("|"," "*nom_jo,joueur," "*nom_jo,"|"," "*nom_or,ordi," "*nom_or,"|")
    print("| ","_"*nom_j," |","_"*nom_o,"  |")
    if joueur == nb_manche_win :
        return nom_joueur
    elif ordi == nb_manche_win :
        return nom_ordi

def verif(nb_manche_win):
    global joueur, ordi
    if joueur == nb_manche_win or ordi == nb_manche_win :
        return False
    else:
        return True