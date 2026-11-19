
#! /usr/bin/env python3

"""Implémentation des piles à l'aide de listes simplement chaînées"""

from listes_simplement_chainees import ListeChainee

class Pile:
    def __init__(self):
        self.liste = ListeChainee()

    def est_vide(self):
        return self.liste.est_vide()

    def sommet(self):
        if self.est_vide():
            print("La pile est vide")

        return self.liste.cellule_tete().valeur

    def empiler(self, x):
        self.liste.inserer_tete(x)

    def depiler(self):
        if self.est_vide():
            print("La pile est vide")

        valeur = self.sommet()
        self.liste.supprimer_tete()
        return valeur

    def longueur(self):
        return self.liste.longueur()

    def afficher(self):
        self.liste.afficher()


if __name__ == "__main__":
    p1 = Pile()

    p1.empiler(1)
    p1.empiler(2)
    p1.empiler(3)
    p1.afficher()

    v = p1.depiler()
    print("Extrait : " + str(v))

    v = p1.depiler()
    print("Extrait : " + str(v))

    v = p1.depiler()
    print("Extrait : " + str(v))

    p1.afficher()
