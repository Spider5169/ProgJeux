
joueur = 0
ordi = 0

def score(resultat):
    global joueur, ordi
    print("on met à jour le tableau des scores ici")
    if resultat == 1 :
        joueur += 1
    elif resultat == 2 :
        ordi += 1


def voir_score():
    global joueur, ordi
    nom_joueur = "PAPA"
    nom_ordi = "Computer"
    nom_j = len(nom_joueur)+2
    nom_jo = round(len(nom_joueur)/2)
    nom_o = len(nom_ordi)+2
    nom_or = round (len(nom_ordi)/2)
    print("on affiche le tableau ici")
    print("| ","_"*nom_j,"|","_"*nom_o," |")
    print("|  ",nom_joueur," | ",nom_ordi,"  |")
    print("| ","_"*nom_j,"|","_"*nom_o," |")
    print("|"," "*nom_jo,joueur," "*nom_jo,"|"," "*nom_or,ordi," "*nom_or,"|")
    print("| ","_"*nom_j,"|","_"*nom_o," |")
    if joueur == 2 :
        return nom_joueur
    elif ordi == 2 :
        return nom_ordi
