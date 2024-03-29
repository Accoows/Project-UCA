def reduction(n):
    if n < 10:
        return 0
    elif n < 50:
        return 10
    else:
        return 20
    
def facture(n,p):
    prix = n*p
    liv = prix / 10
    if liv < 5:
        liv = 5
    if liv > 100:
        liv = 100
    r = reduction(n)
    total = prix * (1-r/100) + liv
    
    print("Prix : ", prix, "€")
    print("Réduction : ", r, "%")
    print("Coût livraison : ", liv, "€")
    print("----------------------------")
    print("Prix total (dont livraison) : ", prix, '€')
    