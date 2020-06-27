# coding=utf-8

# classe des formules propositionnelles dont la racine
# est un connecteur binaire d'équivalence
# auteur : J. Lieber
# date : 09/09/19

from FormuleBinaire import *

class EquivalentA(FormuleBinaire):
    "classe des formules dont la racines sont des équivalences"

    symbole = "<=>"

    def __init__(self, op1, op2):
        FormuleBinaire.__init__(self, EquivalentA.symbole, op1, op2)

    # self : Formule
    # interp : Interpretation
    # sortie : bool (teste si interp satisfait self)
    def est_satisfaite_par(self, interp) :
        return self.get_oper1().est_satisfaite_par(interp) \
               == self.get_oper2().est_satisfaite_par(interp)

