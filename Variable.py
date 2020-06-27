# coding=utf-8

# classe des variables propositionnelles
# auteur : J. Lieber
# date : 09/07/19

from FormuleArite0 import *

class Variable (FormuleArite0) :
    "classe des variables propositionnelles"

    # rac : str
    # Impose que les variables soient stockées en minuscules
    def set_racine(self, rac) :
        self.racine = rac.lower()

    def nom(self):
        return self.get_racine()

    def __str__(self) :
        return self.nom()

    def str_prefixe(self) :
        return Formule.str_prefixe(self)

    # Egalité entre deux variables : il faut et il suffit
    # qu'elles aient le même nom, sans tenir compte de la casse.
    # Par exemple Variable("aB").equals(Variable("Ab")) donne True.
    def __eq__(self, x):
        return isinstance(x, Variable) \
               and self.nom() == x.nom()

    # self : Variable
    # sortie : entier
    def __hash__(self) :
        return self.nom().__hash__()

    # self : FormuleArite0
    # sortie : set
    # effet de bord : positionne l'attribut variables
    def recolte_variables(self) :
        # V : set
        V = set()
        V.add(self)
        # V.add(self.nom())
        self.variables = V
        return V

    # self : Formule
    # interp : Interpretation
    # sortie : bool (teste si interp satisfait self)
    def est_satisfaite_par(self, interp) :
        return interp.acces(self)
