#Test exo 6 TD

from abe import *

A = arbre('+',arbre('*',19,8),arbre('/',arbre('-',6,'x'),'y'))

def min_feuille(A):
    if est_feuille(A):
        if type(A) == int:
            return A
        else:
             raise ValueError("La feuille n'est pas entière (int)")
    else:
        try:
            Ag = min_feuille(fg(A))
        except:
            return min_feuille(fd(A))
        try:
            Ad = min_feuille(fd(A))
        except:
            return Ag
        return min(Ag,Ad)
    
