def multiplication(n):
    i = 0
    while i<=10:
        somme = i * n
        print(f'{i} * {n} = {somme}')
        i += 1
        
    
def abss(n):
    if n >= 0:
        return n
    else:
        return -n
    
def affiche_calcul_binaire(n) :
    while n >= 2:
        q = n//2
        r = n%2
        print(r , 'car' , n , '=' , '2 ×' , q ,'+', r )
        n = q
    print(n)
    
    
    
    
    
    
###############################################
    
def multiplicité(n,d):
    mult = 0
    while n%d==0:
        mult = mult+1
        n = n//d
    return mult

def affiche_facteurs(n):
    plus='' # Pour le premier facteur, on n'affiche pas le symbole +
    if n==0 or n==1:
        produit=str(n)
    else:
        produit=''
        d=2
        while n>1:
            p = multiplicité(n,d)
            if p!=0:
                produit = produit + plus + str(d) + "**" + str(p)
                plus=" + " # à partir de maintenant, on affichera les +
            n=n//(d**p) # Les parenthèses sont ici facultatives
            d=d+1
    print(produit)