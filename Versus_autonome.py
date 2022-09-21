from random import *

liste_attaques = {
    "1": {
        "nom": "poing",
        "min": 3,
        "max": 5,
        "chance": "- 20% de chance de supprimer 2 pts d'armure"
    },
    "2": {
        "nom": "pied",
        "min": 2,
        "max": 6,
        "chance": "- 33% chance de doubler les dégats"
    },
    "3": {
        "nom": "tête",
        "min": 7,
        "max": 3,
        "chance": " - 50% de chance de réussir",
    },
    "4": {
        "nom": "Genou",
        "min": 0,
        "max": -1,
        "chance": " - 50% chance de supprimer 1 pts d'armure."
    },
    "5": {
        "nom": "coude",
        "min": 0,
        "max": 10,
        "chance": " - 50% de chance de réussir",
    },
}

liste_att_magic = {
    "1": {
        "nom": "Soins\t",
        "min": 10,
        "max": 25,
        "chance": "- soigne vos pts de vie.",
        "temp": 1,
    },
    "2":{
        "nom": "FireBall",
        "min": 10,
        "max": 20,
        "chance": "- 25% bruler l'ennemi qui fait perdre 2 pt d'armure.",
        "temp": 1,
    },
    "3":{
        "nom": "IceStorm",
        "min": 5,
        "max": 10,
        "chance": "- 50% geler l'ennemi pour 1 tour.",
        "temp": randint(2,3),
    },
    "4": {
        "nom": "Spécial",
        "min": 25,
        "max": 50,
        "chance": "- Magie Ultime débloquée, détruit l'armure de l'ennemi.",
        "temp": randint(2, 6),
    },
}


#création joueur
class Player:

    def __init__(self, nom, hp=50, inventaire={}, degatmin=0, degatmax=5, degat_magic=3, armure=5):
        self.nom = nom
        self.hp = hp
        self.inventaire = inventaire
        self.degatmin = degatmin
        self.degatmax = degatmax
        self.degat_magic = degat_magic
        self.armure = armure

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

    def get_armure(self):
        return self.armure

    def add_inventaire(self, objet, min, max):
        self.inventaire[objet]={
            "min": min,
            "max": max,
        }
        return self.inventaire

    def add_armure(self, points):
        self.armure += points
        print(self.nom,"a maintenant",self.armure,"pts d'armure.")
        return self.armure

    def suppr_armure(self, point):
        self.armure -= point
        print(self.nom,"perd",point,"pts d'armure. Il lui reste",self.armure,"pts d'armure.")
        return self.armure

    def del_armure(self):
        self.armure = 0
        print("L'armure de",self.nom,"est détruite.")
        return self.armure

    def damage(self, dommage):
        if dommage > 0:
            dommage -= self.armure
            if dommage < 0 :
                dommage = 0
            print("moins",self.armure,"pts bloqués par l'armure.\t\t Dégats Finaux :",dommage,"pts.")
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


def pile_face():
    debut = randint(1, 2)
    return debut


#controle input pour tous les inputs, preciser type pour lancer bon try !
def controle_input(entree, nombre, type_attendu=1):
    #print("debut controle : saisie",entree,"et nombre",nombre)
    if type_attendu == 1 : #int
        try :
            entree1 = int(entree)
            if 0 <= entree1 <= nombre:
                return entree1
            else :
                print("Vous n'avez pas choisi un élément dans la liste.")
                return False
        except :
            return False
    elif type_attendu == 2 : #float (nombre a virgule)
        try :
            entree2 = float(entree)
            return entree2
        except :
            return False
    elif type_attendu == 3 : #Booleen
        try :
            entree3 = bool(entree)
            return entree3
        except :
            return False


lucky = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,
         40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,
         77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
