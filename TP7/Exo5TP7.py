#Exo 5 TP7 

from pile import *
from abe import *

L = [1,2,'-',3,4,'+','*']

def arboriser(L):
    NP = nouvelle_pile()
    for i in L:
        if str(i) in "+-/*":
            n = depile(NP)
            m = depile(NP)
            empile(NP,arbre(i,m,n))
        else:
            empile(NP,i)
    return depile(NP)

def valeur(A): # l'arbre A doit être arithmétique
    if est_feuille(A):
        return A
    else:
        r = racine(A)
        vg = valeur(fg(A))
        vd = valeur(fd(A))
        if r == '+' : return vg + vd
        if r == '-' : return vg - vd
        if r == '*' : return vg * vd
        if r == '/' : return vg / vd

def calcul(L):
    return valeur(arboriser(L))
    
    
    
################################    
def valeur_direct(m,vg,vd):
    if m == '+' : return vg + vd
    if m == '-' : return vg - vd
    if m == '*' : return vg * vd
    if m == '/' : return vg / vd
    
def calcul_direct(L):
    NP2 = nouvelle_pile()
    for i in L:
        if est_feuille(A):
            n = depile(NP2)
            m = depile(NP2)
            empile(NP2,valeur_direct(i,m,n))
        else:
            empile(NP2,i)
    return depile(NP2)
    