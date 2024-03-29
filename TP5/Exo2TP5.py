# Exo 2 TP 5

def produit_scalaire(v1,v2):
    if len(v1) != len(v2):
        raise ValueError('Erreur de dimension')
    
    result = 0
    for i in range(len(v1)):
        result += v1[i]*v2[i]
    return result

###########
import math

def norme(v):
    prod_scal = produit_scalaire(v,v)
    norme_v = math.sqrt(prod_scal)
    return norme_v
    