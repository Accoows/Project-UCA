from random import randint

#####
def choix_ordi():
    choix = randint(0,2)
    if choix == 0 :
        return 'pierre'
    elif choix == 1 :
        return 'feuille'
    else :
        return 'ciseaux'
#####
    
choix_humain = input('Quel est ton choix, humain ? ')
print('Humain, tu as choisi :', choix_humain)

#####

if choix_humain=='pierre' or choix_humain=='feuille' or choix_humain=='ciseaux':
    print('')
    print('Choix correct')
else :
    choix_humain = choix_ordi()
    print('Choix incorrect, je choisis pour toi : ', choix_humain)
    print('')

choix_ordinateur = choix_ordi()
print('')
print('Humain :',choix_humain)
print('Ordinateur :',choix_ordinateur)
print('')

######
cas_gagnant_1 = (choix_humain == 'pierre' and choix_ordinateur == 'ciseaux')
cas_gagnant_2 = (choix_humain == 'feuille' and choix_ordinateur == 'pierre')
cas_gagnant_3 = (choix_humain == 'ciseaux' and choix_ordinateur == 'feuille')

if choix_humain == choix_ordinateur :
    print('Vainqueur : égalite')
elif cas_gagnant_1 or cas_gagnant_2 or cas_gagnant_3:
    print('Vainqueur : humain')
else :
    print('Vainqueur : ordinateur')
