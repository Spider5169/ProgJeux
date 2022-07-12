import random


def tour_ordi():
    choix = random.randint(1,3)
    if choix == 1 :
        return 1
    elif choix == 2 :
        return 2
    elif choix == 3 :
        return 3

def get_choix_ordi() :
    pass


if __name__ == "__main__":
    tour_ordi()