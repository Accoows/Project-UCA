#Exo 5 TP 5

#non linéaire
def est_permutation0(L):
    for i in range(len(L)):
        if i not in L:
            return False
    return True

#linéaire
def est_permutation(L):
    trouve = [False]*len(L)
    for i in L:
        if not (0<=i and i<len(L)):
            return False
        elif trouve[i]:
            return False
        else:
            trouve[i] = True
    return True
        
    