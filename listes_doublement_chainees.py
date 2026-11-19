
#! /usr/bin/env python3

"""Listes doublement chaînées"""


class CelluleDoublementChainee:

    def __init__(self, val, suiv=None):
        self.valeur = val
        self.suivant = suiv
        self.precedent = None

        if suiv is not None:
            suiv.precedent = self


class ListeDoublementChainee:

    def __init__(self):
        self.tete = None
        self.queue = None

    def est_vide(self):
        return self.tete is None

    def cellule_tete(self):
        return self.tete

    def cellule_queue(self):
        return self.queue

    # Ajouter en début
    def inserer_tete(self, val):
        nouvelle = CelluleDoublementChainee(val, self.tete)

        if self.tete is None:
            self.queue = nouvelle

        self.tete = nouvelle

    # Supprimer en début
    def supprimer_tete(self):
        if self.tete is None:
            return

        self.tete = self.tete.suivant

        if self.tete is None:
            self.queue = None
        else:
            self.tete.precedent = None

    # Ajouter en fin
    def inserer_queue(self, val):
        nouvelle = CelluleDoublementChainee(val)

        if self.queue is None:
            self.tete = nouvelle
            self.queue = nouvelle
            return

        nouvelle.precedent = self.queue
        self.queue.suivant = nouvelle
        self.queue = nouvelle

    # Supprimer en fin
    def supprimer_queue(self):
        if self.queue is None:
            return

        self.queue = self.queue.precedent

        if self.queue is None:
            self.tete = None
        else:
            self.queue.suivant = None

    # Nombre de cellules en version itérative
    def longueur(self):
        l = 0
        courant = self.tete

        while courant is not None:
            l += 1
            courant = courant.suivant

        return l

    # Nombre de cellules en version récursive
    def longueur_recursif(self):

        def longueur_aux(cell):
            if cell is None:
                return 0

            return 1 + longueur_aux(cell.suivant)

        return longueur_aux(self.tete)

    # Affichage itératif
    def afficher(self):
        if self.tete is not None:
            print("Valeur en tete : " + str(self.tete.valeur))
        else:
            print("Tete is None")

        if self.queue is not None:
            print("Valeur en queue : " + str(self.queue.valeur))
        else:
            print("Queue is None")

        if self.tete is None:
            print("Liste vide !")

        courant = self.tete

        while courant is not None:
            print(courant.valeur, end=" -> ")
            courant = courant.suivant

        print("None")

    # Affichage récursif
    def afficher_recursif(self):

        def afficher_aux(cell):
            if cell is None:
                print("None")
                return

            print(cell.valeur, end=" -> ")
            afficher_aux(cell.suivant)

        if self.tete is None:
            print("Liste vide !")
        else:
            afficher_aux(self.tete)


def tests():
    L = ListeDoublementChainee()
    L.inserer_tete(10)
    L.inserer_tete(20)
    L.inserer_tete(30)

    L1 = ListeDoublementChainee()
    L1.inserer_tete(1)

    L2 = ListeDoublementChainee()

    L.afficher()
    L1.afficher()
    L2.afficher()

    L.afficher_recursif()
    L1.afficher_recursif()
    L2.afficher_recursif()

    print(L.longueur())
    print(L1.longueur())
    print(L2.longueur())

    print(L.longueur_recursif())
    print(L1.longueur_recursif())
    print(L2.longueur_recursif())

    L.supprimer_tete(); L.afficher()
    L.supprimer_tete(); L.afficher()
    L.supprimer_tete(); L.afficher()
    L.supprimer_tete(); L.afficher()

    L.inserer_tete(1); L.afficher()
    L.inserer_tete(2); L.afficher()
    L.inserer_tete(3); L.afficher()

    # BONUS
    L.supprimer_queue(); L.afficher()
    L.supprimer_queue(); L.afficher()
    L.supprimer_queue(); L.afficher()
    L.supprimer_queue(); L.afficher()

    L.inserer_queue(1); L.afficher()
    L.inserer_queue(2); L.afficher()
    L.inserer_queue(3); L.afficher()


if __name__ == "__main__":
    tests()
