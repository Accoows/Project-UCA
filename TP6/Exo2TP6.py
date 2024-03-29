#Exo 2 TP6

inv = [('Pommes',10),('Carottes',5),('Radis',23),('Lentilles',534),('Poivrons',12)]

def maj_inventaire(inv,produit,n):
    for modifinv in range(len(inv)):
        (p,q) = inv[modifinv]
        if p == produit:
            inv[modifinv] = (p,q-n)
    
def maj_inventaire_error(inv,produit,n):
    for modifinv in range(len(inv)):
        (p,q) = inv[modifinv]
        if p == produit:
            if q >= n: 
                inv[modifinv] = (p,q-n)
                return
            else:
                raise ValueError
    raise IndexError
    print(inv)
    


def achat(inv,produit,n):
    try:
        maj_inventaire_error(inv,produit,n)
        print("Merci pour votre achat.")
    except ValueError:
        print("Produit en quantité insuffisante")
    except IndexError:
        print("Produit inexistant")
