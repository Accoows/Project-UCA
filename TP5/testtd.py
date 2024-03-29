def est_triée(L):
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return False
    return True

#assert est_triée([1,2,3,4,5,9]) == True
#assert est_triée([0,0,0,0,0]) == True

def grouper(L):
    if len(L) == 0:
        return []
    m = L[0]
    n = [m]
    for i in range(1,len(L)):
        if L[i] != m:
            m = L[i]
            n.append(m)
    return n
            
            
def compacter(L):
    if len(L) == 0:
        return []
    m = L[0]
    n = []
    compt = 1
    for i in range(1,len(L)):
        if L[i] != m:
            n.append((compt,m))
            m = L[i]
            compt = 1
        else:
            compt += 1
    n.append((compt,m))
    return n

###############################

def produit_externe(k, L):
    # Crée une nouvelle liste représentant le vecteur k * 𝑣⃗
    resultat = []
    for elem in L:
        resultat.append(k * elem)
    return resultat

# Exemple d'utilisation :
k = 2
vecteur = [1, 2, 3]

resultat_produit_externe = produit_externe(k, vecteur)
print(resultat_produit_externe)


##########################







def unique(x,L):
déjà_trouvé = False
for e in L:
if e==x and déjà_trouvé:
return False
elif e==x:
déjà_trouvé = True
return déjà_trouvé
def est_permutation(L):
n=len(L)
for e in L:
if not( 0<=e and e<n and unique(e,L)):
return False
return True