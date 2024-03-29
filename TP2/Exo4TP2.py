#Exo 4 TP2

def fermat(n):
    return 2**(2**n)+1

def premier_facteur(n):
    ppns = 2
    while n % ppns != 0:
        ppns = ppns + 1
    return ppns
        
#print('Premier facteur de', 57, 'est', premier_facteur(57))

def fermat_pas_premier() :
    n = 0
    f = fermat(n)
    p = premier_facteur(f)
    while f == p :
        n = n + 1
        f = fermat(n)
        p = premier_facteur(f)
    print('fermat(',n,') = ',f,' n’est pas premier car il est divisé par ',p,sep='')