#gain aléatoir d'un objet
def drop(atta, defe):
    global lucky
    luck = choice(lucky)
    lucky.remove(luck)
    arme = choice(["Epée","Marteau","Dague","Lance","Hache"])
    deg_arme_min = 5
    deg_arme_max = 10
    deg_arme_m_min = randint(15,25)
    deg_arme_m_max = randint(25,40)
    arme_magic = choice(["Gungnïr","Mjolnïr","Soul Calibur","Sabre Laser"])
    objet_magic = choice(["Baton Magique", "Book of Spell", "Orbe de Pouvoir","Baguette Magique"])
    degat_magic = randint(5,10)
    defense = randint(2,6)
    if luck == 7 :
        atta.damage(-50)
        print(atta.get_nom(),"est très CHANCEUX, vous gagnez 50 pts de vie.")
        atta.add_inventaire("EXCALIBUR", 35, 50)
        print("Vous trouvez également l'épée Ultime EXCALIBUR.")
    elif 80 < luck < 100 :
        print("Vous avez trouvé une Super Arme.")
        atta.add_inventaire(arme_magic,deg_arme_m_min,deg_arme_m_max)
    elif 60 < luck < 80 :
        print("Vous avez ramassé une pièce d'armure.")
        atta.add_armure(defense)
    elif 25 < luck < 50 :
        print("Vous venez de trouver", objet_magic,"qui vous a automatiquement renforcé de",
              degat_magic,"pts en Magie.")
        atta.equip_magic(degat_magic)
    elif 7 < luck < 25 :
        print("Vous avez trouvé une arme.")
        atta.add_inventaire(arme,deg_arme_min,deg_arme_max)
    elif 0 < luck < 7 :
        luck1 = luck + 5
        print(defe.get_nom(),"vient de subir une malédiction de",luck1,"pts de dégats,")
        defe.damage(luck1)
        print("Vie restante de",defe.get_nom(),":",defe.get_hp())
    else :
        print("...Rien de spécial...")


#infos joueur
def infos(joueur):
    print(joueur.get_nom())
    print("Vous avez", joueur.get_hp(),
          "points de vie et faites [",
          joueur.get_degatmin(), "-", joueur.get_degatmax(),
          "] pts de degats au Corps à Corps.")
    print("Votre armure est de", joueur.get_armure(),"pts qui bloquent autant de pts de dégats.")
    print("Votre puissance magique est de",joueur.get_degat_magic(),"pts de Magie.\n")
    inv = joueur.get_inventaire()
    if inv == {} :
        print ("Votre inventaire est vide\n")
    else :
        print(inv)


#liste des sorts
def list_sorts(joueur, tour):
    global liste_att_magic
    a = 0
    c = 0
    t = tour + choice([0,1])
    print()
    for x,y in liste_att_magic.items() :
        a += 1
        b = liste_att_magic[x]["temp"]
        if b == 1 :
            c += 1
            print (a,": sort", liste_att_magic[x]["nom"],
                       "\tpoints de puissance du sort [",liste_att_magic[x]["min"]+joueur.get_degat_magic(),
                   "-",liste_att_magic[x]["max"]+joueur.get_degat_magic(),
                       "]\tparticularité :",liste_att_magic[x]["chance"])
        if b == 2 and t % 2 == 0 :
            c += 1
            print (a,": sort", liste_att_magic[x]["nom"],
                       "\tpoints de puissance du sort [",liste_att_magic[x]["min"]+joueur.get_degat_magic(),
                   "-",liste_att_magic[x]["max"]+joueur.get_degat_magic(),
                       "]\tparticularité :",liste_att_magic[x]["chance"])

    choix = input("Quel sort lances-tu ?\t")
    choix_m = controle_input(choix, c, 1)
    return choix_m


#liste les attaques dispo
def liste_attaque(joueur):
    global liste_attaques
    a = 0
    print()
    for i,j in liste_attaques.items() :
        a += 1
        print(a,": Coup de", liste_attaques[i]["nom"],"[",
              liste_attaques[i]["min"]+joueur.get_degatmin(),"-",
              liste_attaques[i]["max"]+joueur.get_degatmax(),"] pts de dégats",
              liste_attaques[i]["chance"])
    return a


