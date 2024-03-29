#Exo 5 TP1 

def essai(prix):
    pronostic = int(input('Quel est votre pronostic ?'))
    if pronostic == prix:
        print('Trop bien !')
        return True
    elif pronostic > prix:
        print('Trop haut !')
        return False
    else:
        print('Trop bas !')
        return False



def juste_prix_essais(n,prix):
    if n == 0:
        return False
    else:
        tentative = essai(prix)
        if tentative:
            return True
        else:
            return juste_prix_essais(n-1,prix)


def essai_ordinateur(valeur_min, valeur_max):
    if valeur_min > valeur_max:
        return False
    essai = (valeur_min + valeur_max) // 2
    print('Je devine', essai)
    estimation = input()
    if estimation == '=':
        return True
    elif estimation == '+':
        return essai_ordinateur(essai + 1, valeur_max)
    else: # estimation == '-'
        return essai_ordinateur(valeur_min, essai - 1)

def juste_prix2():
    trouvé = essai_ordinateur(0,100)
    if not trouvé:
        print('Tricheur !')


#essai_ordinateur(0,50000)
juste_prix2()