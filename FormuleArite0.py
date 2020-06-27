# coding=utf-8

# classe des formules propositionnelles d'arité 0
# (variable ou connecteur d'arité 0)
# auteur : J. Lieber
# date : 09/07/19

from Formule import *

class FormuleArite0(Formule) :
    "classe des formules propositionnelles d'arité 0"

    # self : FormuleArite0
    # sortie : set
    # Effet de bord : affecte à l'attribut variables l'ensemble vide.
    # Attention : est redéfini dans la sous-classe Variable
    def recolte_variables(self) :
        # V : set
        V = set() # ensemble vide
        self.variables = V
        return V
    
    # self : Formule
    # interp : Interpretation
    # sortie : bool (test si interp satisfait self)
    def est_satisfaite_par(self, interp) :
        if self is top :
            return True
        return False # dans le cas de bot, pour les instances de
                     # Variable, c'est redéfini dans la sous-classe
                     # Variable.

top = FormuleArite0("TOP")
bot = FormuleArite0("BOT")
