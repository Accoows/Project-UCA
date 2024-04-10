#test 1 TD 9

def liste_nombre_occurences(L):
    N = [0] * (max(L)+1)
    for i in range(len(L)):
        m = L[i]
        N[m] = N[m] + 1
    return N

def crée_liste_triée1(N):
    Lt = []
    for i in range(len(N)):
        m = N[i]
        for j in range(m):
            Lt.append(i)
    return Lt

def crée_liste_triée2(N):
    Lt = []
    for i in range(len(N)):
        m = N[i]
        Lt += [i] * m
    return Lt

def crée_liste_triée2(N):
    Lt = [0]*sum(N)
    k = 0
    for i in range(len(N)):
        for machin in range(N[i]):
            Lt[k] = i
            k=k+1
    return Lt