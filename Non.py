# coding=utf-8

# classe des formules propositionnelles dont la racine
# est la négation logique.
# auteur : J. Lieber
# date : 09/07/19

from FormuleUnaire import *

class Non(FormuleUnaire) :
    "classe des formules propositionnelles dont la racine est non"

    symbole = "NON"

    def __init__(self, op):
        FormuleUnaire.__init__(self, Non.symbole, op)
        self.set_oper(op)

    # self : Formule
    # interp : Interpretation
    # sortie : bool (teste si interp satisfait self)
    def est_satisfaite_par(self, interp) :
        return not self.get_oper().est_satisfaite_par(interp)
