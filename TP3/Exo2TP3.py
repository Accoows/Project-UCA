#Exo 2 TP 3

def code_cesar_lettre(c,k):
    if ord(c) < ord('A') or ord(c) > ord('Z'):
        return c
    elif ord(c)+k > ord('Z'):
        return chr(ord(c)+k-26)
    else :
        return chr(ord(c)+k)
    
def code_cesar(msg,k):
    res = ''
    n = len(msg)
    for i in range(n):
        m = msg[i]
        res += code_cesar_lettre(m,k)
    return res

###########################

def decode_cesar_lettre(c,k):
    if ord(c) < ord('A') or ord(c) > ord('Z'):
        return c
    elif ord(c)-k < ord('A'):
        return chr(ord(c)-k+26)
    else:
        return chr(ord(c)-k)
    
def decode_cesar(msg,k):
    res = ''
    n = len(msg)
    for i in range(n):
        m = msg[i]
        res += decode_cesar_lettre(m,k)
    return res

def decode_brute(msg):
    m = ''
    for i in range(1,26):
        m += decode_cesar(msg,i)
        print('Msg :', m, '-> la clé est :', i)
        m = ''
        