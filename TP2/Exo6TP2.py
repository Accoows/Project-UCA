#Exo 6 TP2

def étoile():
    print('*',sep='',end='')
    
def dièse():
    print('#',sep='',end='')
    
def nouvelle_ligne():
    print()
    
###########################


def ligne_unique(n,symb):
    i=0
    while i<n:
        symb()
        i=i+1

def tapis_A(largeur,hauteur):
    ligne_unique(largeur,étoile)
    nouvelle_ligne()
    i=0
    while i<hauteur-2:
        étoile()
        ligne_unique(largeur-2,dièse)
        étoile()
        nouvelle_ligne()
        i=i+1
    ligne_unique(largeur,étoile)
    nouvelle_ligne()
    
##########################
    
def pos_symb(n,p,symb1,symb2):
    i=0
    while i<n:
        if i==p:
            symb2()
        else:
            symb1()
        i=i+1
        
def tapis_B(largeur,hauteur):
    i = 0
    while i < hauteur:
        pos_symb(largeur, largeur-i-1,dièse,étoile)
        nouvelle_ligne()
        i += 1

    
###############################
        
def barre_1():
    print('/',end='')

def barre_2():
    print('\\',end='')
    
def tapis_C(largeur,hauteur):
    i=0
    m=hauteur//2
    n=largeur//2
    while i<m:
        pos_symb(n,n-i-1,dièse,barre_1)
        pos_symb(n,i,dièse,barre_2)
        nouvelle_ligne()
        i=i+1
    i=0
    while i<m:
        pos_symb(n,i,dièse,barre_2)
        pos_symb(n,n-i-1,dièse,barre_1)
        nouvelle_ligne()
        i=i+1
        
tapis_C(12,12)
    
