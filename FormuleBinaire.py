# coding=utf-8

# classe des formules propositionnelles dont la racine
# est un connecteur binaire
# auteur : J. Lieber
# date : 04/07/19

from Formule import *

class FormuleBinaire(Formule) :
    "classe des formules propositionnelles binaires"
    oper1 = None # 1er opérande
    oper2 = None # 2ème opérande

    def __init__(self, rac, op1, op2):
        Formule.__init__(self, rac)
        self.set_oper1(op1)
        self.set_oper2(op2)

    def get_oper1(self) :
        return self.oper1

    def set_oper1(self, op1) :
        self.oper1 = op1

    def get_oper2(self) :
        return self.oper2

    def set_oper2(self, op2) :
        self.oper2 = op2

    def str_prefixe(self):
        str = Formule.str_prefixe(self)
        str += "("
        str += self.get_oper1().str_prefixe()
        str += ", "
        str += self.get_oper2().str_prefixe()
        str += ")"
        return str

    # self : FormuleArite0
    # sortie : set
    # effet de bord : positionne l'attribut variables
    def recolte_variables(self) :
        # V : set
        V = self.get_oper1().get_variables()\
            .union(self.get_oper2().get_variables())
        self.variables = V
        return V
