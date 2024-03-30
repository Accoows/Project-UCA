#Exo 1 TP 8

from pnm import *
voir_fichier('space-invader-pieuvre.pbm' , quadrillage=True)
#voir_fichier('space-invader-soucoupe.pbm')
#voir_fichier('space-invader-pieuvre-test.pbm', quadrillage=True)

#M = voir_fichier('space-invader-pieuvre.pbm')
#print(M)

M = fichier_vers_matrice('space-invader-pieuvre.pbm')
M[3][4] = 1
matrice_vers_fichier(M,'space-invader-pieuvre2.pbm')
voir_fichier('space-invader-pieuvre2.pbm')