#equiper objet
def equiper_objet(joueur, tour):
    a = 0
    print("0 : Retour")
    for i in joueur.get_inventaire() :
        a += 1
        print(a,":",i)
    b = 0
    armes = input ("Quelle arme voulez-vous équiper ?")
    arme = controle_input(armes, a, 1)
    if arme == 0 :
        return "retour"
    else :
        dico = joueur.get_inventaire()
        for j,k in dico.items() :
            b += 1
            if b == arme :
                d_min = dico[j]["min"]
                d_max = dico[j]["max"]
                joueur.equip(d_min,d_max)
                print(j,"a été ajouté.")
                joueur.sup_arme(j)
                return
        print("ajout de l'arme échoué")
        return


#tour d'attaque
def tour_attaque(joueur, defenseur, tour, att_choisi):
    global liste_attaques
    proba = choice(range(100))
    if proba >2 :
        attaque = randint((liste_attaques[str(att_choisi)]["min"]+joueur.get_degatmin()),
                          (liste_attaques[str(att_choisi)]["max"]+joueur.get_degatmax()))
        if att_choisi == 3 or att_choisi == 5 :
            b = choice([0,1])
            if b == 0 :
                attaque = 0
                print("Vous ratez votre cible.",attaque,"pts de dégats.")
                return attaque
        elif att_choisi == 4 :
            b = choice([0,1])
            if b == 1 :
                defenseur.suppr_armure(1)
        elif att_choisi == 1 :
            b = choice([0,1,2,3,4])
            if b == 1 :
                defenseur.suppr_armure(2)
        elif att_choisi == 2 :
            b= choice ([0,1,2])
            if b == 1 :
                attaque *= 2
                print("Chanceux, vous doublez vos dégats !!!")

        print("Vous faites",attaque,"pts de dégats.")
        return attaque
    else :
        attaque = 0
        return attaque


#tour de magie
def tour_magie(joueur, tour, choix_mag):
    min = liste_att_magic[str(choix_mag)]["min"] + joueur.get_degat_magic()
    max = liste_att_magic[str(choix_mag)]["max"] + joueur.get_degat_magic()
    proba = choice(range(100))
    if choix_mag == 1 :
        soin = randint(-max,-min)
        print("soin : ",soin)
        return [soin, 0]
    elif proba > 2 :
        if choix_mag == 2 : #feu
            feu = randint(min, max)
            t = choice([1,4])
            if t > 1 :
                return [feu, 0]
            else :
                print("ATTENTION\t", joueur.get_nom(),"Brule son ennemi, et lui fait perdre 2 pts d'armure")
                return [feu, 2]
        elif choix_mag == 3 : #glace
            glace = randint(min, max)
            t = choice ([1,2])
            if t == 1 :
                return [glace, 0]
            else :
                print("ATTENTION\t",joueur.get_nom(),"gel son ennemi, et lui fait perdre 1 tour !!!")
                return [glace, 1]
        elif choix_mag == 4 : # Ultime
            if tour >= 8 :
                ultime = randint(min, max)
                return [ultime, 0]
            else :
                ultime = randint(min-10, max-10)
                return [ultime, 0]
    else :
        print("Le sort n'a pas fonctionné...")
        return 0


