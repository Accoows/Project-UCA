##############################################################
##                                                          ##
##  Module pour manipuler des arbres binaire d’expression   ##
##                                                          ##
##############################################################



def arbre(r, Ag, Ad):
    """
    Construit un arbre à partir d’une racine et de deux arbres.
    """
    return (r, Ag, Ad)


def est_opérateur(obj):
    """
    Un opérateur est un nœud interne de l’arbre.
    Les seules valeurs autorisées sont les 4 opérations : + - * /
    """
    return obj in ['+', '*', '-', '/']


def est_feuille(A):
    """
    Regarde si l’arbre A est composé ou s’il est une simple feuille.
    Une feuille est soit un entier soit une chaîne de caractère.
    """
    return type(A) == int or type(A) == str


def racine(A):
    """ 
    Renvoie la racine de l’arbre A
    A doit être un arbre composé et non une feuiile
    """
    if est_feuille(A):
        raise ValueError("une feuille n’a pas de racine")
    return A[0]


def fg(A):
    """ 
    Renvoie le fils gauche de l’arbre A
    A doit être un arbre composé et non une feuiile
    """
    if est_feuille(A):
        raise ValueError("une feuille n’a pas de fils gauche")
    return A[1]


def fd(A):
    """ 
    Renvoie le fils droit de l’arbre A
    A doit être un arbre composé et non une feuiile
    """
    if est_feuille(A):
        raise ValueError('une feuille n’a pas de fils droit')
    return A[2]

