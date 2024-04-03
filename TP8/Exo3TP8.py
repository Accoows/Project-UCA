#Exo 3 TP8

from pnm import *
from Exo2TP8 import *

#voir_fichier('space-invader-pieuvre.pbm')

def dimensions(M):
    return (len(M),len(M[0]))


def matrice_vide(n,m):
    return [ [None] * m for i in range(n)]


def ajoute_horizontal(M1,M2):
    (n1,m1) = dimensions(M1)
    (n2,m2) = dimensions(M2)
    M = matrice_vide(n1,m1+m2)
    for i in range(n1):
        for j in range(m1):
            M[i][j] = M1[i][j]
        for j in range(m2):
            M[i][j+m1] = M2[i][j]
    return M

    
def répète_horizontal(M,n):
    mat = M
    for i in range(1,n):
        mat = ajoute_horizontal(mat,M)
    return mat

def ajoute_vertical_centré(M1,M2):
    (n1,m1) = dimensions(M1)
    (n2,m2) = dimensions(M2)
    n = n1+n2
    m = max(m1,m2)
    M=matrice_vide(n,m)
    delta1 = (m-m1)//2 # L’écart à ajouter au début pour centrer la matrice Mk
    delta2 = (m-m2)//2 # Remarque si Mk est la plus grande, deltak sera nul (k=1 ou 2)
    for i in range(n1):
        for j in range(m1):
            M[i][j+delta1] = M1[i][j]
    for i in range(n2):
        for j in range(m2):
            M[i+n1][j+delta2] = M2[i][j]
    return M
        
        
def army(nblignes, nbpieuvres, nbsoucoupes):
    M1 = fichier_vers_matrice('space-invader-pieuvre.pbm')
    M2 = fichier_vers_matrice('space-invader-soucoupe.pbm')
    M1 = répète_horizontal(M1,nbpieuvres)
    M2 = répète_horizontal(M2,nbsoucoupes)
    M = M1
    for i in range(1, nblignes):
        if i%2 == 0:
            M = ajoute_vertical_centré(M,M1)
        else:
            M = ajoute_vertical_centré(M,M2)
    return M
 
################################################ 
 
# Partie Ajoute Horizontal :
#M = fichier_vers_matrice('space-invader-pieuvre.pbm')
#M2 = ajoute_horizontal(M,M)
#M3 = ajoute_horizontal(M2,M)
#matrice_vers_fichier(M3, 'space-invader-3-pieuvres.pbm')

#affiche_matrice_booléens(M2,'#','.')
#affiche_matrice_booléens(M3,'#','.')

# Partie Répète :

#M20 = répète_horizontal(M,20)
#matrice_vers_fichier(M20,'space-invader-20-pieuvres.pbm')
#voir_fichier('space-invader-20-pieuvres.pbm')

# Partie Ajoute Vertical : 
M1 = fichier_vers_matrice('space-invader-pieuvre.pbm')
#matrice_vers_fichier(M1,'space-invader-test.pbm')
M2 = fichier_vers_matrice('space-invader-soucoupe.pbm')
M3 = ajoute_vertical_centré(M1,M2)
affiche_matrice_booléens(M3,'#','.')
matrice_vers_fichier(M3, 'space-invader-vertical.pbm')