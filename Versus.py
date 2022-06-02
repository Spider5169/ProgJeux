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

liste_att_magic = {
    "1": {
        "nom": "Soins\t",
        "min": 5,
        "max": 20,
        "chance": "- soigne vos pts de vie.",
        "temp": 1,
    },
    "2":{
        "nom": "FireBall",
        "min": 10,
        "max": 20,
        "chance": "- aucune",
        "temp": 1,
    },
    "3":{
        "nom": "IceStorm",
        "min": 5,
        "max": 10,
        "chance": "- Peut geler l'ennemi pour 1 tour",
        "temp": randint(1,2),
    },
    "4": {
        "nom": "Spécial",
        "min": 25,
        "max": 50,
        "chance": "- coup Ultime débloqué",
        "temp": randint(1, 5),
    },
}

#création joueur
class Player:

    def __init__(self, nom, hp=50, inventaire={}, degatmin=0, degatmax=5, degat_magic=3):
        self.nom = nom
        self.hp = hp
        self.inventaire = inventaire
        self.degatmin = degatmin
        self.degatmax = degatmax
        self.degat_magic = degat_magic

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

    def get_degat_magic(self):
        return self.degat_magic

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

    def equip_magic(self, degat_m):
        self.degat_magic += degat_m
        print(self.nom,"dispose de",self.degat_magic,"pts de pouvoir magique !")

    def sup_arme(self,indice):
        del self.inventaire[indice]


#gain aléatoir d'un objet
def drop(atta, defe):
    luck = randint(1,100)
    arme = choice(["Epée","Marteau","Dague","Lance","Hache"])
    deg_arme_min = 5
    deg_arme_max = 10
    deg_arme_m_min = randint(10,20)
    deg_arme_m_max = randint(20,40)
    arme_magic = choice(["Gungnïr","Mjolnïr","Soul Calibur",])
    objet_magic = choice(["Baton Magique", "Book of Spell", "Orbe de Pouvoir"])
    degat_magic = randint(5,10)
    if luck == 7 :
        atta.damage(-50)
        print(atta.get_nom(),"est très CHANCEUX, vous gagnez 50 pts de vie.")
        atta.add_inventaire("EXCALIBUR", 25, 50)
        print("Vous trouvez également l'épée Ultime EXCALIBUR.")
    elif 90 < luck < 100 :
        print("Vous avez trouvé une super arme.")
        atta.add_inventaire(arme_magic,deg_arme_m_min,deg_arme_m_max)
    elif 25 < luck < 35 :
        print("Vous venez de trouver", objet_magic,"qui vous a automatiquement renforcé de",
              degat_magic,"pts en Magie.")
        atta.equip_magic(degat_magic)
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

#liste des sorts
def list_sorts(tour):
    global liste_att_magic
    a = 0
    c = 0
    t = tour
    for x,y in liste_att_magic.items() :
        a += 1
        b = liste_att_magic[x]["temp"]
        if b == 1 :
            print (a,": sort", liste_att_magic[x]["nom"],
                       "\tpoints de puissance du sort [",liste_att_magic[x]["min"],"-",liste_att_magic[x]["max"],
                       "]\tparticularité :",liste_att_magic[x]["chance"])
    choix = input("Quel sort lasses-tu ?\t")
    choix_m = int(choix)
    return choix_m


#liste les attaques dispo
def liste_attaque(joueur):
    global liste_attaques
    a = 0
    for i,j in liste_attaques.items() :
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
    choix = input("Choix de l'attaque :\t")
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
def tour_magie(joueur, tour):
    print("Liste des Sorts disponibles :")
    choix_mag = list_sorts(tour)
    min = liste_att_magic[str(choix_mag)]["min"] + joueur.get_degat_magic()
    max = liste_att_magic[str(choix_mag)]["max"] + joueur.get_degat_magic()
    if choix_mag == 1 :
        soin = randint(-max,-min)
        print("soin : ",soin)
        return soin
    elif choix_mag == 2 : #feu
        feu = randint(min, max)
        return feu
    elif choix_mag == 3 : #glace
        glace = randint(min, max)
        t = choice ([1,2])
        if t == 1 :
            return glace
        else :
            tour += 1
            return glace, tour
    elif choix_mag == 4 : # Ultime
        ultime = randint(min, max)
        return ultime
    else :
        print("Le sort n'a pas fonctionné...")
        return 0


# 2 liste des choix d'action par tour
def liste_choix(j_attaque, tour):
    j= j_attaque
    print(j.get_nom()+", que fais-tu ?")
    print("1 : Consulter ton inventaire")
    if j_attaque.get_inventaire() == {}:
        print ("votre inventaire est vide")
    else:
        print("2 : Equiper objet")
    print("3 : Attaquer")
    if tour < 2 :
        print ("Votre Magie n'est pas encore prete.")
    else :
        print("4 : Utiliser une magie\n")
    choix_a = input("choix :\t")
    try :
        choix_act = int(choix_a)
        if choix_act == 1 :
            infos(j)
            return liste_choix(j, tour)
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
        choix = liste_choix(j_att, tour)
        text_f = "\n\t\tFin du tour"
        if choix == 3 : #on attaque au càc
            attaque = tour_attaque(j_att)
            j_def.damage(attaque)
            print("Il reste",j_def.get_hp(),"pts de vie à",j_def.get_nom())
            tour += 1
            commence += 1
            print(text_f,"d'attaque :", tour, "\n")
        elif choix == 4 : #on utilise la magie
            degats = tour_magie(j_att, tour)
            if degats < 0 :
                j_att.damage(degats)
                print (j_att.get_nom(),"s'est soigné de",-degats,"pts de vie,"
                                                                 " il a maintenant",j_att.get_hp(),"pts de vie")
            else :
                j_def.damage(degats)
                print(j_def.get_nom(),"subit",degats,"pts de magie, il lui reste",j_def.get_hp(),"pts de vie.")
            tour += 1 + degats[1]
            commence += 1
            print(text_f,"de magie:", tour, "\n")
        else:
            tour += 1
            commence += 1
            print(text_f,":", tour, "\n")
    hp1 = j1.get_hp()
    hp2 = j2.get_hp()
    return tour,hp1,hp2


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
    fini = "La partie s'est terminée en",partie[0],"tours."
    if partie[1] < 1 :
        print(fini,"\n",j2.get_nom(),"remporte la partie.")
    else :
        print(fini,"\n",j1.get_nom(),"gagne car",j2.get_nom(),"a",j2.get_hp(),"pts de vie.")




if __name__ == "__main__":
    versus()