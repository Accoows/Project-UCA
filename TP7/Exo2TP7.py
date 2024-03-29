# Exo 1 TP 7

from abe import *

A = arbre('+',arbre('*',1,2),arbre('/',arbre('+',3,4),5))

def contient42(A):
    if est_feuille(A):
        return A == 42
    else:
        Ag = contient42(fg(A))
        Ad = contient42(fd(A))
        return Ag or Ad
    
def compte_pairs(A):
    if est_feuille(A):
        if A%2 == 0:
            return 1
        else:
            return 0
    else:
        Ag = compte_pairs(fg(A))
        Ad = compte_pairs(fd(A))
        return Ag + Ad
    
def feuilles_pairs(A):
    if est_feuille(A):
        if A%2 == 0:
            return [A]
        else:
            return []
    else:
        Ag = feuilles_pairs(fg(A))
        Ad = feuilles_pairs(fd(A))
        return Ag + Ad
    
def liste_profondeur(A,n):
    if est_feuille(A):
        return []
    else:
        if n == 0:
            return [racine(A)]
        else:
            Ag = liste_profondeur(fg(A), n-1)
            Ad = liste_profondeur(fd(A), n-1)
            return Ag + Ad
        
def profondeur_max_pair(A):
    if est_feuille(A):
        if A%2==0:
            return 0
        else:
            return None
    else:
        Ag = profondeur_max_pair(fg(A))
        Ad = profondeur_max_pair(fd(A))
        if Ag==None and Ad==None:
            return None
        elif Ag==None:
            return Ad+1
        elif Ad==None:
            return Ag+1
        else:
            return max(Ag,Ad)+1 #+1 pour la racine