# coding=utf-8

# classe des formules propositionnelles
# auteur : J. Lieber
# date : 09/07/19

class Formule :
    "classe des formules propositionnelles"
    racine = None
    variables = None # variables obtenues par un réflexe si-besoin
                     # cf. méthode recolte_variables

    def get_racine(self) :
        return self.racine

    def set_racine(self, rac) :
        self.racine = rac

    def __init__(self, rac) :
        self.set_racine(rac)

    # self : Formule
    # sortie : set (ensemble des variables apparaissant dans self)
    def get_variables(self) :
        if self.variables is None :
            return self.recolte_variables()
        return self.variables

    # self : Formule
    # sortie : str (représentant l'ensemble des variables)
    def str_variables(self) :
        # vars : set
        vars = self.get_variables()
        return set(map(lambda v : v.nom(), vars)).__str__()

    def str_prefixe(self) :
        return self.get_racine()

    # self : Formule
    # sortie : set (ensemble des variables apparaissant dans self)
    # (calculée dans des sous-classes indirectes)
    def recolte_variables(self) :
        raise Exception("La classe Formule est abstraite : " +
                        "une instance directe de cette classe ne peut " +
                        "pas avoir un ensemble de variables.")

    # self : Formule
    # interp : Interpretation
    # sortie : bool (teste si interp satisfait self)
    # Attention, n'est pas prudent : si self contient une variable non
    # affectée par interp, cela générera une erreur
    # (le test prendrait du temps...).
    def est_satisfaite_par(self, interp) :
        raise Exception("La classe Formule est abstraite : " +
                        "une instance directe de cette classe ne peut " +
                        "pas être satisfaite ou non par une interprétation.")
