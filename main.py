# This is a sample Python script.
import JustePrix
from JustePrix import *
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print ("Jeux textuels")


#liste des jeux
liste_jeux = ["le Juste Prix", "Duel",]
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print("\nChoisissez un jeu :")
    a = 0
    for i in liste_jeux :
        a += 1
        print (a,":",i)

    choix = input ("\nA quoi voulez-vous jouer ? (indiquez le numéro)\n")
    if choix == 1 :
        JustePrix.JustePrix()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
