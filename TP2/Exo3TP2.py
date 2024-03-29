#Exo 3 TP2

def étoile():
    print('*',sep='',end='')
    
def dièse():
    print('#',sep='',end='')
    
def nouvelle_ligne():
    print()
    
##########################
    
def tapis_a(l,h):
    H = 0
    while H < h:
        L = 0
        while L < l:
            étoile()
            L+=1
        H += 1
        nouvelle_ligne()
        

def tapis_b(l,h):
    H = 0
    while H < h:
        L = 0
        while L < l:
            if L%2 == 0:
                étoile()
            else:
                dièse()
            L+=1
        H += 1
        nouvelle_ligne()
        
def tapis_c(l,h):
    H = 0
    while H < h:
        L = 0
        if H%2 == 0:
            while L < l:
                if L%2 == 0:
                    étoile()
                else:
                    dièse()
                L+=1
            H+=1
            nouvelle_ligne()
        else:
            while L < l:
                if L%2 == 0:
                    dièse()
                else:
                    étoile()
                L+=1
            H+=1
            nouvelle_ligne()
            

def tapis_d(l,h):
    H = 0
    compteur = 0
    while H < h:
        if compteur == 0:
            L = 0
            while L < l:
                if L%2 == 0:
                    étoile()
                else:
                    dièse()
                L+=1
            compteur+=1
            H+=1
            nouvelle_ligne()
        elif compteur == 1:
            L = 0
            while L < l:
                if L%2 == 0:
                    dièse()
                else:
                    étoile()
                L+=1
            compteur+=1
            H+=1
            nouvelle_ligne()
        else:
            L = 0
            while L < l:
                if L%2 == 0:
                    étoile()
                else:
                    étoile()
                L+=1
            compteur = 0
            H+=1
            nouvelle_ligne()