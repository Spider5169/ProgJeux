import os
import json

print("_____________\n"
      "|  Moteur   |\n"
      "|    de     |\n"
      "| Recherche |\n"
      "|___________|")

'''
1     verifier ou créer fichier json contenant texte /articles
2     créer class Articles
      _nom
      _ref numérique
      _description longue
      _prix
3     ajouter articles dans fichier
4     demander a utilisateur d'entrer sa recherche
5     spliter sa recherche
6     comparer sa recherche
      _avec parametres nom / description
      _determiner si chiffres
            si OUI comparer avec Ref / Prix
7     afficher résultats
8     trier par pertinance
'''


# 1
def loader():
    dico = {}
    if os.path.exists("list_article.json"):
        with open("list_article.json", "r+") as file:
            dico = file.readlines()
            print("loader\t",dico)
    else :
        with open("list_article.json", "w+") as file:
            json.dump(dico,file)

# 2
class Article:

    def __init__(self, nom, reference, description, prix):
        self.nom = nom
        self.ref = reference
        self.desc = description
        self.prix = prix

    def get_nom(self):
        return self.nom

    def get_ref(self):
        return self.ref

    def get_desc(self):
        return self.desc

    def get_prix(self):
        return self.prix

#incremente un indice et s'en rappelle
def plus_un():
    try :
        with open ("indice.json", "r+") as file2 :
            var = file2.read()
            var = int(var)
            var += 1
            file2.close()
        with open ("indice.json", "w+") as file3 :
            json.dump(var, file3)
            return var
    except :
        file1 = open("indice.json", "w+")
        var = 1
        with open("indice.json", "w+") as file1 :
            json.dump(var, file1)
            return var
#3
def creation_article():
    indice = plus_un()
    print("retour de 'plus un'\t", indice)
    a = input("Nom :")
    b = input("Référence :")
    c = input("Description de l'article :")
    d = input("Prix :")
    nouvel_article = Article(a, b, c, d)
    i_dico = int(indice) -1
    with open("list_article.json", "r+") as file :
        dico = json.load(file)
    dico [nouvel_article.get_nom()] = {
        "indice" : i_dico
    }
    with open("list_article.json", "w+") as file2 :
        json.dump(dico,file2)
        file.close()

#4
def recherche():
    r = input("Saisissez votre recherche :\n")
    r = r.split(" ")
    indice = -1
    with open ("list_article.json", "r+") as files :
        liste_1 = json.load(files)
        for i in r :
            print ("i=",i,"r=",r)
            for j in liste_1 :
                print ("j=",j,"liste=",liste_1)
                indice += 1
                if i == j :
                    print (i)
                    indice_res = indice


#programme principal
def moteur_recherche():
    loader()
    #creation_article()
    with open ("list_article.json", "r+") as files :
        dico_1 = files.readlines()
        for i in dico_1 :
            print("liste le dico du fichier article\t",i)

    recherche()

if __name__ == '__main__':
    moteur_recherche()