#Exo 3 TP6

dico = []
L = []

def extraire_dictionnaire():
    fichier = open("dictionnaire.txt","r",encoding="utf-8")
    for ligne in fichier:
        dico.append(ligne[:-1])
    fichier.close()
    return dico

def afficher(n):
    global dico
    extraire_dictionnaire()
    for i in range(0,n):
        print(i,dico[i],len(dico[i]))
        
def longueurs_mots():
    global dico
    extraire_dictionnaire()
    for longueurs in dico:
        L.append(len(longueurs))
    
def longueur_max():
    global dico
    max_mots = 0
    for i in range(len(dico)):
        if len(dico[i]) > max_mots:
            max_mots = len(dico[i])
    return max_mots

extraire_dictionnaire()

def plus_longs():
    global dico
    pl_mots = longueur_max()
    for i in range(len(dico)):
        if len(dico[i]) == pl_mots :
            print(dico[i])