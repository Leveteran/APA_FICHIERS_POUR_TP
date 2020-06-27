# coding=utf-8

# classe des formules propositionnelles dont la racine
# est un connecteur binaire d'implication.
# auteur : J. Lieber
# date : 04/07/19

from FormuleBinaire import *

class Implique(FormuleBinaire):
    "classe des formules binaires dont la racine est une implication"

    symbole = "=>"

    def __init__(self, op1, op2):
        FormuleBinaire.__init__(self, Implique.symbole, op1, op2)

    # self : Formule
    # interp : Interpretation
    # sortie : bool (teste si interp satisfait self)
    def est_satisfaite_par(self, interp) :
        return not self.get_oper1().est_satisfaite_par(interp) \
               or self.get_oper2().est_satisfaite_par(interp)
