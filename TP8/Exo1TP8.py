#Exo 1 TP8

from pnm import *
#voir_fichier('space-invader-pieuvre.pbm', quadrillage=True)
#voir_fichier('space-invader-soucoupe.pbm', quadrillage=True)
#voir_fichier('space-invader-pieuvre-second.pbm', quadrillage=True)

#Renvoie False pour 0 ; et ; True pour 1 dans PBM
M = fichier_vers_matrice('space-invader-pieuvre.pbm')
#print(M)
M[3][4] = True #M[y][x]
matrice_vers_fichier(M,'space-invader-pieuvre2.pbm')
voir_fichier('space-invader-pieuvre2.pbm')

