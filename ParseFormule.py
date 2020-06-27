# coding=utf-8

# fonction pour parser des formules propositionnelles
# auteur : J. Lieber
# date : 07/07/19
# (Code affreux, mais vite fait... Je sais : c'est mal.)
# (Une façon propre de faire ça aurait été d'utiliser un
#  parser et une grammaire...)

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

# ch : str, une chaîne de caractères codant une formule de façon préfixée
# sortie : une instance de Formule représentée par ch
# (Code affreux, mais vite fait... Je sais : c'est mal.)
def exec(ch) :
    # ch2, rac, param, param1, param2 : str
    ch2 = ch.replace(" ", "")
    if ch2.find("(") == -1 :
        return parse_arite0(ch2)
    [rac, param] = ch2.split("(", 1)
    # rac est la chaîne avant la première occurrence de "(",
    # param est la chaîne commençant après cette 1ère occurrence de "("
    rac = rac.upper()
    param = param.upper()
    if rac == "" :
        raise Exception ("Erreur de parseur : racine vide !")
    if param[-1] != ")" :
        raise Exception("Erreur de parseur : une parenthèse fermante "
                        + "manquante ! (param = \"" + param + "\")")
    param = param[0:-1]
    if rac == "NON" : # on doit donc avoir une formule d'arité 1
        return parse_arite1(rac, param)
    ## [param1, param2] = param.split(",", 1) # ne marche pas !
    param1, param2 = separer_avec_virgule_au_niveau1(param)
    return parse_arite2(rac, param1, param2)

# ch : chaîne sans parenthèse ouvrante sensée coder une
#      formule d'arité 0
# sortie : FormuleArite0
def parse_arite0(ch) :
    if ch == "TOP" :
        return top
    if ch == "BOT" :
        return bot
    return Variable(ch)

# rac, param : chaines sensées coder une formule d'arité 1
#      de la forme rac(param)
# sortie : FormuleArite1
def parse_arite1(rac, param) :
    # op : Formule
    if rac != "NON" :
        raise Exception("Erreur de parseur : le seul connecteur unaire implanté est la négation !")
    op = exec(param)
    return Non(op)

# rac, param1, param2 : chaines sensées coder une formule d'arité 2
#      de la forme rac(param1, param2)
# sortie : FormuleArite1
def parse_arite2(rac, param1, param2) :
    # tabFA2 : tableau des classes de Formules d'arité 2
    # Cform : formule d'arité 2
    tabFA2 = [Et, Ou, Implique, EquivalentA, OuEx]
    if rac not in map(lambda C : C.symbole.upper(), tabFA2) :
        raise Exception("Erreur de parseur : connecteur binaire inconnu :", rac, "!")
    op1 = exec(param1)
    op2 = exec(param2)
    Cform = None
    for C in tabFA2 :
        if C.symbole.upper() == rac :
            Cform = C
            break
    return C(op1, op2)

# param : une chaîne qui est sensée être de la forme param1 + "," + param2
#         où param1 et param2 représentent des formules et donc, la virgule
#         qui les sépare est au niveau 1 dans l'arbre.
# sortie : couple de chaînes (param1, param2)
# exemple : Si param = "et(a, b), non(c)" alors param1= "et(a, b)"
#           et param2 = "non(c)".
def separer_avec_virgule_au_niveau1(param) :
    # i, iVirgule, profondeur : int
    # c : str (représentant un seul caractère)
    # param1, param2 : str
    profondeur = 0
    iVirgule = -1
    for i in range(len(param)) :
        c = param[i]
        if c == "(" :
            profondeur += 1
        if c == ")" :
            profondeur -= 1
        if profondeur == 0 and c == "," :
            iVirgule = i
    if iVirgule == -1 :
        raise Exception("Erreur de parseur : arguments de connecteurs "
                        + "binaires mal formés !")
    param1 = param[: iVirgule]
    param2 = param[iVirgule + 1 :]
    return param1, param2

