#Exo 3 TP5

def produit_externe(k,L):
    M = []
    for i in range(len(L)):
        M.append(k * L[i])
    return M

k = 2
L = [1,2,3]
    
def produit_externe2(k,L):
    return [k * L[i] for i in range(len(L))]