# coding=utf-8

# classe des formules propositionnelles dont la racine
# est un OU.
# auteur : J. Lieber
# date : 09/07/19

from FormuleBinaire import *

class Ou(FormuleBinaire):
    "classe des disjonctions binaires"

    symbole = "OU"

    def __init__(self, op1, op2):
        FormuleBinaire.__init__(self, Ou.symbole, op1, op2)

    # self : Formule
    # interp : Interpretation
    # sortie : bool (teste si interp satisfait self)
    def est_satisfaite_par(self, interp) :
        return self.get_oper1().est_satisfaite_par(interp) or \
               self.get_oper2().est_satisfaite_par(interp)
