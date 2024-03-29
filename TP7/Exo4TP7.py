#Exo 4 TP7

from abe import *

A1 = arbre('+',arbre('*',1,2),arbre('/',arbre('+',3,4),5))

def miroir(A):
    
    if est_feuille(A):
        return A
    else:
        return arbre(racine(A),miroir(fd(A)),miroir(fg(A)))
    
