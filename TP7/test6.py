def profondeur_max_pair(A):
    if est_feuille(A):
        if A%2==0:
            return 0
        else:
            return None
    else:
        rg = profondeur_max_pair(fg(A))
        rd = profondeur_max_pair(fd(A))
        if rg==None and rd==None:
            return None
        elif rg==None:
            return rd+1
        elif rd==None:
            return rg+1
        else:
            return max(rg,rd)+1
        
        
        
def remplacer(A, op1, op2):
if est_feuille(A):
return A
else:
Ag = remplacer(fg(A),op1,op2)
Ad = remplacer(fd(A),op1,op2)
if racine(A)==op1:
op=op2
else:
op=racine(A)
return arbre(op,Ag,Ad)

def compter(A, op):
if est_feuille(A):
return 0
else:
rg = compter(fg(A),op)
rd = compter(fd(A),op)
if racine(A) == op:
return 1 + rg + rd
else:
return rg + rd