def boucle1():
    a = 0
    for i in range(11):
        a = i/10
        print(a, end='->')
        

def boucle2():
    a = 0
    for i in range(41):
        a = i * 0.5
        print(a, end='->')
       
def boucle3():
    for i in range(10,-12,-2):
        print(i, end='->')
        
        
        
def boucle4():
    for i in range(0,100):
        if i%10 == 0:
            print('')
        else:
            if i < 10:
                print('0',i,sep='',end=' ')
            else:
                print(i,sep='',end=' ')
            
####################################
                
def tiret(n):
    a = ""
    for i in range(len(n)):
        a += n[i]
        if i < len(n) - 1:
            a += "-"
    return a

def tirett(s):
    for i in range(len(s)):
        if i < len(s) - 1:
            print(s[i], end="-")
        else:
            print(s[i], end="")

# Exemple d'utilisation :
tiret("abcdef")


#########################################

def appartient(lettre,chaîne):
    """La variable appartient possède la même fonction que l'utilisation de
'in' mais en version beaucoup plus moche visuellement."""
    for i in range(len(chaîne)):
        if chaîne[i] == lettre:
            return True
    return False