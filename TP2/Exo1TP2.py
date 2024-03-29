#Exo 1 TP2

def fac_rec(n):
    if n == 0:
        return 1
    else:
        return fac_rec(n-1)*n
    
def fac(n):
    p = 1
    i = 0
    while i < n:
        i += 1
        p = p * i
    return p

fac(3000)
fac_rec(3000)