# 2 liste des choix d'action par tour
def liste_choix(j_attaque, tour):
    j= j_attaque
    droit_inv = False
    droit_mag = False
    print("\n\t\t",j.get_nom()+", que fais-tu ?")
    print("1 : Consulter ton inventaire")
    if j.get_inventaire() == {}:
        print ("votre inventaire est vide")
    else:
        droit_inv = True
        print("2 : Equiper objet")
    print("3 : Attaquer")
    if tour < 2 :
        print ("Votre Magie n'est pas encore prete.")
    else :
        droit_mag = True
        print("4 : Utiliser une magie\n")
    choix_a = input("choix :\t")
    choix_act = controle_input(choix_a, 4, 1)
    print()
    if choix_act == 1 :
        infos(j)
        return liste_choix(j, tour)
    elif choix_act == 2 and droit_inv :
        equip = equiper_objet(j, tour)
        if equip == "retour" :
            return liste_choix(j, tour)
        else :
            print("S'equiper d'un objet termine votre tour.")
            return [2, tour]
    elif choix_act == 3 :
        print("Liste des attaques disponibles :")
        print("0 : Retour")
        a = liste_attaque(j_attaque)
        choix = input("Choix de l'attaque :\t")
        choix_int = controle_input(choix, a, 1)
        if choix_int == 0:
            return liste_choix(j_attaque, tour)
        elif choix_int == False:
            return liste_choix(j_attaque, tour)
        else :
            return [3, choix_int]
    elif choix_act == 4 and droit_mag:
        print("Liste des Sorts disponibles :")
        print("0 : Retour")
        choix_mag = list_sorts(j_attaque, tour)
        if choix_mag == 0:
            return liste_choix(j_attaque, tour)
        elif choix_mag == False :
            return liste_choix(j_attaque, tour)
        else :
            return [4, choix_mag]
    else :
        return liste_choix(j, tour)


def commence_tour(commence):
    if (commence % 2) == 0:
        nom_debut = 2
        nom_fin = 1
        return nom_debut, nom_fin
    else:
        nom_debut = 1
        nom_fin = 2
        return nom_debut, nom_fin


# 1 choix de l'action
def action(j1,j2,commence):
    tour = 0
    while j1.get_hp() > 0 and j2.get_hp() > 0 :
        joueur = commence_tour(commence)
        if joueur[0] == 1 :
            j_att = j1
            j_def = j2
        else :
            j_att = j2
            j_def = j1

        drop (j_att,j_def)
        choix = liste_choix(j_att, tour)
        text_f = "\n\t\tFin du tour"
        if choix[0] == 3 : #on attaque au càc
            attaque = tour_attaque(j_att, j_def, tour, choix[1])
            j_def.damage(attaque)
            print("Il reste",j_def.get_hp(),"pts de vie à",j_def.get_nom())
            tour += 1
            commence += 1
            print(text_f,"d'attaque :", tour, "\n")
        elif choix[0] == 4 : #on utilise la magie
            degat = tour_magie(j_att, tour, choix[1])
            degats = degat[0]
            tour_sup = 0
            if degat[1] == 1 :
                tour_sup = degat[1]
            elif degat[1] == 2 :
                j_def.suppr_armure(2)
            if degats < 0 :
                j_att.damage(degats)
                print (j_att.get_nom(),"s'est soigné de",-degats,"pts de vie,"
                                                                 " il a maintenant",j_att.get_hp(),"pts de vie")
            else :
                j_def.damage(degats)
                print(j_def.get_nom(),"subit",degats-j_def.get_armure(),
                      "pts de magie, il lui reste",j_def.get_hp(),"pts de vie.")
            tour += 1
            commence += 1 + tour_sup
            print(text_f,"de magie:", tour, "\n")
        else:
            tour += 1
            commence += 1
            print(text_f,":", tour, "\n")
    hp1 = j1.get_hp()
    hp2 = j2.get_hp()
    return tour,hp1,hp2


def nom_joueur(name):
    saisie = input("Quel est le nom du joueur {} ?\n".format(name))
    if not saisie == "":
        return saisie
    else:
        saisie2 = "Player{}".format(name)
        return saisie2


# Programme principal
def versus():
    print("version améliorée de Duel !")
    joueur1 = "Papa"
    joueur2 = "nom_joueur(2)"
    print(joueur1,"VERSUS",joueur2)
    commence = pile_face()
    debut = ("joue en premier.\n")
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