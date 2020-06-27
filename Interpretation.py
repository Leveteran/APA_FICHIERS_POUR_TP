# coding=utf-8

# classe des interprétations dans la sémantique classique de
# la logique propositionnelle finie
# auteur : J. Lieber
# date : 09/07/19

from Variable import *

import ParseFormule

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
    # val_defaut : si param est une "list", on associe à chaque élément
    #              val_defaut comme valeur par défaut
    def __init__(self, param = None, val_defaut = False) :
        if param is None :
            return
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
            self.ajout(var, val_defaut)

    # self : Interpretation
    # sortie : les variables dans une "list"
    #          (qui est renversable, contrairement à un "dict_keys")
    def variables (self) :
        return list(self.get_code().keys())

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
    # sortie : Interpretation
    def clone(self) :
        # codeClone : dict
        # copie : Interpretation
        codeClone = dict(self.get_code())
        copie = Interpretation()
        copie.set_code(codeClone)
        return copie

    # self : Interpretation
    # phi : Formule
    # sortie : bool (True ssi self satisfait phi)
    def satisfait(self, phi) :
        return phi.est_satisfaite_par(self)

    # self : Intepretation
    # vars : liste des variables de self (pour ne pas les recalculer)
    # sortie : Interpretation (la suivante au sens où si self et sortie codent
    #          des entiers naturels en binaire alors sortie code le code de self + 1)
    #          si on dépasse l'interprétation " toutes à True " : retourne None
    def suivante(self, vars = None) :
        # var : Variable
        # sortie_par_break : bool
        # suiv : Interpretation
        if vars is None :
            vars = self.variables()
        suiv = self.clone()
        sortie_par_break = False
        for var in reversed(vars) :
            val = suiv.acces(var)
            suiv.ajout(var, not val)
            if suiv.acces(var) : # i.e., on a un False changé en True
                sortie_par_break = True
                break
        if not sortie_par_break :
            return None
        return suiv

    # vars : liste de variables (ou de chaînes de caractères représentant des variables)
    # interp_init : Interpretation (si None : on prend l'interprétation " toutes à faux ")
    # yield : toutes les interprétations partant de interp_init jusqu'à " toutes à True "
    @staticmethod
    def iterateur_interpretations(vars, interp_init = None) :
        if not vars : # i.e., vars est la liste vide
            return
        if type(vars[0]) is str : # si ce ne sont pas des variables mais des chaînes, on convertit.
            for i in range(len(vars)) :
                vars[i] = Variable(vars[i])
        if interp_init is None :
            interp_init = Interpretation(vars, False)
        interp = interp_init
        while True : # pas de do ... while en Python...
            yield interp
            interp = interp.suivante(vars)
            if interp == None :
                break

    # phi : Formule ou chaîne la représentant
    # effet : affiche la table de vérité de phi
    @staticmethod
    def table_verite(phi) :
        if type(phi) == str :
            phi = ParseFormule.exec(phi)
        for interp in Interpretation.iterateur_interpretations(list(phi.get_variables())) :
            print(interp, "\t", interp.satisfait(phi))
