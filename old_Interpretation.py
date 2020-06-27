# coding=utf-8

# classe des interprétations dans la sémantique classique de
# la logique propositionnelle finie
# auteur : J. Lieber
# date : 09/07/19

from Variable import *

class Interpretation :
    "classe des interprétations (affectation de variables par des booléens)"

    code = None # variable contenant le dictionnaire

    def get_code(self) :
        return self.code

    def set_code(self, c) :
        self.code = c

    # self : Interpretation
    # param : initialisation, soit par un "dict",
    #         soit par une "list" auquel cas, valeurs associées par
    #         défaut aux variables : False
    def __init__(self, param) :
        if type(param) == dict :
            self.set_code(param)
            return
        if type(param) != list :
            raise Exception("Paramètre param du constructeur d'" +
                            "Interpretation n'est ni un dictionnaire " +
                            "ni une liste")
        self.set_code({})
        for v in param :
            if type(v) == str :
                var = Variable(v)
            else :
                  var = v  
            self.ajF(var)

    # self : Interpretation
    # sortie : les variables dans un "dict_keys"
    def variables (self) :
        return self.get_code().keys()

    def __str__(self) :
        # ch : str
        ch = "("
        for var in self.variables() :
            ch += var.nom() + "<-" \
                  + ("V" if self.acces(var) else "F") \
                  + " "
        if len(self.variables()) == 0 :
            return "Interprétation vide"
        return ch[:-1] + ")"

    def __iter__(self) :
        return self

    def next(self) :
        # val, sortie_par_break : bool
        sortie_par_break = False
        for var in reversed(self.variables()) :
            val = self.acces(var)
            self.ajout(var, not var)
            if self.acces(var) : # i.e., on a un False changé en True
                sortie_par_break = True
                break
        if not sortie_par_break :
            raise StopIteration

    # self : Interpretation
    # var : Variable
    # val : bool
    def ajout(self, var, val) :
        self.get_code()[var] = val

    # self : Interpretation
    # var : Variable
    def ajV(self, var) :
        self.ajout(var, True)

    # self : Interpretation
    # var : Variable
    def ajF(self, var) :
        self.ajout(var, False)

    # self : Interpretation
    # var : Variable
    # sortie : bool
    def acces(self, var) :
        return self.get_code()[var]

    # self : Interpretation
    # phi : Formule
    # sortie : bool (True ssi self satisfait phi)
    def satisfait(self, phi) :
        return phi.est_satisfaite_par(self)
