# coding=utf-8

# Fonctions testant les fonctionnalité de
# Formule et de ses sous-classes
# auteur : J. Lieber
# date : 08/07/19

from Formule import *
from FormuleBinaire import *
from Et import *
from Ou import *
from Implique import *
from EquivalentA import *
from OuEx import *
from FormuleUnaire import *
from Non import *
from FormuleArite0 import *
from Variable import *
from Interpretation import *

import ParseFormule

def sep() :
    print("\n====================\n")

def test_str_prefixe() :
    # phi, psi, mu : Formule
    print("TEST D'INSTANCIATIONS DE FORMULES ET DE str_prefixe")
    phi = Et(Variable("a"),
             Ou(Variable("b"), Variable("c")))
    print("phi =", phi.str_prefixe())
    a = Variable("a")
    b = Variable("b")
    psi = Non(a)
    psi = OuEx(a, b)
    psi = Implique(a, b)
    psi = Ou(Non(a), b)
    psi = Non(OuEx(Implique(a, b), Ou(Non(a), b)))
    print("psi =", psi.str_prefixe())
    mu = EquivalentA(Non(top), bot)
    print("mu =", mu.str_prefixe())

def test_parseur() :
    # ch1, ch2, ch3 : str
    # phi1, phi2, phi3 : Formule
    print("TEST DU PARSEUR")
    ch1 = "et(a, =>(b, non(a)))"
    phi1 = ParseFormule.exec(ch1)
    print("ch1  =", ch1)
    print("phi1 =", phi1.str_prefixe())
    ch2 = "<=>(non(et(a, b)), ou(non(a), non(b)))"
    phi2 = ParseFormule.exec(ch2)
    print("ch2  =", ch2)
    print("phi2 =", phi2.str_prefixe())
    ch3 = "et(top, x)"
    phi3 = ParseFormule.exec(ch3)
    print("ch3  =", ch3)
    print("phi3 =", phi3.str_prefixe())


# Test d'une fonction auxiliaire du parseur
def test_separer_avec_virgule_au_niveau1() :
    print("TEST DE ParseFormule.separer_avec_virgule_au_niveau1")
    param = "et(a, b), non(c)"
    param1, param2 = ParseFormule.separer_avec_virgule_au_niveau1(param)
    print("param = \"", param, "\"", sep = "")
    print("param1 = \"", param1, "\"", sep = "")
    print("param2 = \"", param2, "\"", sep = "")

# Test de la méthode get_variables (réflexe si-besoin)
def test_variables() :
    # phi1, phi2 : Formule
    print("TEST DE LA METHODE get_variables")
    phi1 = Et(Variable("a1"),
              Ou(Non(Variable("A1")),
                 Variable("a2")))
    print("phi1 =", phi1.str_prefixe())
    print("V(phi1) =", phi1.get_variables())
    print("V(phi1) =", phi1.str_variables())
    phi2 = ParseFormule.exec("et(a, ou(B, non(=>(bot, A))))")
    print("phi2 =", phi2.str_prefixe())
    print("V(phi2) =", phi2.get_variables())
    print("V(phi2) =", phi2.str_variables())

# Tests de méthodes de base de la classe Interpretation
def test_interpretations() :
    # interp : Interpretation
    # phi : Formule
    print("TEST SUR LES INTERPRETATIONS")
    phi = ParseFormule.exec("et(a, non(ou(b, c)))")
    print("phi =", phi.str_prefixe())
    interp = Interpretation(["a", "b", "c"])
    print("interp =", interp, "satisfait-elle phi ?", interp.satisfait(phi))
    interp.ajV(Variable("b"))
    print("interp =", interp, "satisfait-elle phi ?", interp.satisfait(phi))
    interp.ajV(Variable("a"))
    print("interp =", interp, "satisfait-elle phi ?", interp.satisfait(phi))
    interp.ajF(Variable("b"))
    print("interp =", interp, "satisfait-elle phi ?", interp.satisfait(phi))

#Test sur les itérations des interprétations
def test_iteration_sur_interpretations():
    # interp : Interpretation
    # i : int
    # ch : str
    print("TEST SUR LES ITERATIONS SUR LES INTERPRETATIONS")
    i = 1
    for interp in Interpretation.iterateur_interpretations(["a", "b", "c"]) :
        print("interp", i, " = ", interp, sep = "")
        i = i + 1
    for ch in ["TOP", "BOT", "a", "NON(a)", "ET(a, b)", "OU(a, b)",\
               "=>(A, B)", "<=>(A, B)", "<+>(A, B)",
               "=>(=>(A, =>(B, C)), =>(=>(A, B), =>(A, C)))"] :
        print("\nTable de vérité de", ch, ":")
        Interpretation.table_verite(ch)

def tests() :
    test_str_prefixe()
    sep()
    test_separer_avec_virgule_au_niveau1()
    sep()
    test_parseur()
    sep()
    test_variables()
    sep()
    test_interpretations()
    sep()
    test_iteration_sur_interpretations()

tests()
