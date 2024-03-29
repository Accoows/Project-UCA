#Exo 3 TP7

from abe import *

A1 = arbre('+',arbre('*',1,2),arbre('/',arbre('+',3,4),5))

def compter(A, op):
    if est_feuille(A):
        return 0
    else:
        Ag = compter(fg(A),op)
        Ad = compter(fd(A),op)
        if racine(A) == op:
            return 1 + Ag + Ad
        else:
            return Ag + Ad
        
def remplacer(A, op1, op2):
    if est_feuille(A):
        return A
    else:
        Ag = remplacer(fg(A),op1,op2)
        Ad = remplacer(fd(A),op1,op2)
        if racine(A) == op1:
            op = op2
        else:
            op = racine(A)
        return arbre(op,Ag,Ad)