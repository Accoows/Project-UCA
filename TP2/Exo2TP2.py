#Exo 2 TP2

def suivant(u):
    if u == 1:
        return 1
    elif u%2 == 0:
        return u//2
    else:
        return (3*u)+1

assert suivant(12) == 6
assert suivant(10) == 5
assert suivant(8) == 4
assert suivant(5) == 16

#######################

def syracuse_rec(u):
    if u == 1:
        return 1
    if u%2 == 0:
        u = u//2
        print(u)
        return syracuse_rec(u)
    else:
        u = (3*u)+1
        print(u)
        return syracuse_rec(u)
    
###################    
    
def syracuse(u):
    while u != 1:
        if u%2 == 0:
            print(u)
            u = u//2
        else:
            print(u)
            u = (3*u)+1
    print()
    
    
######################    
    
def syracuse_suite(u):
    etape = 0
    while u != 1:
        if u%2 == 0:
            print(u)
            u = u//2
            etape += 1
        else:
            print(u)
            u = (3*u)+1
            etape += 1
    print("Nombres d'étapes",etape+1)