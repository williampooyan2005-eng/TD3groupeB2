#! /usr/bin/env python3

"""Listes simplement chaînées

TODO : 
Produire une version récursive de la fonction d’affichage 
Produire des fonctions calculant la taille de la liste en versions itératives et récursives
Tester pour des listes de taille vide, réduite à un élément ou plus longues
[BONUS] Permettre de pouvoir donner un nom à une liste
[BONUS] Ajouter un compteur permettant de savoir le nombre total de cellules produites pour gérer toutes les listes construites
"""

class Cellule:

    @classmethod
    def afficher_nombre_cellules_creees(cls):
        print("Nb de cellules créees : " + str(cls.nombre_cellules_creees))

    def __init__(self, val, suiv=None):
        self.valeur = val   
        self.suivant = suiv

class ListeChainee:
    def __init__(self, n=None):
        self.tete = None

    def est_vide(self):
        return self.tete is None

    def cellule_tete(self):
        return self.tete

    def inserer_tete(self, val):
        nouvelle = Cellule(val, self.tete) 
        self.tete = nouvelle

    def supprimer_tete(self):      
        if self.tete is not None: 
            seconde = self.tete.suivant
            self.tete = seconde

    def afficher(self):
        courant = self.tete
        while courant is not None:
            print(courant.valeur, end=" -> ")
            courant = courant.suivant
        print("None")

    def afficher_recursif(self):
        def afficher_aux(cell) : 
            if cell is not None:
                print(cell.valeur, end=" -> ")
                afficher_aux(cell.suivant)
            else:
                print(None)

        if self.tete is None: 
            print("Liste vide !")
        else:
            afficher_aux(self.tete)

    # Nombre de cellules en version itérative
    def longueur(self):
        l = 0
        courant = self.tete
        while courant is not None:
            courant = courant.suivant
            l += 1
        return l

    # Nombre de cellules en version récursive
    # utilisation d'une fonction locale
    def longueur_recursif(self):
        def longueur_rec(cell, l): 
            if cell.suivant is not None:
                return longueur_rec(cell.suivant, l + 1)
            else:
                return l
                
        if self.tete is None: 
            return 0
        else :
            return longueur_rec(self.tete, 1)   


    def inserer_queue(self, val):
        nouvelle = Cellule(val)

        if self.tete is None:
            self.tete = nouvelle
            return

        courant = self.tete

        while courant.suivant is not None:
            courant = courant.suivant

        courant.suivant = nouvelle

    def inserer_queue_recursif(self, val):
        def inserer_rec(noeud):
            # Cas de base : fin de la liste
            if noeud is None:
                return Cellule(val)

            # Appel récursif
            noeud.suivant = inserer_rec(noeud.suivant)
            return noeud

        self.tete = inserer_rec(self.tete)


    def supprimer_queue(self):
        # Cas 1 : liste vide
        if self.tete is None:
            return

        # Cas 2 : un seul élément
        if self.tete.suivant is None:
            self.tete = None
            return

        # Cas 3 : plusieurs éléments
        courant = self.tete

        while courant.suivant.suivant is not None:
            courant = courant.suivant

        courant.suivant = None
    
    def supprimer_queue_recursif(self):
        def supprimer(noeud):
            # Cas 1 : liste vide
            if noeud is None:
                return None

            # Cas 2 : dernier élément
            if noeud.suivant is None:
                return None

            # Cas récursif
            noeud.suivant = supprimer(noeud.suivant)
            return noeud

        self.tete = supprimer(self.tete)



def tests():
    """"""
    L = ListeChainee()
    L.inserer_tete(10)
    L.inserer_tete(20)
    L.inserer_tete(30)

    # L1 = ListeChainee()
    # L1.inserer_tete(1)
    
    # L2 = ListeChainee()

    # L.afficher()
    # L1.afficher()
    # L2.afficher()

    # L.afficher_recursif()
    # L1.afficher_recursif()
    # L2.afficher_recursif()

    # print(L.longueur())
    # print(L1.longueur())
    # print(L2.longueur())

    # print(L.longueur_recursif())
    # print(L1.longueur_recursif())
    # print(L2.longueur_recursif())

    # L.supprimer_tete(); L.afficher()
    # L.supprimer_tete(); L.afficher()
    # L.supprimer_tete(); L.afficher()
    # L.supprimer_tete(); L.afficher()

    # L.inserer_tete(1); L.afficher()
    # L.inserer_tete(2); L.afficher()
    # L.inserer_tete(3); L.afficher()
    
    # # BONUS
    L.supprimer_queue(); L.afficher()
    # L.supprimer_queue(); L.afficher()
    # L.supprimer_queue(); L.afficher()
    # L.supprimer_queue(); L.afficher()

    # L.inserer_queue(1); L.afficher()
    # L.inserer_queue(2); L.afficher()
    # L.inserer_queue(3); L.afficher()

    # L.supprimer_queue_recursif(); L.afficher()
    # L.supprimer_queue_recursif(); L.afficher()
    # L.supprimer_queue_recursif(); L.afficher()
    # L.supprimer_queue_recursif(); L.afficher()

    # L.inserer_queue_recursif(1); L.afficher()
    # L.inserer_queue_recursif(2); L.afficher()
    # L.inserer_queue_recursif(3); L.afficher()


if __name__ == "__main__":
    tests()
