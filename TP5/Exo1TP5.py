#Exo 1 TP 5

def apparait(x,L):
    for i in range(len(L)):
        if x == L[i]:
            return True
    return False

#######

def apparait2(x,L):
    for e in L:
        if x == e:
            return True
    return False

#######

def contient(L1,L2):
    for i in range(len(L1)):        
        if not apparait(L1[i],L2):
            return False
    return True

assert contient([],[3,5,1,0,2]) == True
assert contient([4,2,1,5],[1,3,0,8,4,2,7]) == False
assert contient([3,6,2,9],[1,5,3,2,6,9,7]) == True

#######

def commun(L1,L2):
    for i in range(len(L1)):
        if apparait(L1[i],L2):
            return L1[i]
    return False
        
        
        