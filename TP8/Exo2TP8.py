#Exo 2 TP8

from pnm import *

M1 = fichier_vers_matrice('space-invader-pieuvre.pbm')
M2 = fichier_vers_matrice('space-invader-soucoupe.pbm')

def dimensions(M):
    return (len(M), len(M[0]))

def affiche_matrice_booléens(M,plein,vide):
    (n,m) = dimensions(M)
    for i in range(n):
        for j in range(m):
            if M[i][j] == True:
                print(plein, sep='', end='')
            else:
                print(vide, sep='', end='')
        print()
                
                