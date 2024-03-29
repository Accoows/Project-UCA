# Exo 1 TP 6

def nombre_définitions(s):
    compteur = 0
    fichier = open(s,'r', encoding='utf_8')
    for ligne in fichier:
        if ligne[:4] == 'def ':
            compteur += 1
    fichier.close()
    return compteur