#Exo 1 TP 3

###################

#print(ord('a'),ord('A'),ord('D'),ord('O'),ord('0'),ord('3'))

def alphabet(c):
    n = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(n)):
        if n[i] == c:
            print(c,'est à la position', i+1)

#################

def est_chiffre(c):
    if ord(c) >= ord('0') and ord(c) <= ord('9'):
        return True
    return False

def est_chiffre_eff(c):
    return ord(c) >= ord('0') and ord(c) <= ord('9')
    
assert est_chiffre('9')==True
assert est_chiffre('0')==True
assert est_chiffre('*')==False

def masquer_numéro(s):
    n = ''
    e = '*'
    for i in range(len(s)):
        a = est_chiffre(s[i])
        if a == True:
            n = n+e
        else:
            n = n + s[i]
    return n