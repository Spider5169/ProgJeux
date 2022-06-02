import Duel
from random import *

liste_attaques = {
    "1": {
        "nom": "poing",
        "min": 2,
        "max": 4,
        "chance": ""
    },
    "2": {
        "nom": "pied",
        "min": 0,
        "max": 6,
        "chance": ""
    },
    "3": {
        "nom": "tête",
        "min": 5,
        "max": 5,
        "chance": " - 50% de chance de réussir",
    },
}

#création joueur
class Player:

    def __init__(self, nom, hp=50, inventaire={}, degatmin=0, degatmax=5):
        self.nom = nom
        self.hp = hp
        self.inventaire = inventaire
        self.degatmin = degatmin
        self.degatmax = degatmax

    def get_nom(self):
        return self.nom

    def get_hp(self):
        return self.hp

    def get_inventaire(self):
        return self.inventaire

    def get_degatmin(self):
        return self.degatmin

    def get_degatmax(self):
        return self.degatmax

    def add_inventaire(self, objet, min, max):
        self.inventaire[objet]={
            "min": min,
            "max": max,
        }
        return self.inventaire

    def damage(self, dommage):
        self.hp -= dommage
        return self.hp

    def equip(self, minobjet, maxobjet):
        self.degatmin += minobjet
        self.degatmax += maxobjet
        print(self.nom,"fait maintenant [",self.degatmin,"-",self.degatmax,"] de degats au CàC.")

    def sup_arme(self,indice):
        del self.inventaire[indice]


#gain aléatoir d'un objet
def drop(atta, defe):
    luck = randint(1,100)
    arme = choice(["Epée","Marteau","Dague","Lance","Hache"])
    deg_arme_min = 5
    deg_arme_max = 10
    deg_arme_m_min = 10
    deg_arme_m_max = 20
    arme_magic = choice(["Baton Magique","Gungnïr","Mjolnïr","Book of Spell"])
    if luck == 7 :
        atta.damage(-50)
        print(atta.get_nom(),"est très CHANCEUX, vous gagnez 50 pts de vie.")
        atta.add_inventaire("EXCALIBUR", 25, 50)
        print("Vous trouvez également l'épée Ultime EXCALIBUR.")
    elif 90 < luck < 100 :
        print("Vous avez trouvé une super arme.")
        atta.add_inventaire(arme_magic,deg_arme_m_min,deg_arme_m_max)
    elif 7 < luck < 25 :
        print("Vous avez trouvé une arme.")
        atta.add_inventaire(arme,deg_arme_min,deg_arme_max)
    elif 0 < luck < 7 :
        print(defe.get_nom(),"vient de subir une malédiction")
        defe.damage(luck)
        print("vous venez de perdre",luck,"pts, vie de",defe.get_nom(),":",defe.get_hp())
    else :
        print("Rien de spécial...")


#infos joueur
def infos(joueur):
    print(joueur.get_nom())
    print("Vous avez", joueur.get_hp(),
          "points de vie et faites [",
          joueur.get_degatmin(), "-", joueur.get_degatmax(),
          "] pts de degats\n")
    inv = joueur.get_inventaire()
    if inv == {} :
        print ("Votre inventaire est vide\n")
    else :
        print(inv)

#liste les attaques dispo
def liste_attaque(joueur):
    global liste_attaques
    a = 0
    for i,y in liste_attaques.items() :
        a += 1
        print(a,": Coup de", liste_attaques[i]["nom"],"[",
              liste_attaques[i]["min"]+joueur.get_degatmin(),"-",
              liste_attaques[i]["max"]+joueur.get_degatmax(),"] pts de dégats",
              liste_attaques[i]["chance"])


#equiper objet
def equiper_objet(joueur):
    a = 0
    for i in joueur.get_inventaire() :
        a += 1
        print(a,":",i)
    b = 0
    arme = input ("Quelle arme voulez-vous équiper ?")
    dico = joueur.get_inventaire()
    for j,k in dico.items() :
        b += 1
        if b == int(arme) :
            d_min = dico[j]["min"]
            d_max = dico[j]["max"]
            joueur.equip(d_min,d_max)
            print(j,"a été ajouté.")
            joueur.sup_arme(j)
            return joueur
        else :
            print("ajout de l'arme échoué")



#tour d'attaque
def tour_attaque(joueur):
    print("Liste des attaques disponibles :")
    liste_attaque(joueur)
    choix = input("Choix de l'attaque :")
    attaque = randint((liste_attaques[choix]["min"]+joueur.get_degatmin()),
                      (liste_attaques[choix]["max"]+joueur.get_degatmax()))
    choix_int = int(choix)
    if choix_int == 3 :
        a = choice([0,1])
        if a == 0 :
            attaque = 0
            print("Vous ratez votre cible.",attaque,"pts de dégats.")
            return attaque

    print("Vous faites",attaque,"pts de dégats")
    return attaque

#tour de magie
def tour_magie(joueur):
    pass

# 2 liste des choix d'action par tour
def liste_choix(j_attaque):
    j= j_attaque
    print(j.get_nom()+", que fais-tu ?")
    print("1 : Consulter ton inventaire")
    if j_attaque.get_inventaire() == {}:
        print ("votre inventaire est vide")
    else:
        print("2 : Equiper objet")
    print("3 : Attaquer")
    print("4 : Utiliser une magie\n")
    choix_a = input("choix :\t")
    try :
        choix_act = int(choix_a)
        if choix_act == 1 :
            infos(j)
            return liste_choix(j)
        elif choix_act == 2 :
            equiper_objet(j)
            print("S'equiper d'un objet termine votre tour.")
            return
        elif choix_act == 3 :
            return 3
        elif choix_act == 4 :
            return 4
    except :
        print("Vous avez raté votre tour, faites mieux la prochaine fois.")
        return 0


# 1 choix de l'action
def action(j1,j2,commence):
    tour = 0
    while j1.get_hp() > 0 and j2.get_hp() > 0 :
        joueur = Duel.commence_tour(commence)
        if joueur[0] == 1 :
            j_att = j1
            j_def = j2
        else :
            j_att = j2
            j_def = j1

        drop (j_att,j_def)
        choix = liste_choix(j_att)
        text_f = "\n\t\tFin du tour"
        if choix == 3 : #on attaque au càc
            attaque = tour_attaque(j_att)
            j_def.damage(attaque)
            print("Il reste",j_def.get_hp(),"pts de vie à",j_def.get_nom())
            tour += 1
            commence += 1
            print(text_f,"d'attaque :", tour, "\n")
        elif choix == 4 : #on utilise la magie
            tour_magie(j_att)
            tour += 1
            commence += 1
            print(text_f,"de magie:", tour, "\n")
        else:
            tour += 1
            commence += 1
            print(text_f,":", tour, "\n")

    return tour


# Programme principal
def versus():
    print("version améliorée de Duel !")
    joueur1 = "Papa"
    joueur2 = Duel.nom_joueur(2)
    print(joueur1,"VERSUS",joueur2)
    commence = Duel.pile_face()
    debut = (" joue en premier.\n")
    j1 = Player(joueur1)
    j2 = Player(joueur2)
    if commence == 1 :
        print(j1.get_nom(),debut)
    else :
        print(j2.get_nom(),debut)

    partie = action(j1,j2,commence)



if __name__ == "__main__":
    versus()