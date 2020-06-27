# coding=utf-8

# classe des formules propositionnelles dont la racine
# est un connecteur unaire
# auteur : J. Lieber
# date : 08/07/19

from Formule import *

class FormuleUnaire(Formule) :
    "classe des formules propositionnelles unaires"
    oper = None # opérande

    def __init__(self, rac, op):
        Formule.__init__(self, rac)
        self.set_oper(op)

    def get_oper(self) :
        return self.oper

    def set_oper(self, op) :
        self.oper = op

    def str_prefixe(self):
        str = Formule.str_prefixe(self)
        str += "("
        str += self.get_oper().str_prefixe()
        str += ")"
        return str

    # self : FormuleArite0
    # sortie : set
    # effet de bord : positionne l'attribut variables
    def recolte_variables(self) :
        # V : set
        V = self.get_oper().get_variables()
        self.variables = V
        return V
