def majuscules(f):
    f1 = f[0:len(f)-4] + "-maj.txt"
#    f1 = ''
#    for i in range(0,len(f)-4):
#        f1 = f1 + f[i]
#    f1 += '-maj.txt'
    old = open(f,'r', encoding='utf_8')
    new = open(f1,'w', encoding='utf_8')
    for L in old:
        new.write(L.upper())
    old.close()
    new.close()
    
#############################
    
def nombres_lignes(s):
    try:
        fichier = open(s,'r', encoding='utf_8')
        res = 0
        for nb in fichier:
            res = res + 1
        return res
        fichier.close()
    except FileNotFoundError or PermissionError:
        return -1
    
################################# 
 
def minimum(L):
    m = L[0]
    for i in m:
        if i < m:
            m = i
    return i

def maximum(L):
    m = L[0]
    for i in m:
        if i > m:
            m = i
    return i

def moyenne(L):
    m = 0
    for i in L:
        m = m + i
    return m/len(L)


##########################


inv = [('Pommes',10),('Carottes',5),('Radis',23),('Lentilles',534),('Poivrons',12)]


def maj_inventaire(inv,produit,n):
    for reserv in range(len(inv)):
        (p,q) = inv[reserv]
        if p == produit:
            inv[reserv] = (p,q-n)
    print(inv)
    
def maj_inventaire2(inv,produit,n):
    for reserv in range(len(inv)):
        (p,q) = inv[reserv]
        if p == produit:
            if q-n < 0:
                raise ValueError
            else:
                inv[reserv] = (p,q-n)
                return
    raise IndexError
    print(inv)
    
def achat(inv,produit,n):
    try:
        maj_inventaire2(inv,produit,n)
        print("Merci pour votre achat.")
    except ValueError:
        print("Produit en quantité insuffisante")
    except IndexError:
        print("Produit inexistant")
        
        
###################################
        
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
    for longueurs in dico:
        L.append(len(longueurs))
    

def longueur_max(dict):
    global L
    max_mots = [len(dict[0]),dict[0]]
    for i in dict:
        if len(i)